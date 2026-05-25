class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k = 0
        m = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ' and m == 1:
                break
            elif s[i] != ' ' and m == 0:
                m = 1
            if s[i] != ' ':
                k = k + 1
        return k