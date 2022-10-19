def q1a():
    def der(x,i):
        k=1/3
        p=1
        for j in range(1,i+1):
            p*=1/k
            k=k-i
        return p*x**k
    def tay(x,a,n):
        f=x**(1/3)
        if n!=0:
            for i in range(1,n+1):
                f+=((x-a)**i)*der(x,i)
        return f
    n=int(input('Enter of no of order of expansion'))
    print('Taylor Expansion of x**1/3 till',n,'th order is :\t',tay(8.5,8,n))
def q2ab():
    import matplotlib.pyplot as py
    import numpy as np                   # in the answer sheet i did not import numpy as np 
    import math
    def fact(k):
        f=1
        for i in range(1,k+1):
            f*=i
        return f
    def binomial(x):
        n=100
        p=1/5
        return(fact(n)/(fact(n-x)*fact(x)))*(p**x)*((1-p)**(n-x))
    def plot1():
        X=[i for i in range(0,101)]
        P=[binomial(x) for x in X]
        py.bar(X,P,color='Red')
        py.show()
    def Nor(x):
        m=20
        v=16
        return math.exp(-((x-m)**2)/2*v)/(math.sqrt(v*2*math.pi))  # mistake
    def plot2(A): # error forgot to take A from user
        X1=[i for i in range(0,101)]
        P1=[binomial(x) for x in X1]
        py.bar(X1,P1,color='Red')
        X2=np.arange(A[0],A[1],0.01)
        P2=[Nor(x) for x in X2]
        #py.plot(X2,P2)
        #py.xtitle('x')                  # These two commands i.e py.xtitle and py.ytitle  are wrong to make the programme to work comment these two commands
        py.ytitle('Probability of x')
        py.show()
    A=[0,100]# not in the answer sheet
    plot2(A) # not in answer sheet     
    plot1()  #not in answer sheet
print('Question 1')
q1a()
print('Question 2')
q2ab()
