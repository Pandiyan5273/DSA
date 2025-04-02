#User function Template for python3

class Solution:
    def reverseWithSpacesIntact(self, s):
        n=len(s)
        s=list(s)
        l=0
        r=n-1
        while(l<r):
            if s[l]==" ":
                l+=1
            elif s[r]==" ":
                r-=1
            else:
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
        return "".join(s)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.reverseWithSpacesIntact(s)
        print(ans)
# } Driver Code Ends