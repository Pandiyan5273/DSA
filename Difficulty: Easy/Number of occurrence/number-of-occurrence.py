from collections import Counter
class Solution:
    def countFreq(self, arr, target):
        c=Counter(arr)
        return c.get(target,0)
        
        