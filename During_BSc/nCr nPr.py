#permutation and combination
n=int(input('enter the value of n='))
r=int(input('enter the value of r='))
def fact(x):
    s=1
    while x>0:
        s=s*x
        x=x-1
    return s
p=fact(n)/fact(r)
print('permutation nPr=',p)
c=fact(n)/(fact(r)*fact(n-r))
print('combitantion nCr=',c)
