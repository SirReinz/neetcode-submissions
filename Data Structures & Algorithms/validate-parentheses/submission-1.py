from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        r = {')': '(', '}': '{', ']': '['}
        stack = []
        for i in s:
            print(i)
            if len(stack) != 0 and i in list(r.keys()) and r[i] == stack[-1]:
                stack.pop()
                print(i, "POPPED")
            else:
                stack.append(i)
                print(i, "APPENDED")
        if len(stack) != 0:
            return False
        return True