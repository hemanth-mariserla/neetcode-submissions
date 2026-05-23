class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = defaultdict(list)
        for w in strs:
            k = ''.join(sorted(w))
            l[k].append(w)
        return list(l.values())