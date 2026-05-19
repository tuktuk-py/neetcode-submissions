class Solution:    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        output = ""
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if strs[j][i] != strs[0][i]:
                    return output
            output += strs[0][i]
        return output