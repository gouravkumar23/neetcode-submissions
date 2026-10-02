class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans= []
        dd= {}
        for i in strs:
            si= tuple(sorted(i))
            if(si in dd):
                dd[si].append(i)
            else:
                dd[si]= [i]
        for i in dd:
            ans.append(dd[i])

        return ans