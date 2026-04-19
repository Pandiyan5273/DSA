class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # maxi=0
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i]<=nums2[j]:
        #             maxi=max(maxi,j-i)
        # return maxi
        l=0
        r=0
        maxi=0
        while l<len(nums1) and r<len(nums2):
            if nums1[l]<=nums2[r]:
                maxi=max(maxi,r-l)
                r+=1
            else:
                l+=1
                if l>r:
                    r=l
        return maxi