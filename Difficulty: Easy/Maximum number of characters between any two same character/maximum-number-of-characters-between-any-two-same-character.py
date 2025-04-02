#User function Template for python3

class Solution:

    def maxChars(self, s):
        char={}
        maxi=-1
        for i,c in enumerate(s):
            if c in char:
                d=i-char[c]-1
                maxi=max(maxi,d)
            else:
                char[c]=i
        if maxi==-1:
            return -1
        else:
            return maxi

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.maxChars(s)

        print(ans)

# } Driver Code Ends