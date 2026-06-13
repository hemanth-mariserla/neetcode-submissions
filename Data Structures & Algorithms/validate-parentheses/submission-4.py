class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {']' : '[', '}' : '{', ')' : '('}
        for i in s:
            if i == '{' or i == '[' or i == '(':
                stack.append(i)
                continue
            if len(stack) == 0 or d[i] != stack[-1]:
                return False
            else:
                stack.pop()
        return len(stack) == 0