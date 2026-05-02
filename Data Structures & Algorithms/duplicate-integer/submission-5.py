class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        return len(nums) != len(set(nums))

        