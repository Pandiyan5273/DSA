class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0
        c=Counter(nums)
        for i,j in c.items():
            if j==1:
                ans=i
        return ans        