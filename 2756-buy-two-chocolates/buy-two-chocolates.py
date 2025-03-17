class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices=sorted(prices)
        s=0
        for i in range(2):
            s+=prices[i]
        if money-s <0:
            return money
        else:
            return money-s     

        