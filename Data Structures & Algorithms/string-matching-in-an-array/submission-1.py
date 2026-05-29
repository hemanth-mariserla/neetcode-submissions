class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        s = []
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] in words[j] and i != j:
                    s.append(words[i])
                    break
        return s