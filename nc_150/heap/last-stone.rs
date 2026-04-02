use std::collections::BinaryHeap;

impl Solution {
    pub fn last_stone_weight(stones: Vec<i32>) -> i32 {
        let mut heap = BinaryHeap::new();
        for num in stones {
            heap.push(num);
        }

        while heap.len() > 1 {
            let x = heap.pop().unwrap();
            let y = heap.pop().unwrap();
            
            let diff = (x - y).abs();
            if  diff != 0 {
                heap.push(diff);
            }

        }

        match heap.peek() {
            Some(val) => *val,
            None => 0
        }
    }
}
