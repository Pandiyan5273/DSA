class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        s=Counter(nums)
        sorted_k=sorted(s.items(),key =lambda x :(-x[-1],x[0]))
        l=[]
        for i in range(min(k,len(nums))):
            l.append(sorted_k[i][0])
        return l
        print(sorted_k)