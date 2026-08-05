class Solution:
    def isValid(self, s: str) -> bool:
        valid = {"]":"[",")":"(","}":"{"}
        stack = []
        for i in s:
            if i in valid and stack and stack[-1] == valid[i]:
                stack.pop()
            else:
                stack.append(i)
        return False if stack else True