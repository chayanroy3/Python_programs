#interation by trapisoid method of function x^2+5x+6
print('here the function is x^2+5x+6')
def f(x):
    f=x**2+5*x+6
    return f
n=eval(input('enter the number of division,n='))
a=eval(input('enter the lower limit of integration:'))
b=eval(input('enter the upper limit of integration:'))
h=(b-a)/n
s=f(a)+f(b)
for i in range (1,n+1):
    y=a+i*h
    s=s+2*f(y)
print('the value of integration is:',s*h/2)
