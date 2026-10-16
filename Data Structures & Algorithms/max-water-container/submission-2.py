class Solution:
    def maxArea(self, heights: List[int]) -> int:
        t1, t2= 0, len(heights)-1
        mx= 0
        while (t1<t2):
            mh= min(heights[t1], heights[t2])
            area= (t2-t1)*mh
            mx= max(mx, area)
            if(heights[t1]<heights[t2]):
                t1+= 1
            else:
                t2-=1
        return mx