#include "leetcode.h"

class Solution {
public:
  vector<int> twoSum(vector<int> &nums, int target) {
    unordered_map<int, int> m;
    for (int i = 0; i < nums.size(); ++i) {
      int curr = nums[i];
      if (m.find(target - curr) == m.end()) {
        m[curr] = i;
      } else {
        return {m[target - curr], i};
      }
    }
    return {};
  }
};
