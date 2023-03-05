#terminal velocity
import matplotlib.pyplot as pt
v1=eval(input('enter the velocity of the particle'))
t=eval(input('enter the initial time'))
h=eval(input('enter the step size'))
t1=eval(input('enter the final time'))
k=eval(input('enter the viscous constant'))
m=eval(input('enter the mass'))
g=eval(input('enter the gravititional constant'))
ta,va=[],[]
while t<t1:
    ta.append(t)
    va.append(v1)
    v2=v1+(g-(k/m)*v1)*h
    v1=v2
    t=t+h
pt.figure()
pt.plot(ta,va,'r')
pt.xlabel('time')
pt.ylabel('velocity')
pt.title('terminal velocity')
pt.show()
