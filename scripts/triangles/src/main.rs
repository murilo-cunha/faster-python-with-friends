use std::collections::HashSet;
use std::fs;
use std::iter::FromIterator;

#[derive(Debug, Hash, PartialEq, Eq, Clone)]
struct Edge {
    left: u32,
    right: u32,
}

impl Edge {
    fn new(s: &str) -> Self {
        let mut chars = s.split(' ');
        Self {
            left: chars.next().unwrap().parse().unwrap(),
            right: chars.next().unwrap().parse().unwrap(),
        }
    }
}

fn load_edges(file_path: &str) -> Vec<Edge> {
    fs::read_to_string(file_path)
        .expect("Should have been able to read the file")
        .lines()
        .map(Edge::new)
        .collect()
}

fn to_undirected(directed: Vec<Edge>) -> HashSet<Edge> {
    let mut edges = HashSet::from_iter(directed.clone());
    // let reversed = HashSet::from_iter();
    edges.extend(directed.iter().map(|e| Edge {
        left: e.right,
        right: e.left,
    }));
    edges
}

fn calc_triangles(edges: HashSet<Edge>) -> u32 {
    let _edges = Vec::from_iter(edges);
    let mut num_triangles = 0;
    println!("{}", _edges.len());

    for i in 0.._edges.len() {
        if (i % 100).eq(&0) {
            println!("{} done", i);
        }
        let _ref = &_edges[i];
        for j in (i + 1).._edges.len() {
            let other = &_edges[j];
            if _ref.right.eq(&other.left) {
                for last in &_edges[(j + 1)..] {
                    if other.right.eq(&last.right) && last.left.eq(&_ref.left) {
                        num_triangles += 1
                    }
                }
            }
        }
    }
    num_triangles
}

fn main() {
    let directed = load_edges("../../static/facebook_combined.txt");
    let edges = to_undirected(directed);
    let n_triangles = calc_triangles(edges);
    println!("number of triangles: {}", n_triangles);
    assert_eq!(n_triangles, 1612010)
}
