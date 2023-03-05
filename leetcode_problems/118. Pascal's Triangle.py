class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a=[]
        if numRows==1:
            return [[1]]
        else:
            for i in range(1,numRows+1):
                b=[]
                for j in range(0,i):
                    if j>0 and j<i-1:
                        c=p[j-1]+p[j]
                        b.append(c)
                    else:
                        b.append(1)
                a.append(b)
                p=b
        return a

            

                
