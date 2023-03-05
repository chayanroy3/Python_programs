#projectile motion
import matplotlib.pyplot as pt
import math
v=eval(input('enter the value of velocity'))
o=eval(input('enter the angle with xaxis'))
vy=v*math.sin(math.pi*o/180)
vx=v*math.cos(math.pi*o/180)
x=eval(input('enter the value of initial position of x axis'))
y=eval(input('enter the value of initial position of y axis'))
t=eval(input('enter the value of initial time'))
h=eval(input('enter the value of step size'))
g=eval(input('enter the value of gravitational constant'))
T=eval(input('enter the value of final time'))
H=0
xa,ya=[],[]
while t<T:
    xa.append(x)
    ya.append(y)
    vy=vy-g*h
    y=y+vy*h
    x=x+vx*h
    t=t+h
    if y>H:
        H=y
    if y<0:
        print ('x range=',x)
        print ('time of flight',t)
        break
print ('max height =',H)
pt.figure()
pt.plot(xa,ya,'r')
pt.xlabel('time')
pt.ylabel('height')
pt.title('Projectile motion')
pt.show()
