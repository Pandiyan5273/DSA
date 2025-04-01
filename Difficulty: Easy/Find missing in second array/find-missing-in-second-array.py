#User function Template for python3


class Solution:
    def findMissing(self,a,b):
        res=[]
        s=set(b)
        for i in a:
            if i not in s:
                res.append(i)
        return res        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ob = Solution()
    ans = ob.findMissing(a, b)
    for each in ans:
        print(each, end=' ')
    print()
    print("~")

# } Driver Code Ends