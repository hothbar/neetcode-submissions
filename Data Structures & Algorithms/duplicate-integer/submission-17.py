class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l1 = []

        for num in nums:
            if num in l1:
                return True
            else:
                l1.append(num)

        return False