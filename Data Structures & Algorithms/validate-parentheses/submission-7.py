class Solution:
    def isValid(self, s: str) -> bool:
        
        contains = collections.deque()

        corresponding = { ")": "(", 
                "}": "{", 
                "]": "["}

        for i in s:
            if i == "(" or i == "{" or i == "[":
                contains.append(i)
            elif not contains and i:
                return False
            elif corresponding[i] != contains.pop():
                return False
                

        print(contains)

        if not contains:
            return True
        else:
            return False
