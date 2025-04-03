class Solution:
    def scoreOfString(self, s: str) -> int:
        l=[]
        for i in s:
            a=ord(i)
            l.append(a)
        n=len(l)    
        sumi=0    
        for i in range(n-1):
            sumi+=abs(l[i]-l[i+1])
        return sumi    
