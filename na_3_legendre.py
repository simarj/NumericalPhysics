import numpy as np ;import math;import pandas as pd;import matplotlib.pyplot as plt;from scipy.special import legendre as  Leg
def sign(x):
    return '+ ' if x >=0  else ''
def gamma(x,c=0):
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
    if c==1 :
      return I
    else:
      return  I,math.gamma(x),I-math.gamma(x)
def leg(n,x):   #Legendre Function  of the first kind(Using Recurrence Relation)
    m=n//2
    c0=gamma(2*n+1)[0]/((pow(2,n)*pow(gamma(n+1)[0],2)))   
    C=[c0]
    p=[c0*pow(x,n)]
    S=str(c0)+'x^'+str(n)
    for i in range(1,m+1):
        ci=C[i-1]*(-(n-2*(i-1))*(n-2*(i-1)-1))/(2*(i)*(2*n-2*(i-1)-1))
        xi=pow(x,n-2*i)
        C.append(ci)
        p.append(ci*xi)
        S=S+sign(ci)+str((ci))+'x^'+str(n-2*(i))
    P=sum(p)
    return S,P
def dleg(n,x):
    m=n//2
    c0=gamma(2*n+1)[0]/((pow(2,n)*pow(gamma(n+1)[0],2)))   
    C=[c0]
    p=[0]if x==0 and n==0 else [c0*n*pow(x,n-1)]
    S=str(c0*n)+'x^'+str(n-1)
    for i in range(1,m+1):
        ci=C[i-1]*(-(n-2*(i-1))*(n-2*(i-1)-1))/(2*(i)*(2*n-2*(i-1)-1))
        C.append(ci)
        dxi=n-2*i if n-2*i==0 else pow(x,n-2*i-1)*(n-2*i)
        p.append(ci*dxi)
        S=S+sign(ci)+str((ci*(n-2*i)))+'x^'+str(n-2*(i)-1) if n-2*(i)-1 >=0 else S
    P=sum(p)
    return S,P
def inleg(n,x):
    poly=Leg(n)
    polyd=poly.deriv()
    return poly(x),polyd(x)    
print('Gamma Function')
x=0.5
G=gamma(x)
print('Calulated Value of Gamma('+str(x)+')= ',G[0])
print('Value of Gamma('+str(x)+') from inbuilt function= ',G[1])
print('Error in Gamma('+str(x)+')= ',G[2])
n=6
x=-0.7777777777777778
O,dO=leg(n,x),dleg(n,x)
print('Legendre Function of the first kind upto order'+str(n)+'= ',O[0])
print('for x ='+str(x),',','P'+str(n)+'('+str(x)+')= ',O[1])
print('Derivative of Legendre Function of the first kind upto order'+str(n)+'= ',dO[0])
print('for x ='+str(x),',','P'+str(n)+'('+str(x)+')= ',dO[1])
print('Comparision with built in  function')
X=np.linspace(-1,1,10)
pnxib=inleg(n,X)[0]
dpnxib=inleg(n,X)[1]
pnxc=[leg(n,x)[1]for x in X]
dpnxc=[dleg(n,x)[1]for x in X]
epnx=[abs(pnxc[i]-pnxib[i]) for i in range(len(X))]
edpnx=[abs(dpnxc[i]-dpnxib[i]) for i in range(0,len(X))]
c=pd.DataFrame({'x':X,'P'+str(n)+'(x)_c':pnxc,'D(P'+str(n)+'(x)_c)':dpnxc,'P'+str(n)+'(x)':pnxib,'D(P'+str(n)+'(x))':dpnxib,'Diff_Pn(x)':epnx,'Diff_D(Pn(x))':edpnx})
print(c.round(5),'\n')
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
n_i=100
X=np.arange(-1,1,2/n_i)
lenstr = len(str(2/n_i).split(".")[1])
X=X.round(lenstr)
N0=N1=5
n1,n2,n3=2,2,3
Cn0=['x']
[Cn0.append('P'+str(i)+'(x)') for i in range(0,N0+1)]
Cv0=[X]
[Cv0.append([leg(n,x)[1] for x in X])for n in range(N0+1)]
name0='leg00.txt'
wr(Cn0,Cv0,name0)
plt.xlabel('x')
plt.ylabel('Pn(x)')
plt.title('Legendre Function of the first kind upto order'+str(N0))
plt.xlim([-1,1])
plt.ylim([-1.1,1.1])
for i in range(1,len(Cv0)):
    plt.plot(X,Cv0[i],label='P'+str(i-1)+'(x)')
plt.legend()
plt.grid(True)
plt.show()
Cn1=['x']
[Cn1.append('D(P'+str(i)+'(x))') for i in range(0,N1+1)]
Cv1=[X]
[Cv1.append([dleg(n,x)[1] for x in X])for n in range(N1+1)]
name1='leg01.txt'
wr(Cn1,Cv1,name1)
plt.xlabel('x')
plt.ylabel('D(Pn(x))')
plt.title('Derivative of Legendre Function of the first kind upto order'+str(N1))
for i in range(1,len(Cv1)):
    plt.plot(X,Cv1[i],label='D(P'+str(i-1)+'(x))')
