#Radio active decay
import matplotlib.pyplot as pt
N1=eval(input('enter the no of the initial atoms'))
t=eval(input('enter the initial time'))
T=eval(input('enter the time constant'))
h=eval(input('enter the step size'))
t1=eval(input('enter the total time'))
Na,ta=[],[]
while t<t1:
    Na.append(N1)
    ta.append(t)
    N2=N1-(N1*h)/T
    N1=N2
    t=t+h
print('no of atoms after time ',t1,'sec =',N1)
pt.figure()
pt.plot(ta,Na,'r')
pt.xlabel('time')
pt.ylabel('no of atoms')
pt.title('radio active decay')
pt.show()

    
