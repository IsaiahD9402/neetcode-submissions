class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {"]" : "[",
                      "}" : "{",
                      ")" : "("}

        stack = []

        for c in s:
            if c in bracketMap:
                if stack and bracketMap[c] == stack.pop():
                    continue
                else:
                    return False
            stack.append(c)
        
        return True if not stack else False