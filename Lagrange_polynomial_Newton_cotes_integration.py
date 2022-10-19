import numpy as np
import matplotlib.pyplot as plt
import math
f=lambda t: np.sin(t)
def lin_sys(A,Y): # A is some rXc and X is a cx1 matrix and Yi is some rx1 matrix then system to solve is A|Y1,Y2,...YN] 
    r=len(A)
    c=len(A[0])
    cy=len(Y[0])
    for i in range(0,r):
        for j in range(0,c):   # this part is for the pivot row
            if i==j :
                I=i
                J=j
                pv=A[I][J]
                break
        for j in range(0,c):
            A[i][j]=A[i][j]/pv
        for j in range(0,cy):
            Y[i][j]=Y[i][j]/pv
        if (np.array_equal(A,np.identity(2))):
            break
        for k in range(-I,r-I): # this part makes the values above and  below the pivot  zero
            if k==0:
                continue
            t=A[I+k][J]
            for  j in range(0,c):
                A[I+k][j]+=-(t)*(A[I][j])
            for j in range(0,cy):
                Y[I+k][j]+=-(t)*(Y[I][j])
    return np.matrix(A),np.matrix(Y)
'''******************************************************************************************'''                
def LPC(X,Y): #lagrange_polynomial_coefficent
    M_x=[[X[i]**k for k in range(0,len(X))]for i in range(0,len(X))]
    M_y=[[Y[i]] for i in range(0,len(Y))]
    C=lin_sys(M_x,M_y)[1]
    return C
'''******************************************************************************************'''
def NC_int(a,b,n,f):
    d=(b-a)/n
    X=[a+d*i for i in range(0,n+1)
    Y=[f(x) for x in X]
    C=LPC(X,Y)
    X1=np.linspace(a,b,100)
    Y1=[f(x) for x in X1]
    plt.plot(X1,Y1,color='green')
    #print(C)
    I= sum([(C[i]*((b)**(i+1)-a**(i+1)))/(i+1) for i in range(0,n+1)])
    print('Integral=\t',float(I))
    #print(d*(sum([Y[i] for  i in range(1,n)])+(Y[0]+Y[n])/2))
    plt.plot(X,Y,color='black')
    #plt.scatter(X,Y,color='red',marker='x')
    for i in range(0,n+1):
        plt.vlines(x =a+i*d, ymin=0,ymax=f(a+i*d),color = 'red')
    P=[sum([float(C[i])*x**i for i in range(0,n)]) for x in X]
    #plt.ylim(min(Y1),max(Y1)) 
    plt.plot(X,P,color='pink')
    plt.show()
#NC_int(0,np.pi,10,f)
'''******************************************************************************************'''
def Trapz(a,b,n,ni):
    d=(b-a)/n                             
    X=[a+d*i for i in range(0,n+1)]
    #print(len(X))
    Y=[f(x) for x in X]
    Xp=[X[i:i+ni+1] for i in range(0,(n-ni)+1)]
    Yp=[Y[i:i+ni+1] for i in range(0,(n-ni)+1)]
    I=0
    fig,ax=plt.subplots(2)
    ax[0].plot(X,Y,color='black')
    for i in range(0,n-ni+1):
        if i%ni!=0:
            ax[1].vlines([Xp[i][0],Xp[i][-1]],ymin=[0,0],ymax=[Yp[i][0],Yp[i][-1]],color='yellow')
            continue
        C=LPC(Xp[i],Yp[i])
        a1=Xp[i][0]              
        b1=Xp[i][-1]
        #print(Xp[i],Yp[i])
        #print(C)
        X1=np.linspace(a1,b1,100)
        P=[sum([float(C[i])*x**i for i in range(0,ni+1)]) for x in X1]
        ax[1].plot(X1,P)
        #ax[0].vlines(Xp[i],ymin=[0,0],ymax=Yp[i],color='green')
        #ax[0].fill_between(Xp[i],Yp[i])
        ax[1].vlines([Xp[i][0],Xp[i][-1]],ymin=[0,0],ymax=[Yp[i][0],Yp[i][-1]],color='black')
        ax[1].fill_between([Xp[i][0],Xp[i][-1]],[Yp[i][0],Yp[i][-1]])
        I+=sum([(float(C[j])/(j+1))*(b1**(j+1)-a1**(j+1)) for j in range(0,ni+1)])
    print(I)
    plt.show()
#Trapz(0,np.pi,10,2)
'''******************************************************************************************'''
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
X=[]
Y=[]
x=1.5
print(lagrange_intp(x,X,Y)[0])
l=np.linspace(0.1,2*max(X),100)
plt.plot(l,np.log(l),label='ln(x)')
X,Y=lagrange_intp(l,X,Y)[1],lagrange_intp(l,X,Y)[2]
L=[lagrange_intp(s,X,Y)[0] for s in l]
plt.plot(l,L,label='Pn(x)')
plt.scatter(X,Y)
plt.plot(x,lagrange_intp(x,X,Y)[0],"*",color='red')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
#Trapz(0,1001*np.pi,100,2)                  
    


    

    
    
