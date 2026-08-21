class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        length = len(nums)
        product = 1
        j = 0
        lst = []

        if all(x == 0 for x in nums):
            return [0] * len(nums)
        
        for i in range(len(nums)):
            # skip = i
            # if i == len(nums):
            #     skip = i
        
            j = 0
            product = 1
            while j < length:
                if j != i:
                    product *= nums[j]
                j += 1
            lst.append(product)
            
        return lst




        