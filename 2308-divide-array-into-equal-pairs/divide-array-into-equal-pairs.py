class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        ans=Counter(nums)
        for c in ans.values():
            if c%2!=0:
                return False
        return True        