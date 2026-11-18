import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        target = len(nums) - k

        while True:
            p = random.randint(left, right)
            nums[p], nums[right] = nums[right], nums[p]
            pivot = nums[right]

            ptr = left

            for i in range(left, right):
                if nums[i] < pivot:
                    nums[ptr], nums[i] = nums[i], nums[ptr]
                    ptr += 1
            
            nums[ptr], nums[right] = nums[right], nums[ptr]
                
            if ptr == target:
                return nums[ptr]
            elif target > ptr:
                left = ptr + 1
            else:
                right = ptr - 1