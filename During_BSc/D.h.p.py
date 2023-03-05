# Damped Harmonic motion
import matplotlib.pyplot as pt
v1=eval(input('Enter the value of initial velocity'))
x1=eval(input('Enter the value of initial position'))
t=eval(input('Enter the value of initial time'))
h=eval(input('Enter the value of step size'))
m=eval(input('Enter the value of the mass of the particle'))
k1=eval(input('Enter the value of damping constant'))
k=eval(input('Enter the value of propagation constant'))
t1=eval(input('Enter the value of final time'))
ta,xa=[],[]
va=[]
while t<t1:
    ta.append(t)
    xa.append(x1)
    va.append(v1)
    v=v1+((-k/m)*x1-(k1/m)*v1)*h
    v1=v
    x2=x1+v1*h
    x1=x2
    t=t+h
pt.figure()
pt.plot(ta,xa,'r')
pt.plot(ta,va,'g')
pt.xlabel('time')
pt.ylabel('Velocity in Green, Position in Red')
pt.title('Damped Harmonic Motion')
pt.show()
