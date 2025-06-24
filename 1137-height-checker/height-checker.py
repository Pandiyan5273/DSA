class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        cnt=0
        exp=sorted(heights)
        for i in range(len(exp)):
            if heights[i]!=exp[i]:
                cnt+=1
        return cnt        