class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            key = tuple(sorted(i))
            if key not in res:
                res[key] = []
            res[key].append(i)
        return list(res.values())