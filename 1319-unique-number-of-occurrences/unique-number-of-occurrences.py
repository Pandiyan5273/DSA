class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        c=Counter(arr)
        s=[j for i,j in c.items()]
        ans=set()
        for i in s:
            if i not in ans:
                ans.add(i)
            else:
                return False
        return True            