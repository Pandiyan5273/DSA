class Solution:
    def findLucky(self, arr: List[int]) -> int:
        a=Counter(arr)
        ans=0
        for i,j in a.items():
            if i==j:
                ans=max(ans,i)

        return ans if ans !=0 else -1        