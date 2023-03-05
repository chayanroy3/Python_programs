#bar ploting
import matplotlib.pyplot as pt
roll=[2,3,4,5,6,7,8,9]
height=[1,2,3,4,5,6,7,8]
pt.bar(roll,height)
pt.xlabel('roll')
pt.ylabel('height')
pt.title('Bar plot')
pt.show()

