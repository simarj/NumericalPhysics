import math
import numpy as np
import matplotlib.pyplot as mp

def sine_cosine():
    #cos(x)
    def cosine(x,N):
        n=0
        s=0
        while n<=N:
            t= ((-1)**n)*(x**(2*n))/math.factorial((2*n))
            s+=t
            n+=1
        return s

    #sin(x)
    def sine(x,N):
        n=0
        s=0
        while n<=N:
            t= ((-1)**n)*(x**(2*n+1))/math.factorial((2*n+1))
            s+=t
            n+=1
        return s



    #For Plot of  cosine
    x=np.arange(-4*math.pi,4*math.pi,0.01)
    print(x)
    f1,ax= mp.subplots()
    ax.plot(x,np.cos(x))

    for i in [1,2,3,5,10]:
        tcos = [cosine(X,i) for X in x]
        ax.plot(x,tcos)
 
    ax.set_ylim([-5,5])
    legend=['cos() in built']
    for i in [1,2,3,5,10]:
        legend.append('Taylor Expansion to - '+str(i-1)+'Terms')
    ax.legend(legend,loc=3)




    # For Plot of Sine
    x=np.arange(-4*math.pi,4*math.pi,0.1)
    f,ax= mp.subplots()
    ax.plot(x,np.sin(x))
    for i in [1,2,3,5,10]:
        tcos = [sine(X,i) for X in x]
        ax.plot(x,tcos)
    ax.set_ylim([-5,5])

    legend=['sin() in built']
    for i in [1,2,3,5,10]:
        legend.append('Taylor Expansion to - '+str(i-1)+'Terms')
    ax.legend(legend,loc=3)
    
    
    '''# Extra (not complete)
    for i in [1,2,3,5,10]:
        print('Error in value taylor expansion of cosine for ',str(i+1),'terms in range [-4pi,4pi]')
        for X in x:
            e= abs(np.cos(X)-cosine(X,i))
            print('error=\t',e,'for x=',X)'''
            
    mp.show()


def ln():
    #For ln(1+x)
    def t_ln(k,err): 
        if 0<k<=2:
            x=k-1
            s=0
            t=0
            c=1
            while True :
                t= ((-1)**c)*(x**c)/c
                s+=t
                if abs((math.log(x)-s)/(math.log(x))) < err :
                    break
                k=s
                c+=1
            print('Taylor Expansion of ln(1+x) with error of', err,'has',c,'terms')
            print('Value of expansion is',s)
            print('Error', abs((math.log(x)-s)/(math.log(x))))
    print('Enter the value of x  for ln(1+x) note that |x|<1\t')
    x=eval(input('Enter Value Of x :|x|<1 \t'))
    err=eval(input('Enter the tolerance value\t'))
    t_ln(1+x,err)
    # For ln(x)
    def tln(x,err):
        while True:
        
            t=0
            s=0
            c=1
            if 0<x<2:
                t=(((-1)**(n+1))*((x-1)**n)/n)
                s+=t
                if abs(s-math.log(x))<err:
                    break
            print('Taylor Expansion of ln(x) with error of', err,'has',c,'terms')
            print('Value of expansion is',s)
            print('Error', abs((math.log(x)-s)/(math.log(x))))
    print('For ln(x)')
    x=eval(input('Enter Value Of x\t'))
    err=eval(input('Enter the tolerance value\t'))
    tln(x,err)


def exp():
    #exp(-x^2)
    def exp_minus_x_sq(x,N):
        n=0
        s=0
        while n<=N:
            t= (((-1)**n)*((x)**(2*n)))/math.factorial(n)
            s+=t
            n+=1
        return s

    #exp(x)
    def exp_x(x,N):
        n=0
        s=0
        while n<=N:
            t=(x**(n))/math.factorial(n)
            s+=t
            n+=1
        return s



    #For Plot of  exp(-x^2)
    x=np.arange(-3,3,0.01)
    print(x)
    f1,ax= mp.subplots()
    ax.plot(x,np.exp(-1*(x**2)))

    for i in [1,2,3,5,10]:
        texsq = [exp_minus_x_sq(X,i) for X in x]
        ax.plot(x,texsq)
 
    ax.set_ylim([-2,2])
    legend=['exp(-(x^2))in built']
    for i in [1,2,3,5,10]:
        legend.append('Taylor Expansion to - '+str(i-1)+'Terms')
    ax.legend(legend,loc=3)




    # For Plot of exp(x)
    x=np.arange(-1,1,0.1)
    f,ax= mp.subplots()
    ax.plot(x,np.exp(x))
    for i in [1,2,3,5,10]:
        texp = [exp_x(X,i) for X in x]
        ax.plot(x,texp)
    ax.set_ylim([-10,10])

    legend=['exp(x) in built']
    for i in [1,2,3,5,10]:
        legend.append('Taylor Expansion to - '+str(i-1)+'Terms')
    ax.legend(legend,loc=3)        
    mp.show()

def tp():
    a=eval(input('Enter value of a where function is approximated enter a \t'))
    y=eval('lambda x:1/(x-3)')
    x=eval(input('Enter Value of x\t'))
    def fun(x,a,n):
        if n==0:
            return y(a)
        else:
            c=0
            s=0
            while True:
                t= ((-1*(x-a))**(c))/((a-3)**(c+1))
                s+=t
                if c==n:
                    break
                c+=1
                
            return s
    if a>0:
        c=a
    else :
        c=-a
    x=np.arange(-2*c-1,2*c+1,0.001)
    f,ax= mp.subplots()
    y_=[y(X) for X in x]
    ax.plot(x,y_)
    for i in [2,3,4]:
        tp= [fun(X,a,i) for X in x]
        ax.plot(x,tp)
    ax.set_ylim(-20,20)
    legend=['1/x-3 in built']
    for i in [2,3,4]:
        legend.append('Taylor Expansion to - '+str(i)+'Terms')
    ax.legend(legend,loc=3)
    
        
    mp.show()
        
    
    
def menu():
    while True:
        print('1. Taylor Expansions graphs of sin(x), cos(x) for n=2,3,4,5,10 ')
        print('2. Value of log(x) and log(1+x) by taylor expansion')
        print('3. Taylor Expansion graphs for exp(x) and exp(-(x^2)) for n=2,3,4,5,10')
        print('4.Taylor Expansion graphs for 1/x-3 at x=5,x=2.8 for n =2,3,4')
        print('Close programme')
        l=int(input('Enter your choice:\t'))
        if l==1:
            sine_cosine()
        if l==2:
            ln()
        if l==3:
            exp()
        if l==4:
            tp()
        if l==5:
            break
    
    
    
menu()
