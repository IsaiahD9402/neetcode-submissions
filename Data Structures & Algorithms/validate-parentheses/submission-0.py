class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedToOpenMap = { '}' : '{', ')' : '(', ']' : '['}

        for i in range(len(s)):
            if s[i] in closedToOpenMap:
                if not stack or stack.pop() != closedToOpenMap[s[i]]:
                    return False
            else:
                stack.append(s[i])
        return not stack
            

        
        