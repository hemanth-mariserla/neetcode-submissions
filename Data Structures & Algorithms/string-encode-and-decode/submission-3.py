class Solution:

    def encode(self, strs: List[str]) -> str:
        t = ""
        for i in range(len(strs)):
            t += strs[i] + '.'
        return t
    def decode(self, s: str) -> List[str]:
        t = []
        k = ""
        for i in range(len(s)):
            if s[i] == '.':
                t.append(k)
                k = ""
                continue
            k += s[i]
        return t