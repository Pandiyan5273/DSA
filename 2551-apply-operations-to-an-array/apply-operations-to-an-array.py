class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
            else:
                continue
        zc=0
        for i in nums:
            if i==0:
                zc+=1
        res=[]
        for i in nums:
            if i>0:
                res.append(i)

        for i in range(zc):
            res.append(0)                
        return res
        