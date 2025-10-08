class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxi=0
        c=0
        cm={0:-1}

        for i in range(len(nums)):
            c+=1 if nums[i]==1 else -1
            if c in cm:
                maxi=max(maxi,i-cm[c])
            else:
                cm[c]=i 

        return maxi           