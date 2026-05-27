class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = [0]*26
        for i in s:
            d[ord(i)-ord('a')] += 1
        for i in t:
            if d[ord(i)-ord('a')] == 0:
                d[ord(i)-ord('a')] += 1
            else:
                d[ord(i)-ord('a')] -= 1
        return sum(d) == 0