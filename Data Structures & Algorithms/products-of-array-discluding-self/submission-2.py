class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l1= []
        l2= []
        tl, th= 1, 1
        for i in range(len(nums)):
            tl*= nums[i]
            th*= nums[-(i+1)]

            l1.append(tl)
            l2.append(th)
        l2= l2[::-1]
        ans= []
        #print(l1,"l2:", l2)
        for i in range(len(nums)):
            if(i==0):
                ans.append(l2[1])
            elif(i==len(nums)-1):
                ans.append(l1[-2])
            else:
                ans.append(l1[i-1]*l2[i+1])
        return ans