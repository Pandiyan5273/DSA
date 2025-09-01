from collections import Counter
class Solution:
    def frequencyCount(self, arr):
        d=Counter(arr)
        ans=[]
        for i in range(1,len(arr)+1):
            if d[i]:
                ans.append(d[i])
            else:
                ans.append(0)
        return ans        

