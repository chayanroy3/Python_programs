#S.H.M.
import matplotlib.pyplot as pt
x=eval(input('enter the initial position='))
t=eval(input('enter the time'))
v=eval(input('enter the initial velocity'))
h=eval(input('enter the step size'))
T=eval(input('enter the final time'))
k=eval(input('enter the constant'))
m=eval(input('enter the mass'))
ta,xa,va=[],[],[]
while t<T:
    ta.append(t)
    va.append(v)
    xa.append(x)
    v=v-(k/m)*h*x
    x=x+v*h
    t=t+h
pt.figure()
pt.plot(ta,va,'r')
pt.plot(ta,xa,'c')
pt.xlabel('time')
pt.ylabel('velocity & position')
pt.title('S.H.M.')
pt.show()
