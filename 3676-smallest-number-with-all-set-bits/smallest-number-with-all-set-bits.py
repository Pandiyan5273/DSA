class Solution:
    def smallestNumber(self, n: int) -> int:
        
        a=n
        while True:
            ans=bin(a)[2:]
            if '0' in ans:
                a+=1
            else:
                return a    