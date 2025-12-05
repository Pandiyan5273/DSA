class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g={}
        for w in strs:
            k=tuple(sorted(w))
            g.setdefault(k,[]).append(w)
        return list(g.values())