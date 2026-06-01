from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(int)
        if len(s) != len(t):
            return False
        for i in s:
            d[i] += 1
        for i in t:
            if d[i] == 0:
                return False
            else:
                d[i] -= 1
        return True