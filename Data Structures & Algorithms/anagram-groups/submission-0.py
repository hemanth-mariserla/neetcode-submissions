class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = []
        v = []
        for i in strs:
            k = []
            if i in v:
                continue
            for j in strs:
                if sorted(i) == sorted(j):
                    k.append(j)
                    v.append(j)
            l.append(k)
        return l