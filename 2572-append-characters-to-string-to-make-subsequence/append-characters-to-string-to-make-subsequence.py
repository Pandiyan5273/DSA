class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ans=0
        l=0
        r=0
        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                r+=1
            l+=1

        return len(t)-r         
        