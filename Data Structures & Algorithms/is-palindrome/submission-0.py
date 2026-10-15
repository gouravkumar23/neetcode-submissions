class Solution:
    def isPalindrome(self, s: str) -> bool:
        def clean(s):
            tt= ""
            for i in range(len(s)-1, -1, -1):
                tt+= s[i] if s[i].isalnum() else ""
            ss= ""
            for i in range(len(s)):
                ss+= s[i] if s[i].isalnum() else ""
            return ss.lower()==tt.lower()
        return clean(s)