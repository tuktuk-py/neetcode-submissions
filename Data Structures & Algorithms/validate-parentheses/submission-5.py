class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = {")":"(","]":"[","}":"{"}

        for n in s:
            if n in openToClose:
                if stack and stack[-1] == openToClose[n]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(n)
        return True if not stack else False 