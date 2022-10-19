import matplotlib.pyplot as plt;import numpy as np;import math;import pandas as  pd 
def l(x,X,Y):
    C=[]
    
    for i in range(0,len(X)):
        p=1
        for k in range(0,len(X)):
            if k==i:
                continue	
            p=p*(x-X[k])/(X[i]-X[k])
        C.append(p)
    LP=sum([C[i]*Y[i] for i in range(0,len(Y))])    
    return LP
def M(l):
    L=[]
    for i in range(1,len(l)-1):
    	if l[i]>=l[i+1] and l[i]>l[i-1]:
    		L.append(l[i])
    	elif l[i]<=l[i+1] and l[i]<=l[i-1]:
    		L.append(l[i])
    return L

def lag(x,XL,YL,c=0,sp=0): # c=0 implies lagrange interpolation of Y wrt X and c=1 implies Inverse lagrange interpolation 
    if sp==0 and c==0:
    	print('Lagrange Interpolation')
    elif sp==0 and c==1:
    	print('Inverse Lagrange Interpolation')
    if c==0:
       A=[]
       B=[]
       for i in range(len(XL)):
       	if   XL.count(XL[i])>1:
       		A.append(XL[i])
       		B.append(YL[i])
       [XL.remove(i) for i in A]
       [YL.remove(i) for i in B]
       a=(XL[0]if x>=XL[0] else x ) if sp==0 else (XL[0] if XL[-1]>=XL[0] else XL[-1])
       b=(XL[-1] if x<=XL[-1] else x ) if sp==0 else (XL[-1] if XL[-1]>=XL[0] else XL[-0])
       X=np.linspace(a,b,20)
       Y=l(X,XL,YL)
       plt.title('Lagrange Interpolation');plt.xlabel('x');plt.ylabel('y');plt.plot(XL,YL,'-*',color='black',label='Data Points') 
       plt.plot(X,Y,color='red',label='Lagrange Interpolation Polynomial')
       if sp==0 or XL[0]<=x<=XL[-1]:
       	y=l(x,XL,YL) 
       	print('F('+str(x)+') =\t',y)
       	plt.plot(x,y,'o',color='orange',label='x') 
       if sp==0:
       	plt.grid(True);plt.legend();plt.show()
    else :   # if c is 1 and maximas and minimas exist then 
       A=[]
       B=[]
       for i in range(len(XL)):
       	if   YL.count(YL[i])>1:
       		A.append(XL[i])
       		B.append(YL[i])
    	 
       [XL.remove(i) for i in A]
       [YL.remove(i) for i in B]
       count=0
       co=-1 
       d=1
       c1=0
       y=x
       L=M(YL)
       L.insert(0,YL[0])
       L.append(YL[-1])
       for i in L:
        if L.index(i)==len(L)-1:
         break
        a1=YL.index(i,c1)
        a2=YL.index(L[L.index(i)+1],c1) if len(L)-1>=L.index(i)+1 else YL.index(L[L.index(i)],c1)
        U=YL[a1:a2+1] if a1<=a2 else YL[a2:a1+1]
        T=XL[a1:a2+1] if a1<=a2 else XL[a2:a1+1]
        ind=[a1,a2]
        ind.sort()
        c1=ind[1] 
        if co>0:
         U.reverse()
         T.reverse()
        co*=-1
        #a=(U[0]if y>=U[0] else y) if U[-1]>=U[0] else (U[-1]if y>=U[-1] else y) 
        #b=(U[-1] if y<=U[-1] else y)if U[-1]>=U[0] else (U[0] if y<=U[0] else y)
        #U=[U=YL[YL.index(L[i]):YL.index(L[i+1])+1]]
        a=U[0] if U[-1]>=U[0] else U[-1]
        b=U[-1] if U[-1]>=U[0] else U[-0]
        Y=np.linspace(a,b,20) 
        X=l(Y,U,T)	
        if U[0]<=y<=U[-1] or U[-1]<=y<=U[0]:
           x=l(y,U,T)
           plt.plot(y,x,'-o',color='orange',label='(y,x'+str(d)+')')
           print('Inv(f('+str(y)+')) = ',x)
           d+=1	
       	#print(i,U,T,sep='\n')
       	#print('*',X,Y,sep='\n')
       	if count==0:
       	   plt.title('Inverse Lagrange Interpolation');plt.xlabel('y');plt.ylabel('x');plt.plot(U,T,'-*',color='black',label='Data Points') 
       	   plt.plot(Y,X,color='red',label='Inverse Lagrange Interpolation Polynomial');plt.grid(True)
       	   count+=1
        else:
           plt.title('Inverse Lagrange Interpolation');plt.xlabel('y');plt.ylabel('x');plt.plot(U,T,'-*',color='black') 
       	   plt.plot(Y,X,color='red')
       if sp==0:
       		plt.legend();plt.grid(True);plt.show()
