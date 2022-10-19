import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.special import  jv
def gamma(x):
    if type(x) is int:
        I=x if x==1 else x-1
        for i in range(1,x-1):
            I=I*i
    elif (2*x)%2==1:
        I=np.sqrt(np.pi)
        i=1
        while(x-i)>=0.5:
            I*=(x-i)
            i=i+1
    return I
def J(n,x):
    S=0
    for i in range(0,50):
        S+=(-1)**i*(x/2)**(n+2*i)/(gamma(i+1)*(gamma(n+i+1)))
    return S
def dJ(n,x):
    S=0
    for i in range(0,50):
       S+=(-1)**i*(x/2)**(n+2*i-1)*(n+2*i)/(2*gamma(i+1)*(gamma(n+i+1)))
    return S
print(J(0,20))
print(dJ(2.5,20))

def wr(Cn,Cv,name):
    D={Cn[i]:Cv[i] for i in range(len(Cn))}
    d=pd.DataFrame(D)
    d.to_csv(name,header=False,index=False,sep='\t')
def rd(name,Cn):
    d1=pd.read_csv(name,sep='\t',header=None,names=Cn)
    L=[]
    for i in range(0,len(Cn)):
        t=[]
        for j in range(0,len(d1)):
            t.append(d1.iloc[j])
        L.append(t)
    D={Cn[i]:L[i] for i in range(len(Cn))}
    return D,d1

x=np.linspace(-20,20,100)

J0=[J(0,X) for X in x]
J1_2=[J(0.5,X) for X in x]
J1=[J(1,X) for X in x]
dj=[dJ(0,X) for X in x]
Cn1=['x','J0','J1/2','J1','J\'0']
Cv1=[x,J0,J1_2,J1,dj]
Jn1_2=[J(-0.5,X) for X in x] 
name1=r"C:\Users\Lenovo\Desktop\Wprime\Academic\Python_Programs\bes01.txt"
wr(Cn1,Cv1,name1)
D1,d1=rd(name1,Cn1)
print(d1)
plt.xlabel('x')
plt.ylabel('Pn(x)')
plt.grid(True)
plt.title('Bessel Function of the first kindd for various orders')
plt.xlim([-20,20])


plt.plot(x,J0,label='J0(x)')
plt.plot(x,J1_2,label='J0.5(x)')
plt.plot(x,J1,label='J1(x)')
plt.plot(x,dj,label='J\'0(x)')

plt.legend()
plt.show()
plt.xlim([0,20])
plt.grid(True)
plt.plot(x,jv(0.5,x),label='Inbuilt J0.5')
plt.plot(x,jv(-0.5,x),label='Inbuilt J-0.5')
plt.plot(x,J1_2,'-o',label='J0.5')
plt.plot(x,Jn1_2,'-o',label='J-0.5')
plt.legend()
plt.show()

df=pd.DataFrame({'x':x,'Builtin J(0.5)':jv(0.5,x),'J(0.5)':J1_2,'Builtin J(-0.5)':jv(-0.5,x),'J(-0.5)':Jn1_2})
print(df)
            

    
        
