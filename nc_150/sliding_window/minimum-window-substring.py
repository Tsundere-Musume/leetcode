from collections import Counter, defaultdict
import math

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_counter = Counter(t)
        valid_count = 0
        #  find a valid window
        r = 0
        window = defaultdict(lambda  : 0)
        while r < len(s):
            c = s[r]
            window[c] += 1
            if c in t_counter and window[c] == t_counter[c]:
                valid_count+= 1
            if valid_count == len(t_counter):
                break
            r += 1

        l = 0
        rl, rr = float("Inf"),float("-Inf")
        while r < len(s):
            if math.isinf(rl) or (rr - rl ) > (r - l):
                rr = r
                rl = l

            c = s[l]
            if c not in t_counter or window[c] > t_counter[c]:
                l+= 1
                window[c]  -= 1
            else:
                r += 1
                if r < len(s):
                    window[s[r]] += 1
        if math.isinf(rl):
            return ""
        else:
            return s[rl : rr + 1]
        


