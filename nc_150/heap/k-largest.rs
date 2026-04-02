use std::cmp::Reverse;
use std::collections::BinaryHeap;

struct KthLargest {
    heap: BinaryHeap<Reverse<i32>>,
    cap: i32,
}

impl KthLargest {
    pub fn new(k: i32, nums: Vec<i32>) -> Self {
        let mut heap = BinaryHeap::new();
        for num in nums {
            heap.push(Reverse(num));
            if heap.len()  > k as usize {
                heap.pop();
            }
        }
        Self {
            heap: heap,
            cap: k
        }

    }

    pub fn add(&mut self, val: i32) -> i32 {
        self.heap.push(Reverse(val));
        if self.heap.len()  > self.cap as usize {
            self.heap.pop();
        }
        match self.heap.peek().unwrap() {
            Reverse(k) => *k,
            _ => 0,
        }
    }
}
