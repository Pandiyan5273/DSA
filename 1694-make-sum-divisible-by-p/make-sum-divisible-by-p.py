class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        tot=sum(nums)
        res=len(nums)
        rem=tot%p
        if tot %p==0:
            return 0
        seen={0:-1}
        pre=0
        for i,num in enumerate(nums):
            pre=(pre+num)%p
            tar=(pre-rem+p)%p
            if tar in seen:
                res=min(res,i-seen[tar])
            seen[pre]=i
        return res if res<len(nums) else -1    