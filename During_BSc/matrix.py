#matrix
r=int(input('enter the no of rows'))
c=int(input('enter the no of column'))
a=[]
b=0
for i in range(r):
    a1=[]
    b=b+1
    d=0
    for i in range(c):
        d=d+1
        print('enter the value of row',b,'col',d)
        a1.append(eval(input()))
    a.append(a1)
print('matrix',a)
