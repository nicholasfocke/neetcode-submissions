class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1
        # mid = round(nums / 2)

        for i, num in enumerate(nums):
            if num < target:
                l += 1
            elif num > target:
                r -= 1
            else:
                return i 
        return -1