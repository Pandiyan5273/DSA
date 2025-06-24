class Solution:
    def scoreOfString(self, s: str) -> int:
        ans=[]
        si=0
        for i in s:
            ans.append(ord(i))
        for i in range(len(ans)-1):
            si+=abs(ans[i]-ans[i+1])
        return si    