class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        t1, t2= 0,  len(numbers)-1
        while(t1<t2):
            summ= numbers[t1]+numbers[t2]
            if(summ== target):
                return [t1+1, t2+1]
            elif(summ<target):
                t1+= 1
            else:
                t2-= 1