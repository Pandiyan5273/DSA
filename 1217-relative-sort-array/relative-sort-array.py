class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans=[]
        for i in arr2:
            for j in range(len(arr1)):
                if i ==arr1[j]:
                    ans.append(i)
        n=[]
        for i in arr1:
            if i not in arr2:
                n.append(i)
        n.sort()        

        return ans+n
