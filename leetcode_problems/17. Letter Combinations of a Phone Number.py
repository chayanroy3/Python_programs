class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=None
        a={"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        for k in range(0,len(digits)):
            if res == None:
                res=a[digits[k]]
            else:
                b=[]
                for i in a[digits[k]]:
                    for j in res:
                        b.append(j+i)
                res=b
        return res
