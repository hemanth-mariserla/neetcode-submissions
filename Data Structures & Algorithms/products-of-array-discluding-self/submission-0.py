class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        t = [1]*len(nums)
        k = 1
        for i in range(len(nums)):
            t[i] = k
            k *= nums[i]
        k = 1
        for i in range(len(nums)-1,-1,-1):
            t[i] *= k
            k *= nums[i]
        return t