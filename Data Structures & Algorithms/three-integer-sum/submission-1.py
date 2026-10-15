class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans= []
        nums.sort()
        #t1, t2= 1, len(nums)-1
        for i in range(len(nums)-2):
            if i>0 and nums[i]== nums[i-1]:
                continue
            t1, t2= i+1, len(nums)-1
            #print(t1, t2)
            tar= -nums[i]
            while(t1<t2):
                #print(tar,nums, nums[t1], nums[t2])
                if(nums[t1]+nums[t2]== tar):
                    tt= [nums[i], nums[t1], nums[t2]]
                    if tt not in ans:
                        ans.append(tt)
                    t1+= 1
                    t2-=1
                elif(nums[t1]+nums[t2]<tar):
                    t1+= 1
                    #print("increasing", t1-1, "to", t1)
                else:
                    t2-= 1
                    #print("decreasing", t2+1, "to", t2)
        return ans