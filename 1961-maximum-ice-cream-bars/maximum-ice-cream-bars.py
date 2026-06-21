class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        s={}
        for i in costs:
            if i  not in s:
                s[i]=1
            else:
                s[i]+=1
        cnt = 0                 
        for price, num in s.items():  
            if coins < price:
                break            

            affordable = min(num, coins // price)   
            cnt += affordable     
            coins -= affordable * price
        return cnt


