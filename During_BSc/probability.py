#probability
import random
n=int(input('enter the total number of trials'))
s=0
t=0
u=0
r=int(input('enter the favourable events,r='))
p=int(input('enter the favourable events,p='))
for i in range (0,n):
    x=random.randint(1,6)
    if x==r:
        s=s+1
    if x==p:
        t=t+1
    if x==r or x==p:
        u=u+1
a=s/n
b=t/n
c=u/n
print('probability of r only=',a)
print('probability of p only=',b)
print('probability of r & p together=',c)

