use pyo3::wrap_pymodule;
use pyo3::{exceptions::PyTypeError, prelude::*, PyErr};
use std::collections::HashMap;

/// Calculate triangles for network.
///
/// I.e.: use graph from https://snap.stanford.edu/data/ego-Facebook.html.
#[pymodule]
fn triangles(_py: Python, module: &PyModule) -> PyResult<()> {
    type NeighborNodes = Vec<u16>;
    type Graph = HashMap<u16, NeighborNodes>;

    /// Calculate number of triangles.
    ///
    /// 0. Track nodes visited and number of triangles
    /// 1. For each node:
    ///     a. Track neighbors visited
    ///     b. Get it's neighbors
    ///     c. If the neighbor node has not been visited, check it's neighbors
    ///      ("far neighbor")
    ///     d. If the "far neighbor" has not been visited (either nodes or neighbors), check
    ///      that the current node is in the "far neighbor's" neighbors and increment
    ///      triangle count if present
    ///     e. Add neighbor node to neighbors visited
    /// 2. Add node to nodes visited
    #[pyfn(module)]
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
    Ok(())
}

/// Fibonacci numbers.
#[pymodule]
fn fibonacci(_py: Python, module: &PyModule) -> PyResult<()> {
    /// Calculate the nth Fibonacci number.
    #[pyfn(module)]
    fn fib(n: u32) -> PyResult<u32> {
        if n <= 1 {
            return Ok(n);
        }
        Ok(fib(n - 2)? + fib(n - 1)?)
    }
    Ok(())
}

/// Rust source code.
#[pymodule]
fn rs(_py: Python, module: &PyModule) -> PyResult<()> {
    module.add_wrapped(wrap_pymodule!(triangles))?;
    module.add_wrapped(wrap_pymodule!(fibonacci))?;
    Ok(())
}
