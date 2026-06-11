class Solution:
    def maxArea(self, h: List[int]) -> int:
        area = float('-inf')
        i = 0
        j = len(h)-1
        while i < j:
            area = max(area, min(h[i],h[j])*(j-i))
            if h[i] > h[j]:
                j -= 1
            else:
                i += 1
        return area