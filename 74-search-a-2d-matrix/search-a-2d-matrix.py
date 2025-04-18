class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarysearch(matrix,target):
            n=len(matrix)

            l,r=0,n-1
            while l<=r:
                mid=(l+r)//2
                if matrix[mid]==target:
                    return True
                elif matrix[mid]<target:
                    l+=1
                else:
                    r-=1
            return False
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            if matrix[i][0] <= target <=matrix[i][m-1]:
                return binarysearch(matrix[i],target)
        return False        



        