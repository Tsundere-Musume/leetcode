#include "../leetcode.h"

#define operate(stk, op)                                                       \
    do {                                                                       \
        int a = stk.top();                                                     \
        stk.pop();                                                             \
        int b = stk.top();                                                     \
        stk.pop();                                                             \
        stk.push(b op a);                                                      \
    } while (false)

class Solution {
  public:
    int evalRPN(vector<string> &tokens) {
        stack<int> stk;
        for (string token : tokens) {
            if (token == "+") {
                operate(stk, +);
            } else if (token == "-") {
                operate(stk, -);
            } else if (token == "*") {
                operate(stk, *);
            } else if (token == "/") {
                operate(stk, /);
            } else {
                stk.push(stoi(token));
            }
        }
        return stk.top();
    }
};
