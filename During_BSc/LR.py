 #L.R
import matplotlib.pyplot as pt
i=eval(input('enter the value of initial current'))
v=eval(input('enter the value of initial voltage'))
R=eval(input('enter the value of resistance'))
L=eval(input('enter the value of inductance'))
h=eval(input('enter the value of step size'))
t=eval(input('enter the value of initial time'))
T=eval(input('enter the value of final time'))
ia,ta=[],[]
while t<T:
    ia.append(i)
    ta.append(t)
    i=i+((v-i*R)/L)*h
    t=t+h
print('final current=',i)
pt.figure()
pt.plot(ta,ia,'c')
pt.xlabel('time')
pt.ylabel('current')
pt.title('current vs time')
pt.show()

