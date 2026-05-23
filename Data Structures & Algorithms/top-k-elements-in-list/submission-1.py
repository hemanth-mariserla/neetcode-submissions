class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = Counter(nums)
        return [key for key, val in l.most_common(k)]