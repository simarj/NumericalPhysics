#Write a code to compute eigenvalues of a given square matrix of order n 
import numpy as np
n=int(input('Enter order of Square Matrix'))
L=[]
for i in range(0,n):
    l=eval(input('Enter row n'+str(i+1)))
    L.append(l)
M=np.array(L)
b=M[0][0]+M[1][1]
C=-(M[0][1]*M[1][0])+(M[0][1]*M[1][0])
k=-4*(C)
D=(b**2)+k
if D==0:
    lam=b/2
    print('Eigenvalue of',M,'is',lam)
elif D>0:
    lam1=(b+D**(1/2))/2
    lam2=(b-D**(1/2))/2
    lam=(lam1,lam2)
    print('Eigenvalues of',M,'are',lam)
else:
    lam1=(b+((-D)**(1/2).j))/2
    lam2=(b-((-D)**(1/2).j))/2
    print('Eigenvalues of Matrix',M,'are',lam1,lam2)
    
