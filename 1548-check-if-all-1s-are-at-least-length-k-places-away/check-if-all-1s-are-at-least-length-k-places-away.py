class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        mini=-1
        n=len(nums)

        for i in range(n):
            if nums[i]==1:
                if mini==-1:
                    mini=i
                else:
                    if i-mini<=k:
                        return False
                    mini=i
        return True            