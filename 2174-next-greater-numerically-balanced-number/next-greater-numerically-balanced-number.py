from collections import Counter

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def is_beautiful(num):
            l = [int(i) for i in str(num)]
            c = Counter(l)
            for i, j in c.items():
                if i != j:
                    return False
            return True
        
        n += 1
        while True:
            if is_beautiful(n):
                return n
            n += 1
