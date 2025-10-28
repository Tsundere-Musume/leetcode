#include "leetcode.h"

class Solution {
private:
  string get_key(const string &str) {
    string result = str;
    sort(result.begin(), result.end());
    return result;
  }

public:
  vector<vector<string>> groupAnagrams(vector<string> &strs) {
	unordered_map<string, vector<string>> groups;
    for (const string &word : strs) {
		groups[get_key(word)].push_back(word);
    }

    vector<vector<string>> result;
	for (auto& pair : groups){
		result.push_back(pair.second);
	}
    return result;
  }
};
