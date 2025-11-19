#include "../leetcode.h"

class Solution {
  public:
    bool searchMatrix(vector<vector<int>> &matrix, int target) {
        int t = 0;
        int b = matrix.size() - 1;
        while (t <= b) {
            int mm = t + (b - t) / 2;
            vector<int> row = matrix[mm];
            int l = 0;
            int r = matrix[0].size() - 1;
            if (target >= row[l] && target <= row[r]) {
                while (l <= r) {
                    int m = l + (r - l) / 2;
                    if (target == row[m]) {
                        return true;
                    } else if (target > row[m]) {
                        l = m + 1;
                    } else {
                        r = m - 1;
                    }
                }
				return false;

            } else if (target > row[r]) {
                t = mm + 1;
            } else {
                b = mm - 1;
            }
        }

        return false;
    }
};
