class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l=0
        r=1
        maxi=0
        while r < len(prices):
            if prices[l]<prices[r]:
                p=prices[r]-prices[l]
                maxi=max(p,maxi)
            else:
                l=r
            r+=1
        return maxi