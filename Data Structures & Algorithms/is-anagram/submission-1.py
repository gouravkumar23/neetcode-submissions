from typing import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1= Counter(s)
        d2= Counter(t)
        for i in d1:
            if(i in d2 and d1[i]==d2[i]):
                continue
            return False
        for i in d2:
            if(i in d1 and d2[i]==d1[i]):
                continue
            return False

        return True