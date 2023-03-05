#least error curve
x=[1,2,3,4,5,6]
y=[3,5,6,4,8,3]
n=5
sumx=0
sumx2=0
sumy=0
sumxy=0
i=0
while i<n:
    sumx=sumx+x[i]
    sumy=sumy+y[i]
    sumx2=sumx2+x[i]*x[i]
    sumxy=sumxy+x[i]*y[i]
    i=i+1
d=((sumx)**2-n*(sumx2))
a0=(sumx*sumxy-sumy*sumx2)/d
a1=(sumx*sumy-n*sumxy)/d
print ('a0=',a0)
print ('a1=',a1)
    
