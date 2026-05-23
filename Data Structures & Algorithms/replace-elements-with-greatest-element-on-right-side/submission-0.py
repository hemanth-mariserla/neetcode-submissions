class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        k = max(arr)
        for i in range(len(arr)-1):
            if arr[i] == k:
                k = max(arr[i+1:])
            arr[i] = k
        arr[len(arr)-1] = -1
        return arr