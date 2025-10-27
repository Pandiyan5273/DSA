class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        d=[row.count("1") for row in bank]
        tot=0
        prev=0
        for c in d:
            if c>0:
                tot+=prev*c
                prev=c
        return tot        