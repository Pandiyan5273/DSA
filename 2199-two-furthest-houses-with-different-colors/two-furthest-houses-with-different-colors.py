class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        maxi=0
        for i in range(len(colors)-1):
            for j in range(i+1,len(colors)):
                if colors[i]==colors[j]:
                    continue
                else:
                    maxi=max(maxi,abs(i-j))
        return maxi

            