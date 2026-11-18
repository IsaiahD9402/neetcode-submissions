class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for c in s:
            substr = ""
            if c != "]":
                stack.append(c)
                continue
            while stack[-1] != "[":
                substr = stack.pop() + substr

            stack.pop()

            k = ""

            while stack and stack[-1].isdigit():
                k = stack.pop() + k
            
            for _ in range(int(k)):
                for char in substr:
                    stack.append(char)
                
        return "".join(stack)    