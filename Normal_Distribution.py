import math
import matplotlib.pyplot as plt
import numpy
def norm_prob(s,mu,x):
    if s==0:
        return 'Value of standard deviation  must not be zero'
    else:
        c=math.exp(-(1/2)*(((x-mu)/s)**2))/(((2*math.pi))**(0.5)*s)
        return c
def norm_plot(s,mu,R):
    X= numpy.arange(R[0],R[1],0.1)
    p=[norm_prob(s,mu,x) for x in X]
    plt.plot(X,p)
    plt.ylim([0,norm_plot(s,mu,0)])
    plt.show()
s=eval(input('Enter Value of Standard Deviation: \t'))
mu=eval(input('Enter Value of Mean:\t'))
def menu(s,mu):
    print('What would you not like to do ?')
    print('Enter your choice :')
    print('1. Probability of some x')
    print('2. Plot of Normal distribution in a certain range of x')
    c=int(input('What would you not like to do ? : \t'))
    if c==1:
        R=eval(input('Enter range of x (xa,xb):\t'))
        norm_plot(s,mu,R)
    elif c==2:
        x=eval(input('Enter value of x '))
        print(norm_prob(s,mu,x))
menu(s,mu)
    
        
    
