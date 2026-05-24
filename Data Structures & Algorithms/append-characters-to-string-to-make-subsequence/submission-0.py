class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        k = 0
        for i in s:
            if t[k] == i:
                k = k + 1
            if k >= len(t):
                break
        return len(t) - k