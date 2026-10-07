class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr= [0] * len(temperatures)
        st= [len(temperatures)-1]
        for i in range (len(temperatures)-2, -1, -1):
            if(temperatures[st[-1]]>temperatures[i]):
                arr[i]= st[-1] -i
            else:
                while(len(st)>0):
                    tt= st.pop()
                    if(len(st)>0 and temperatures[st[-1]]>temperatures[i]):
                        arr[i]= st[-1] - i
                        break
            st.append(i)
            
        return arr