#User function Template for python3

class Solution:
    def canReach(self, a, b, x):
        req=abs(a)+abs(b)
        if x<req:
             return 0
        if (x-req)%2==0:
            return 1
        else:
            return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        a,b,x=map(int,input().split())
        
        ob = Solution()
        print(ob.canReach(a,b,x))
        print("~")
# } Driver Code Ends