import matplotlib.pyplot as plt
import math
import numpy
def fac(n):
    if n>0:
        f=1
        for i in range(1,n+1):
            f*=i
        return f
    elif n==0:
        return 1



def bin_prob(s,n,r):
    p=(fac(n)*(s**r)*((1-s)**(n-r)))/(fac(n-r)*fac(r))
    return p
def bin_plot(s,n):
    r=[i for i in range(0,n+1)]
    k=[bin_prob(s,n,i) for i in range(0,n+1)]
    plt.bar(r,k,color='red')
    plt.xlim([0,n+10])
    plt.xlabel('no of failures')
    plt.ylabel('probability of failures')
    plt.show()
s=eval(input('Enter Probability of failure \t'))
n=eval(input('Enter number of trials \t'))
r=eval(input('Enter number of failures \t'))
if (type(n) is int and type(r) is int) and (n >r>0 ):
    print('Probability of failure is :\t',bin_prob(s,n,r))
    
else:
    if type(n) is not int:
        print('no of trials must be integer')
    if n <0:
        print('no of trials must be a positive integer')
    if type(r) is not int:
        print('no of failures must be a integer')
    if r <0:
        print('no of trials must be a positive integer')
    if n <r:
       print('no of trials must be greater than number of failures')
bin_plot(s,n)
        
                    
        

