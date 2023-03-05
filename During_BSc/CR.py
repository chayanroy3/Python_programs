#Charging and Discharging of a CR circuit
import matplotlib.pyplot as pt
q=eval(input('enter the value of initial charge'))
v=eval(input('enter the value of voltage'))
R=eval(input('enter the value of Resistance'))
C=eval(input('enter the value of Capacitance'))
h=eval(input('enter the value of step size'))
t=eval(input('enter the value of initial time'))
T=eval(input('enter the value of final time'))
Qa,ta=[],[]
while t<T:
    Qa.append(q)
    ta.append(t)
    q=q+((v/R)-(q/(C*R)))*h
    t=t+h
print('final charge =',q)
pt.figure()
pt.plot(ta,Qa,'c')
pt.xlabel('time')
pt.ylabel('charge')
pt.title('charge vs time of CR circuit')
pt.show()
