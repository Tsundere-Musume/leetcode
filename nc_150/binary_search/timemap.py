#Format: (key, value, timestamp)

from typing import DefaultDict


class TimeMap:
    def __init__(self):
        self.store = DefaultDict(list)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))
    def get(self, key: str, timestamp: int) -> str:
        e = self.store[key]
        l, r = 0, len(e)
        result = ("", -1)
        while l <= r:
            m = l + (r - l ) // 2
            if e[m][1] <= timestamp:
                result =e[m] if result[1] == -1 or  e[m][1] > result[1] else result
            if e[m][0] == timestamp:
                return result[0]

            if e[m][1] > timestamp:
                l = m + 1
            else:
                r = m  - 1
        return result[0]
