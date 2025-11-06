from typing import List 

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        idx_arr = list(range(len(position)))
        idx_arr.sort(key = lambda x : position[x], reverse=True)
        stk = []
        for idx in idx_arr:
            p = position[idx]
            s = speed[idx]
            time = (target - p) / s
            if not stk or stk[-1] < time:
                stk.append(time)
        return len(stk)
        
