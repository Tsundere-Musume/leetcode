#include "leetcode.h"

class Solution {
public:
  vector<int> topKFrequent(vector<int> &nums, int k) {
    vector<vector<int>> bucket(nums.size() + 1);
    unordered_map<int, int> counter;

    for (int num : nums) {
		counter[num] = 1 + counter[num];
    }

	for(const auto& entry: counter){
		bucket[entry.second].push_back(entry.first);
	}

	vector<int> result;
	for (auto b = bucket.rbegin(); b != bucket.rend(); ++b) {
		for (int n : *b) {
			result.push_back(n);
			if (result.size() == k){
				return result;
			}
		}
	}
	return result;
  }
};


