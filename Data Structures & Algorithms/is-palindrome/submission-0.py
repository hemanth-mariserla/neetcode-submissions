class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = ""
        for i in s:
            if (i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z') or (i >= '0' and i <= '9'):
                l += i 
        l = l.lower()
        i = 0
        j = len(l) - 1
        while i < j:
            if l[i] != l[j]:
                return False
            i += 1
            j -= 1
        return True