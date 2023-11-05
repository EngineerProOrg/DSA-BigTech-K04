class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        min_len = min([len(s) for s in strs])
        
        for ind in range(min_len):
            compared_ch = strs[0][ind]
            for s in strs:
                if compared_ch != s[ind]:
                    return strs[0][:ind]

        return strs[0][:min_len]
