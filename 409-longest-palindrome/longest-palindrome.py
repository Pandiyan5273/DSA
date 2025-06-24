class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen=set()
        ans=0
        for i in s:
            if i in seen:
                seen.remove(i)
                ans+=2
            else:
                seen.add(i)
        return ans+1 if seen else ans            