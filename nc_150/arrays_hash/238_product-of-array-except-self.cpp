#include "../leetcode.h"

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
		vector<int> result(nums.size(), 1);

		int pre = 1;
		for(int i = 0; i < nums.size(); ++i){
			result[i] = pre;
			pre *= nums[i];
		}

		int suf = 1;
		for (int i = nums.size() - 1; i >= 0; --i){
			result[i] *= suf;
			suf *= nums[i];
		}
        
		return result;
    }
};
