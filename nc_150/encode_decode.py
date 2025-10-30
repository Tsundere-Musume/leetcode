from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        output = []
        output = [f'{len(word)}:{word}' for word in strs]
        return "".join(output)

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != ":":
                j += 1
            n = int(s[i: j])
            end = j + 1 + n
            output.append(s[j + 1: end])
            i = end
        return output

