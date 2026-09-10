class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {"(" : ")", 
                      "{" : "}",
                      "[" : "]"}
        stack = collections.deque()

        for c in s:
            if c not in bracketMap and not stack:
                return False
            elif c not in bracketMap and bracketMap[stack[-1]] != c:
                return False
            elif c not in bracketMap and bracketMap[stack[-1]] == c:
                stack.pop()
            elif c in bracketMap:
                stack.append(c)


        if len(stack) > 0:
            return False
        
        return True
            