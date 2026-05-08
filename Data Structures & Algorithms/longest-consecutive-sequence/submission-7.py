class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sn = sorted(set(nums))

        if not nums:
            return 0
        current = 1
        longest = 1

        for i in range(len(sn) - 1):
            if sn[i+1] - sn[i] == 1:
                current += 1
                longest = max(current, longest)
            else:
                current = 1
        return longest