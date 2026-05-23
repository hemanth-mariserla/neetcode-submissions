class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k = 0
        if len(s) == 0:
            return True
        for i in t:
            if s[k] == i:
                k = k + 1
            if k >= len(s):
                return True
        return False 