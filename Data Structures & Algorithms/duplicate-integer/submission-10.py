class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if len(nums) == 0:
            return False
        
        seT = list(set(nums))

        return len(seT) != len(nums)