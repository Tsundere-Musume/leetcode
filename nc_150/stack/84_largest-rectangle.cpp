#include "../leetcode.h"

class Solution {
  public:
    int largestRectangleArea(vector<int> &heights) {
        int result = 0;
        stack<int> areas;
        stack<int> idx;
        for (int i = 0; i < heights.size(); ++i) {
			int startIdx = i;
            while (!areas.empty() && areas.top() > heights[i]){
				startIdx = idx.top();
				int width = i - idx.top();
				result = max(result, width * areas.top());
				areas.pop();
				idx.pop();
            }
			areas.push(heights[i]);
			idx.push(startIdx);
        }

		while (!areas.empty()){
			int h = areas.top();
			int w = heights.size() - idx.top();
			result = max(result, h * w);
			areas.pop();
			idx.pop();
		}

		return result;
    }
};
