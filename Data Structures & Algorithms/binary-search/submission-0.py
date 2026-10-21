class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #ans= -1
        lo, hi= 0, len(nums)-1
        while(lo<=hi):
            mid= lo+ (hi-lo)//2
            #print(mid)
            if(nums[mid]== target):
                return mid
            elif(nums[mid]<target):
                lo= mid+1
            else:
                hi= mid-1
        return -1