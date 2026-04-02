impl Solution {
    pub fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
        let mut heap = BinaryHeap::with_capacity((k + 1) as usize);
        for num in nums {
            heap.push(Reverse(num));

            if heap.len() > k as usize {
                heap.pop();
            }
        }

        match heap.peek().unwrap() {
            Reverse(v) => *v,
            _ => 0,
        }
    }
}
