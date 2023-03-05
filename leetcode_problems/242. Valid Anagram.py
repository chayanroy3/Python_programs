class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts={}
        dictt={}
        if len(s) ==len(t):
            for i in s:
                if i not in dicts:
                    dicts[i]=1
                else:
                    dicts[i]+=1
            for j in t:
                if j not in dictt:
                    dictt[j]=1
                else:
                    dictt[j]+=1
            if dictt==dicts:
                return True
        return False
