#L.C.R. circuit (euler crammer method)
import matplotlib.pyplot as pt
i=eval(input('enter the initial current'))
v=eval(input('enter the voltage'))
R=eval(input('enter the resistance'))
L=eval(input('enter the inductance'))
C=eval(input('enter the capacitance'))
q=eval(input('enter the initial charge'))
h=eval(input('enter the step size'))
T=eval(input('enter the final time'))
t=eval(input('enter the initial time'))
ta,qa,ia=[],[],[]
while t<T:
    ta.append(t)
    ia.append(i)
    qa.append(q)
    i=i+(v/L)*h-(((R*i)/L)+(q/(L*C)))*h
    q=q+i*h
    t=t+h
pt.figure()
pt.plot(ta,qa,'r')
#pt.plot(ta,ia,'c')
pt.xlabel('time')
pt.ylabel('charge(q) or current(c)')
pt.title('L.C.R.')
pt.show()
