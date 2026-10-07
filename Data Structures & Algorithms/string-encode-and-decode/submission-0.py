class Solution:

    def encode(self, strs: List[str]) -> str:
        tt= ""
        for i in strs:
            tt+= f"0xmadhur{i}"
        return tt

    def decode(self, s: str) -> List[str]:
        ans= list(s.split("0xmadhur"))
        return ans[1:]