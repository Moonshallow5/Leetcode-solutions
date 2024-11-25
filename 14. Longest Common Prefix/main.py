class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for index in range(len(strs[0])):

            for s in strs[1:]:
                if(index>=len(s) or strs[0][index]!=s[index]):
                    return strs[0][:index]   
        return strs[0]
