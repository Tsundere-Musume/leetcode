import java.util.Stack;

class Solution {
	public int[] dailyTemperatures(int[] temperatures) {
		int[] result = new int[temperatures.length];
		Stack<Integer> stk = new Stack<>();
		for (int i = 0; i < temperatures.length; ++i) {
			int curr = temperatures[i];
			while(!stk.isEmpty() && temperatures[stk.peek()] < curr){
				int idx = stk.pop();
				result[idx] = i - idx;
			}
			stk.push(i);

		}
		return result;
	}
}
