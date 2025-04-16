class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        sumo=0
        res=float('inf')
        for r in range(0,len(nums)):
            sumo+=nums[r]
            while sumo>=target:
                res=min(res,r-l+1)
                sumo-=nums[l]
                l+=1
        return res if res !=float('inf') else 0        
        