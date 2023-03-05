class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=strs[0]
        for i in strs:
            temp=""
            for j in range(min([len(i),len(res)])):
                if i[j]==res[j]:
                    temp=temp+i[j]
                else:
                    break
            res=temp
        return res


