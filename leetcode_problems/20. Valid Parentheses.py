class Solution:
    def isValid(self, s: str) -> bool:
        a=[""]
        i=0
        for j in range(len(s)):
            if s[j]=="(":
                a.append(s[j])
                i=i+1
            elif s[j]=="{":
                a.append(s[j])
                i=i+1
            elif s[j]=="[":
                a.append(s[j])
                i=i+1
            elif s[j]==")" and a[i]=="(":
                a.pop(i)
                i=i-1
            elif s[j]=="]" and a[i]=="[":
                a.pop(i)
                i=i-1
            elif s[j]=="}" and a[i]=="{":
                a.pop(i)
                i=i-1
            else:
                return False
        if i==0:
            return True
        else:
            return False
        
            
