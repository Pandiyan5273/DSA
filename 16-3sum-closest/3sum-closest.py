class Solution:
    def threeSumClosest(self, arr: List[int], target: int) -> int:
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