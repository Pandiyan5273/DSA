#User function Template for python3

class Solution:
    def closest3Sum(self, arr, target):
        n=len(arr)
        arr.sort()
        res=0
        mindiff=float("inf")
        for i in range(n-2):
            l,r=i+1,n-1
            while l<r:
                currsum=arr[i]+arr[l]+arr[r]
                if abs(currsum-target)<mindiff:
                    mindiff=abs(currsum-target)
                    res=currsum
                elif abs(currsum-target)==mindiff:
                    res=max(res,currsum)
                if currsum>target:
                    r-=1
                else:
                    l+=1
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        target = int(input())
        ob = Solution()
        print(ob.closest3Sum(arr, target))
        print("~")

# } Driver Code Ends