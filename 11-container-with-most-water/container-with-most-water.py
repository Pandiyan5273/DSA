class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxi=float("-inf")
        l=0
        r=len(height)-1
        while l<r:
            area=(r-l)* min(height[l],height[r])
            maxi=max(area,maxi)
            if height[l]< height[r]:
                l+=1
            else:
                r-=1
        return maxi
