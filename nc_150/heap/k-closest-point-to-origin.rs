use std::collections::BinaryHeap;

impl Solution {
    pub fn k_closest(points: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let mut heap = BinaryHeap::with_capacity((k + 1) as usize);
        for point in points {
            let x = point[0];
            let y = point[1];
            let dist_sq = x * x + y * y;

            heap.push((dist_sq, point));

            if heap.len() > k as usize {
                heap.pop();
            }
        }

        let mut result = Vec::new();
        while let Some((_, v)) = heap.pop() {
            result.push(v);
        }
        result
    }
}
