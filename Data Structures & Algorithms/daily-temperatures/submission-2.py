class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # stack of pairs [val, index]

        for i, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                stackVal, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append([val, i])
        
        return res