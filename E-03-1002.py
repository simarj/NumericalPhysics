import numpy as np;import matplotlib.pyplot as plt;import pandas as pd;from scipy.special import  jv;from scipy.special import jn_zeros as z
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
    for i in range(0,80):
       if x==0 and n+2*i<0:
        S=float('inf')
       elif x<0 and type(n) is not int :
        S+=complex(0,pow(-1,i)*(pow(x/2,n+2*i).imag)/(gamma(i+1)*(gamma(n+i+1))))
       else:
       	S+=complex(pow(-1,i)*(pow(x/2,n+2*i))/(gamma(i+1)*(gamma(n+i+1))),0)      
    return S
def dJ(n,x):
    S=0
    for i in range(0,50):
       if x==0 and n+2*i-1<0:
       	continue
       elif x<0 and type(n) is not int :
        S+=complex(0,pow(-1,i)*(n+2*i)*(pow(x/2,n+2*i-1).imag)/(2*gamma(i+1)*(gamma(n+i+1))))
       else:
        S+=complex(pow(-1,i)*(n+2*i)*(pow(x/2,n+2*i-1))/(2*gamma(i+1)*(gamma(n+i+1))),0) #*pow(x/2,n+2*i-1).real
    return S
def real(L):
    return [x.real for x in L]
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
x1=np.linspace(-20,20,100);x=[float(X) for X in x1]
J0=[J(0,X) for X in x];J1_2=[J(0.5,X) for X in x] ;J1=[J(1,X) for X in x];dj=[dJ(0.5,X) for X in x] ;Jn1_2=[J(-0.5,X) for X in x] 
Cn1=['x','J0','J1/2','J1','J\'0']
Cv1=[x,J0,J1_2,J1,dj]
name1="bes01.txt"
wr(Cn1,Cv1,name1)
D1,d1=rd(name1,Cn1)
print(d1)
df=pd.DataFrame({'x':x,'Builtin J(0.5)':jv(0.5,x),'J(0.5)':J1_2,'Builtin J(-0.5)':jv(-0.5,x),'J(-0.5)':Jn1_2})
print(df)
plt.xlabel('x')
plt.ylabel('Jn(x)')
plt.grid(True)
plt.title('Bessel Function of the first kind for various orders')
plt.xlim([x[0],x[-1]])
plt.plot(x,real(J0),label='J0(x)')
plt.plot(x,real(J1_2),label='J0.5(x)')
plt.plot(x,real(J1),label='J1(x)')
plt.plot(x,real(dj),label='J\'0(x)')
plt.legend()
plt.show()
plt.xlim([x[0],x[-1]])
plt.title('Comparision of Inbuilt Bessel and User Defined Bessel')
plt.xlabel('x')
plt.ylabel('Jn(x)')
plt.grid(True)
plt.plot(x,jv(0.5,x),label='Inbuilt J0.5')
plt.plot(x,jv(-0.5,x),label='Inbuilt J-0.5')
plt.plot(x,real(J1_2),'-o',label='J0.5')
plt.plot(x,real(Jn1_2),'-o',label='J-0.5')
plt.legend()
plt.show()
def orth(n,a,n_p,N):
    LHS_M=np.zeros((N,N))
    RHS_M=np.zeros((N,N))
    x1=np.linspace(0,a,n_p)
    x=[float(i) for i in x1]
    h=abs(x[0]-x[-1])/n_p
    R=z(n,N)  # This contains N roots of bessel polynomial of degree n 
    for i in range(0,N):
       for j in range(0,N):
       	Jnr1=[J(n,R[i]*X/a) for X in x]
       	Jnr2=[J(n,R[j]*X/a) for X in x]
       	LHS_M[i][j]=sum([h*x[i]*Jnr1[i].real*Jnr2[i].real for i in range(len(x))])
       	RHS_M[i][j]=0 if R[i]!=R[j] else a**2*dJ(n,R[i]).real**2/2
    print('LHS\n',LHS_M.round(5),sep='************************************************************'+'\n')
    print('RHS\n',RHS_M.round(5),sep='************************************************************'+'\n')
    print('LHS-RHS\n',(LHS_M-RHS_M).round(5),sep='************************************************************'+'\n')
n,a,n_p,N=(1,2,100,5)
orth(n,a,n_p,N) #N is the order of matrix of Orthogonality for all combination  of N roots	

def lagrange_intp(x,X,Y):
    
    C=[]

    for i in range(0,len(X)):
        p=1
        for k in range(0,len(X)):
            if k==i:
                continue
            p=p*(x-X[k])/(X[i]-X[k])
        C.append(p)
        
    
    LP=sum([C[i]*Y[i] for i in range(0,len(Y))])
    
    
    return LP,X,Y

#n=2
#X=[i
#Y=
#x=1
#l=np.linspace(0.1,2*max(X),100)
#Jn=[J(n,s) for s in l]
#plt.plot(l,Jn,label='J'+str(n)+'x)')
#print(lagrange_intp(x,X,Y)[0])
#X_,Y_=lagrange_intp(l,X,Y)[1],lagrange_intp(l,X,Y)[2]
#L=[lagrange_intp(s,X,Y)[0] for s in l]
#plt.plot(l,L,label='Pn(x)')
#plt.scatter(X_,Y_)
#plt.plot(x,lagrange_intp(x,X,Y)[0],"*",color='red')
#plt.legend()
#plt.xlabel('x')
#plt.ylabel('y')
#plt.ylim([-2,2])
#plt.show()
             
    


    

