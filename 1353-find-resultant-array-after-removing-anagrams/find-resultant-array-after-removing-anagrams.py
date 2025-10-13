class Solution:
    def removeAnagrams(self, nums: List[str]) -> List[str]:
        ans=[nums[0]]
        n=len(nums)
        for i in range(1,n):
            if sorted(nums[i])!= sorted(nums[i-1]):
                ans.append(nums[i])
        return ans        
            