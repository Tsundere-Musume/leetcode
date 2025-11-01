#include "../leetcode.h"

class MinStack {
  private:
    stack<int> stk;
    stack<int> min_stack;

  public:
    MinStack() {}

    void push(int val) {
        stk.push(val);
        int min_val = min_stack.size() == 0 ? val : min(val, min_stack.top());
        min_stack.push(min_val);
    }

    void pop() {
        stk.pop();
        min_stack.pop();
    }

    int top() { return stk.top(); }

    int getMin() { return min_stack.top(); }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
