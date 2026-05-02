class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seT = set()
        for n in nums:
            if n in seT:
                return True
            else:
                seT.add(n)
        return False
        