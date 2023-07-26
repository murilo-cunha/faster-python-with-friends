use std::{collections::HashMap, env, fs};

use pyo3::{exceptions::PyTypeError, prelude::*, PyErr};

type NeighborNodes = Vec<u16>;
type Graph = HashMap<u16, NeighborNodes>;

/// Load undirected graph from CSV file with ` ` delimiter.
fn load_graph(file_path: Option<&str>) -> Graph {
    let _expected_token = "missing token in line";
    let mut edges: Vec<(u16, u16)> = fs::read_to_string(
        file_path.unwrap_or(&env::var("FB_DATA").expect("data file path not found")),
    )
    .expect("could not read file")
    .lines()
    .map(|l| {
        let mut tokens = l.split(' ');
        (
            tokens.next().expect(_expected_token).parse().unwrap(),
            tokens.next().expect(_expected_token).parse().unwrap(),
        )
    })
    .collect();
    edges.extend(edges.clone().iter().map(|&l| (l.1, l.0)));

    let mut graph: Graph = HashMap::new();
    for (node, neighbor) in edges {
        let mut _neighbors = graph.entry(node).or_default();
        _neighbors.push(neighbor);
    }
    graph
}

///     Calculate number of triangles.
///
///     0. Track nodes visited and number of triangles
///     1. For each node:
///         a. Track neighbors visited
///         b. Get it's neighbors
///         c. If the neighbor node has not been visited, check it's neighbors
///          ("far neighbor")
///         d. If the "far neighbor" has not been visited (either nodes or neighbors), check
///          that the current node is in the "far neighbor's" neighbors and increment
///          triangle count if present
///         e. Add neighbor node to neighbors visited
///     2. Add node to nodes visited
fn calc_triangles(graph: Graph) -> PyResult<u32> {
    let mut num_triangles = 0;

    let mut visited: NeighborNodes = Vec::new();
    for node in graph.keys() {
        let mut neighbors_visited: NeighborNodes = Vec::new();
        for neighbor in graph
            .get(node)
            .ok_or(PyErr::new::<PyTypeError, _>("key error"))?
        {
            if !visited.contains(neighbor) {
                for far_neighbor in graph
                    .get(neighbor)
                    .ok_or(PyErr::new::<PyTypeError, _>("key error"))?
                {
                    if (!neighbors_visited.contains(far_neighbor))
                        && (!visited.contains(far_neighbor))
                        && (graph
                            .get(far_neighbor)
                            .ok_or(PyErr::new::<PyTypeError, _>("key error"))?
                            .contains(node))
                    {
                        num_triangles += 1;
                    }
                }
            }
            neighbors_visited.push(*neighbor);
        }
        visited.push(*node);
    }

    Ok(num_triangles)
}

/// Loads graph from path `p` and calculate triangles.
#[pyfunction]
fn load_and_calc(p: Option<&str>) -> PyResult<u32> {
    let graph = load_graph(p);
    calc_triangles(graph)
}

/// Calculating triangles implemented in Rust.
#[pymodule]
fn rs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(load_and_calc, m)?)?;
    Ok(())
}
