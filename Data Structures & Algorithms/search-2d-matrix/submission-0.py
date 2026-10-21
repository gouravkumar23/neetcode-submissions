class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binS(arr, tar, lo, hi):
            while(lo<=hi):
                mid= lo+(hi-lo)//2
                n= arr[mid]
                if(n== tar):
                    return True
                elif(n< tar):
                    lo= mid+ 1
                else:
                    hi= mid-1
            return False
        m= len(matrix[0])- 1
        for i in matrix:
            if(binS(i, target, 0, m)):
                return True
        return False