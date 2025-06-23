class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        c=defaultdict(int)
        n=len(grid)
        for i in range(n):
            for j in range(n):
                c[grid[i][j]]+=1
    
        rep=mis=0
        for num in range(1,n*n+1):
            if c[num]==0:
                mis=num
            if c[num]==2:
                rep=num
        return [rep,mis]            