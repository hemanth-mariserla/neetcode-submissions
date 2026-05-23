class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k = 0
        f = 0
        for i in range(len(nums)):
            if target - nums[i] in nums[i+1:]:
                k = target - nums[i]
                nums[i] = 0
                f = i
                break
        for i in range(f+1,len(nums)):
            if k == nums[i]:
                return [f,i]
                break