class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        tot=sum(skill)
        if (2*tot)%len(skill):
            return -1
        res=0
        target=(2*tot)//len(skill)
        cnt=Counter(skill)
        for s in skill:
            if not cnt[s]:
                continue
            diff=target-s
            if not cnt[diff]:
                return -1
            res+=diff*s
            cnt[s]-=1
            cnt[diff]-=1
        return res        
        