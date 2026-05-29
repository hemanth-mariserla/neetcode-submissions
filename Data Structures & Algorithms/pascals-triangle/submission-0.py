class Solution:
    def generate(self, n: int) -> List[List[int]]:
        s = []
        for i in range(1,n+1):
            k = []
            c = 1
            for j in range(1,i+1):
                k.append(c)
                c = c * (i-j)//j
            s.append(k)
        return s