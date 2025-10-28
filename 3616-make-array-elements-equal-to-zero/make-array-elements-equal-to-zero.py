class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        f=sum(nums)
        ans=0
        ff=0
        for i in range(len(nums)):
            if nums[i]==0:
                if f==ff or f-ff==1 or ff-f==1:
                    ans+=1
                    if ff==f:
                        ans+=1
            else:
                ff+=nums[i]
                f-=nums[i]
        return ans                