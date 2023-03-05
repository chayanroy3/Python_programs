#ploting two or more lines
import matplotlib.pyplot as pt
x1=[1,2,23,4,5]
y1=[1,5,9,6,7]
pt.plot(x1,y1,'m')
x2=[5,6,4,5,8]
y2=[5,6,9,2,5]
pt.plot(x2,y2,'c')
pt.xlabel('x axis')
pt.ylabel('y axis')
pt.title('ploting two or more lines')
pt.show()
