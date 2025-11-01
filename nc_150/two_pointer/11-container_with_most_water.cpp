#include "../leetcode.h"

class Solution {
  public:
    int maxArea(vector<int> &height) {
        int n = height.size();
        int l = 0;
        int r = n - 1;

        int max_area = 0;
        while (l < r) {
            int cur_area = (r - l) * min(height[l], height[r]);
            max_area = max(max_area, cur_area);
            if (height[l] < height[r]) {
                l++;
            } else {
                r--;
            }
        }
        return max_area;
    }
};
