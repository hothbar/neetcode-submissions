class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, n in enumerate(nums):
            n2 = target - n
            if n2 in d:
                return [d.get(n2), i]
            d[n] = i
         