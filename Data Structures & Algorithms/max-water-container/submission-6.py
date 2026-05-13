class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            d = r - l
            h = min(heights[l], heights[r])
            a = max(a, d * h)
            print(a)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return a



        