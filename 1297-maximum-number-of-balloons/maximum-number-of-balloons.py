class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        s=Counter(text)
        b=Counter("balloon")
        cnt=float("inf")
        for i in b:
            cnt=min(cnt,s[i]//b[i])
        return cnt