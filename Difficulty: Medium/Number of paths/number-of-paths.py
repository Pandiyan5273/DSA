class Solution:
    def numberOfPaths(self, m, n):
        dp=[[0]*n for i in range(m)]
        
        for i in range(m):
            dp[i][0]=1
        for j in range(n):
            dp[0][j]=1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        M = int(input())
        N = int(input())

        ob = Solution()
        ans = ob.numberOfPaths(M, N)
        print(ans)

        print("~")

# } Driver Code Ends