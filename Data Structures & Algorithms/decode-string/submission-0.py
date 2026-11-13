class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            substr = ""
            if c != "]":
                stack.append(c)
            else:
                k = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)

        
        return "".join(stack)
                