class Solution:
    def isValid(self, s: str) -> bool:
        st= []
        for i in s:
            if(i=='(' or i=='{' or i=='['):
                st.append(i)
            else:
                if(len(st)<=0):
                    return False
                tt= st.pop()
                if(i==')' and tt!='(') or (i==']' and tt!='[') or (i==']' and tt!='['):
                    return False
        if(len(st)>0):
            return False
        return True
