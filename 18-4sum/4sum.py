class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        st=set()     
        for i in range(n):
            for j in range(i+1,n):
                hashi=set()
                for k in range(j+1,n):
                    sumi=nums[i]+nums[j]+nums[k]
                    four=target-sumi
                    if four in hashi:
                        temp=[nums[i],nums[j],nums[k],four]
                        temp.sort()
                        st.add(tuple(temp))
                    else:
                        hashi.add(nums[k])    
        ans=[list(x) for x in st]
        return ans                    