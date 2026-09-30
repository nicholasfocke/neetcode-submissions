class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_counts = {}
        for num in nums:
            num_counts[num] = num_counts.get(num, 0) + 1
    
        for num, count in num_counts.items():
            if count > 1:
                return True
        return False
        