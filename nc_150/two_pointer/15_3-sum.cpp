#include "../leetcode.h"

class Solution {
public:
  vector<vector<int>> threeSum(vector<int> &nums) {
    vector<vector<int>> result;
    sort(nums.begin(), nums.end());

    for (int f = 0; f < nums.size(); ++f) {
      // all numbers are positive after this point, so result can't be zero
      if (nums[f] > 0) {
        break;
      }
      if (f > 0 and nums[f] == nums[f - 1]) {
        continue;
      }
      int l = f + 1;
      int r = nums.size() - 1;
      while (l < r) {
        int sum = nums[f] + nums[l] + nums[r];
        if (sum == 0) {
          result.push_back(vector<int>{nums[f], nums[l], nums[r]});
          r--;
          do {
            l++;
          } while (nums[l] == nums[l - 1] && l < r);
        } else if (sum > 0) {
          r--;
        } else {
          l++;
        }
      }
    }
    return result;
  }
};
