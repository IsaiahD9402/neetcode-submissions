import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        l, r = 0, len(nums) - 1

        while True:
            p = random.randint(l, r)
            pivot = nums[p]
            nums[p], nums[r] = nums[r], nums[p]

            store = l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[store] = nums[store], nums[i]
                    store += 1
            nums[store], nums[r] = nums[r], nums[store]

            if store == target:
                return nums[store]
            elif store < target:
                l = store + 1
            elif store > target:
                r = store - 1