def nspline(x,XL,YL,c,n):
	print('Using Spline')
	if len(XL)%n==0:
		for i in range(0,len(XL)-n,n-1):
			X=XL[i:i+n]
			Y=YL[i:i+n]
			lag(x,X,Y,c,1)
		plt.grid(True)
		plt.title('Spline of order'+str(n-1))
		plt.show()
	
	
	else:
		for i in range(0,len(XL)-n,n-1):
			X=XL[i:i+n]
			Y=YL[i:i+n]
			lag(x,X,Y,c,1)
		
		X=XL[i+n-1:i+n+len(XL)%n]
		Y=YL[i+n-1:i+n+len(XL)%n]
		lag(x,X,Y,c,1)
		plt.title('Spline of order'+str(n-1))
		plt.grid(True)
		plt.show()	


		

    
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
def LPC(x,X,Y): #lagrange_polynomial_coefficent
    M_x=[[X[i]**k for k in range(0,len(X))]for i in range(0,len(X))]
    M_y=[[Y[i]] for i in range(0,len(Y))]
    C=lin_sys(M_x,M_y)[1]
    X=[x**n for n in range(len(X))]
    
    P=sum([X[i]*float(C[i]) for i in range(len(X))])
    return C,P
def LPCP(x,XL,YL):
    a=(XL[0]if x>=XL[0] else x ) if sp==0 else (XL[0] if XL[-1]>=XL[0] else XL[-1])
    b=(XL[-1] if x<=XL[-1] else x ) if sp==0 else (XL[-1] if XL[-1]>=XL[0] else XL[-0])
    X=np.linspace(a,b,20)
    Y=LPC(X,XL,YL)[1]
    plt.plot(X,Y)
    plt.scatter(XL,YL)
    plt.show()

def LC(x,X,Y):
    CO=[]
    L=[i for i in range(len(X))]
    XL=[x**i for i in L]
    for i in L:
     T=L.copy();T.remove(i)
     M=[[(X[j])**k for k in range(len(X))] for j in T]
     M.append(XL)
     M=np.array(M)
     Ci=np.linalg.det(M)*(-1)**(i+1)
     CO.append(Ci)
    else :
     M=[[X[j]**k for k in range(len(X))] for j in L]
     Cd=np.linalg.det(M)*(-1)**(len(X)+1)
    LP=[-Y[i]*CO[i]/Cd for i in range(len(Y))]
    P=sum(LP)
    return LP,P    

def Cheb(n): # n+1 is the number of points  
 R=[]
 for i in range(n):
   R.append(np.cos(((2*i+1)*np.pi)/(2*(n+1))))
  
 return R
def DC(f,np): # n is the number of points
 X=Cheb(np)
 Y=[f(i) for i in X]
 return X,Y
f=lambda x : 1/(1+x**2)
n_p=50
f1=lambda x: 512*x**10 -1280*x**8+1120*x**6-400*x**4+50*x**2-1

X1=np.linspace(-1,1,n_p)
Yf=f(X1)
X1=[i for i in  X1]
Yf=[i for i in Yf]
lag(0,X1,Yf)
#lag(0.2,X1,Y1)
X,Y=DC(f,n_p+1)
plt.plot(X,[f(x) for x in X],'-o',label='f(x)',color='blue')
plt.plot(X1,[f1(x) for x in X1],color='pink')
plt.plot(np.linspace(-1,1,100),[f(i) for i in np.linspace(-1,1,100)],color='blue')
lag(0,X,Y)
Yl=[l(x,X,Y) for x in X1]
Er=[Yf[i]-Yl[i] for i in range(len(Yf))]
df=pd.DataFrame({'x':X1,'F(x)':Yf,'Pn(X)':Yl,'Error':Er})
print(df) 









#print('Question 3b V,I graph')
I=[2.81,3.24,3.80,4.30,4.37,5.29,6.03]
V=[0.5,1.2,2.1,2.9,3.6,4.5,5.7]
#plt.scatter(V,I,color='r')
#v=2.4
#lag(2.9,[I[0],I[-1]],[V[0],V[-1]],1)
#print(LC(2.9,I,V)[1])

