#Differentiation
print('The function is defined as x^2+x')
x=eval(input('Enter the value of x in the function'))
h=eval(input('Enter  the step size'))
def f(x):
    f=x**2+x
    return f
#case1
d1=(f(x+h)-f(x))/h
print('The result of differentiation at x=',x,' using Forward method =',d1)
#case 2
d=(f(x+h)-f(x-h))/(2*h)
print('The result of Differentiation at x =',x,'using Central Method=',d)
#case 3
d2=(f(x)-f(x-h))/h
print('The result of Differentiation at x =',x,'using Backward Method=',d2)
