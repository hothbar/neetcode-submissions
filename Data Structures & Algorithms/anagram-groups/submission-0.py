class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for st in strs:
            sortedSt = ''.join(sorted(st))
            output[sortedSt].append(st)
        return list(output.values())