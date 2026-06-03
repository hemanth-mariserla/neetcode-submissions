class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        s = list(set(nums))
        i = 0
        while i < len(s):
            if s[i] - 1 not in s:
                current = s[i]
                c = 0
                while current in s:
                    current += 1
                    c += 1
                length = max(c,length)
            i += 1
        return length