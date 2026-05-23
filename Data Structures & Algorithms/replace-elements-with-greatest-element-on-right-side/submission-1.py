class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        k = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            temp = arr[i]
            arr[i] = k
            k = max(temp, arr[i])
        arr[len(arr)-1] = -1
        return arr