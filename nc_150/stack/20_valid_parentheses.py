class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        lookup = {
                "}": "{",
                "]": "[",
                ")": "(",
            }
        for letter in s:
            match letter:
                case '(' | '[' | '{':
                    stk.append(letter)
                case ')' | ']' | '}':
                    if not stk:
                        return False
                    p = stk.pop()
                    if lookup[letter] != p:
                        return False
                case _:
                    return False
        return len(stk) == 0
        
