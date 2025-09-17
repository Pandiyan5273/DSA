class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d={}
        for i in range(len(arr)):
            if arr[i] not in d:
                d[arr[i]]=1
            else:
                d[arr[i]]+=1
        a=[]        
        for i in arr:
            if d[i]==1:
                a.append(i)   
        if k<=len(a):
            return a[k-1]
        else:
            return ""    
