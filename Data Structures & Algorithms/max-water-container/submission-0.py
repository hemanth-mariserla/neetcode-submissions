class Solution:
    def maxArea(self, h: List[int]) -> int:
        maxi = float('-inf')
        for i in range(len(h)):
            for j in range(len(h)):
                maxi = max(maxi, min(h[i],h[j])*(j-i))
        return maxi