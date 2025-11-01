#include "../leetcode.h"

class Solution {
  public:
    int trap(vector<int> &height) {
        int n = height.size();
        int l = 0;
        int r = n - 1;
        int left_max = height[l];
        int right_max = height[r];
        int result = 0;
        while (l < r) {
            if (left_max < right_max) {
				l++;
				left_max = max(left_max, height[l]);
				result += (left_max - height[l]);
            } else {
				r--;
				right_max = max(right_max, height[r]);
				result += (right_max - height[r]);
            }
        }

        return result;
    }
};
