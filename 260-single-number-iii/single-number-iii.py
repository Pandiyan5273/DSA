class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans=[]
        c=Counter(nums)
        for i,j in c.items():
            if j==1:
                ans.append(i)
        return ans        