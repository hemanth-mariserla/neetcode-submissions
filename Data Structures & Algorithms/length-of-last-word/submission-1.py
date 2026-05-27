class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                k += 1
            elif k > 0:
                break
        return k