import math
import numpy
import matplotlib.pyplot as plt

def fac(n):
    if n>0:
        f=1
        for i in range(1,n+1):
            f*=i
        return f
    elif n==0:
        return 1
def poi_prob(l,x):
    c=0
    if isinstance(x,int) is True:
        if x==0:
            return 'x cannot be zero'
        elif x<0:
            return 'x cannot be negative'
        else:
            c+=1
    else:
        return 'x must be an integer'

    if l<0:
        return 'l cannot be negative'
    else:
        c+=1
    if c==2:
        return (l**x)*math.exp(-l)/fac(x)
x=eval(input('Enter value of x \t'))
l=eval(input('Enter value of lambda \t'))
print(poi_prob(l,x))
a=eval(input('Enter the range in which you want the distribution in (xa,xb) form : \t'))

def poi_plot(l,a):
    X=[i for i in range(a[0],a[1]+1)]
    p=[poi_prob(l,x) for x in X]
    plt.bar(X,p,color='red')
    plt.xlabel('no of events x')
    plt.ylabel('Probability of x events')
    plt.show()
poi_plot(l,a)

    
    
    
