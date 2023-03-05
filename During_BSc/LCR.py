#L.C.R. circuit (euler method)
import matplotlib.pyplot as pt
i1=eval(input('enter the initial current'))
v=eval(input('enter the voltage'))
R=eval(input('enter the resistance'))
L=eval(input('enter the inductance'))
C=eval(input('enter the capacitance'))
q1=eval(input('enter the initial charge'))
h=eval(input('enter the step size'))
T=eval(input('enter the final time'))
t=eval(input('enter the initial time'))
ta,qa,ia=[],[],[]
while t<T:
    ta.append(t)
    ia.append(i1)
    qa.append(q1)
    i2=i1+(v/L)*h-(((R*i1)/L)+(q1/(L*C)))*h
    i2=i1
    q2=q1+i1*h
    q2=q1
    t=t+h
pt.figure()
pt.plot(ta,qa,'r')
pt.plot(ta,ia,'c')
pt.xlabel('time')
pt.ylabel('charge(q) or current(c)')
pt.title('L.C.R.')
pt.show()