plt.legend()
plt.grid(True)
plt.show()
d_r0,D0=rd(name0,Cn0)
d_r1,D1=rd(name1,Cn1)
l=len(D0['x'])
LHS=[n1*D0['P'+str(n1)+'(x)'][i] for i in range(l)]
RHS=[X[i]*D1['D(P'+str(n1)+'(x))'][i] - D1['D(P'+str(n1-1)+'(x))'][i] for i in range(l)]
V=[LHS[i]-RHS[i] for i in range(l)]
Cn2=['x','n','n-1','Pn(x)','P(n-1)(x)','D(Pn(x))','D(P(n-1)(x))','n*Pn(x)','x*D(Pn(x))-D(P(n1-1)(x))','LHS-RHS']
Cv2=[D0['x'],[n1]*len(D0['x']),[n1-1]*len(D0['x']),D0['P'+str(n1)+'(x)'],D0['P'+str(n1-1)+'(x)'],D1['D(P'+str(n1)+'(x))'],D1['D(P'+str(n1-1)+'(x))'],LHS,RHS,V]
name2='leg02.txt'
wr(Cn2,Cv2,name2)
LHS=[(2*n2+1)*X[i]*D0['P'+str(n2)+'(x)'][i] for i in range(l)]
RHS=[(n2+1)*D0['P'+str(n2+1)+'(x)'][i]+n2*D0['P'+str(n2-1)+'(x)'][i] for i in range(l)]
V=[LHS[i]-RHS[i] for i in range(l)]
Cn3=['x','n','n-1','n+1','Pn(x)','P(n-1)(x)','P(n+1)(x)','(2n+1)*Pn(x)','(n+1)*P(n+1)(x)+n*P(n-1)(x)','LHS-RHS']
Cv3=[D0['x'],[n2]*len(D0['x']),[n2-1]*len(D0['x']),[n2+1]*len(D0['x']),D0['P'+str(n2)+'(x)'],D0['P'+str(n2-1)+'(x)'],D0['P'+str(n2+1)+'(x)'],LHS,RHS,V]
name3='leg03.txt'
wr(Cn3,Cv3,name3)
LHS=[n3*D0['P'+str(n3)+'(x)'][i] for i in range(l)]
RHS=[(2*n3-1)*X[i]*D0['P'+str(n3-1)+'(x)'][i]-(n3-1)*D0['P'+str(n3-2)+'(x)'][i] for i in range(l)]
V=[LHS[i]-RHS[i] for i in range(l)]
Cn4=['x','n','n-1','n-2','Pn(x)','P(n-1)(x)','P(n-2)(x)','n*Pn(x)','(2n-1)*x*P(n-1)(x)-(n-1)P(n-2)(x)','LHS-RHS']
Cv4=[D0['x'],[n3]*len(D0['x']),[n3-1]*len(D0['x']),[n3-2]*len(D0['x']),D0['P'+str(n3)+'(x)'],D0['P'+str(n3-1)+'(x)'],D0['P'+str(n3-2)+'(x)'],LHS,RHS,V]
name4='leg04.txt'
wr(Cn4,Cv4,name4)
X=list(D0['x'])
s=len(Cn0)-1
I_c=np.zeros((s,s))
I_a=np.zeros((s,s))
for i in range(s):
    for j in range(s):
        Pi=list(D0['P'+str(i)+'(x)'])
        Pj=list(D0['P'+str(j)+'(x)'])
        P=[Pi[k]*Pj[k] for k in range(l)]
        
        I_a[i][j]=2/(2*i+1) if i==j else 0    
        I_c[i][j]=sum(P)*abs(X[0]-X[1]) if sum(P)*abs(X[0]-X[1])>1e-14 else 0
print('Legendre Polynomial for x from [-1,1] and n from'+str([0,N1]))
print(rd(name0,Cn0)[1],'\n')
print('Derivative of Legendre Polynomial for x[-1,1] and for'+str([0,N1]))
print(rd(name1,Cn1)[1],'\n')
print('Recursion relations verification')
print('*****************************************2c1**********************************************')
print(rd(name2,Cn2)[1].round(6),'\n')
print('*****************************************2c2**********************************************')
print(rd(name3,Cn3)[1].round(6),'\n')
print('*****************************************2c3**********************************************')      
print(rd(name4,Cn4)[1].round(6),'\n')
print('*****************************************2d***********************************************')
print('Checking Orthogonality relation')
print('')
print('Caluclated Orthogonality Matrix','\n',I_c.round(3))
print('\n')
print('Analytical Orthogonality Matrix','\n',I_a.round(3))
print('\n')
print('Error Matrix','\n',I_a-I_c.round(3))



