class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dc = {}
        
        for n in nums:
            if n in dc:
                dc[n] += 1
            else:
                dc[n] = 1
            
        v = sorted(dc, key=dc.get)

        return v[len(v) - k:]
