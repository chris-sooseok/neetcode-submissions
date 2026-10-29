class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = {}
        ans = []

        for i, s in enumerate(strs):
            ss = "".join(sorted(s))
            if seen.get(ss, -1) == -1:
                ans.append([s])
                seen[ss] = len(ans) - 1
            else:
                ans[seen[ss]].append(s)

        return ans