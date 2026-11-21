class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d={}
        for st in strs:
            k=tuple(sorted(st))
            d.setdefault(k,[]).append(st)
        return list(d.values())