import numpy as np
'''______________________________________________________________________________________________________________'''

def smm(A,B): # Short for square Matrix Multiplier
    n=len(A)
    P=np.array([[0,0],[0,0]],complex)
    for i in range(0,n):
        for k in range(0,n):
            t=0
            for j in range(0,n):
                t+=A[i][j]*B[j][k]
            P[i][k]=t
                
    
    
            
            

    return P
#______________________________________________________________________________________________________

def square_pauli():
    while True:
        print(''' 1. s1^2
    2.s2^2
    3=s3^2
    4. For exiting to menu''')
        c=int(input('Enter your choice'))
        if c==1:
            (A,B)=(s1,s1)
            print('Product is :\t',smm(A,B))
        elif c==2:
            (A,B)=(s2,s2)
            print('Product is :\t',smm(A,B))
        elif c==3:
            (A,B)=(s3,s3)
            print('Product is :\t',smm(A,B))   
        else:
            break
#__________________________________________________________________________________________________________________________
def trace(A):
    t=0
    for i in range(0,len(A)):
        t+=A[i][i]
    return print('Trace is :\t',t)


#____________________________________________________________________________________________________________________
def trace_pauli():
    while True:
        
        print(''' 1. tr(s1)
        2.tr(s2)
        3.tr(s3)
        4. For exiting to menu''')
        c=int(input('Enter your choice'))
        if c==1:
            A=s1
            trace(A)
        elif c==2:
            A=s2
            trace(A)
        elif c==3:
            A=s3
            trace(A)
        else:
           break
#___________________________________________________________________________________________________
def levi_cevita(i,j,k):
    if (i,j,k) in [(1,2,3),(3,1,2),(2,3,1)]:
        return 1
    elif i==j or i==k or j==k: # By the way in commutator(i,j) we just require the equality between i and j 
        return 0  
    else:
        return -1
#__________________________________________________________________________
def Kronecker_delta(i,j): 
    if i==j:
        return 1.j
    else :
        return 0.j
Kd=np.array([[1,0],[0,1]])
#____________________________________________________________________
def des(n): #Short for Designator
    if n ==1:
        return s1
    elif n==2:
        return s2
    else :
        return s3
#__________________________________________________________________________________________________
    
    
def commutator(i,j):
    L=[1,2,3]
    if i!=j:
        L.remove(i)
        L.remove(j)
        k=L[0]
        com_ij=smm(des(i),des(j))-smm(des(j),des(i))
        print('commutator of i ,j =\t',com_ij)
        f=2*(1.j)*levi_cevita(i,j,k)*des(k)
        print('2*i*epsilon(i,j,k)*sk =\t',f)
        if (com_ij==f).all():
            print('si*sj-sj*si = 2*i*epsilon(i,j,k)*sk for (i,j,k)= \t',(i,j,k))
        else :
            print('The above expression in not true  for these values of (i,j,k) :\t',(i,j,k))
    else:
        L.remove(i)
        k=L[0]
        com_ij=smm(des(i),des(j))-smm(des(j),des(i))
        f=2*(1.j)*levi_cevita(i,j,k)*des(k)
        print('[s',i,'.s',j,'-s',j,'.s',i,']=\t',com_ij)
        print('2*i*epsilon(i,j,k)*sk =\t',f)
        if (com_ij==f).all():
            print('si*sj-sj*si = 2*i*epsilon(i,j,k)*sk for (i,j,k)= \t',(i,j,k))
        else :
            print('The above expression in not true  for these values of (i,j,k) :\t',(i,j,k))
        
        
    
def commutator_function():
    i=int(input('Enter Value of i'))
    j=int(input('Enter Value of j'))
    commutator(i,j)
#_________________________________________________________________________________________________________________________
        
def anti_commutator(i,j):
    Kd=np.array([[1,0],[0,1]]) #Kronecker Delta Function
    anticom_ij=smm(des(i),des(j))+smm(des(j),des(i))
    print('{s',i,'.s',j,'+s',j,'.s',i,'}=\t',anticom_ij)
    f=2*Kd
    print(f)
    if (anticom_ij==f).all():
        print('si*sj-sj*si = 2*delta(i,j) for (i,j) = \t',(i,j))
    else:
        print('The above expression in not true  for these values of (i,j) :\t',(i,j))
    
def anticommutator_function():
    i=int(input('Enter Value of i'))
    j=int(input('Enter Value of j'))
    anti_commutator(i,j)
#_______________________________________________________________________________________________________________________
        
def ladder_operators() :
    sp=0.5*(s1+ complex(0,1)*s2)
    sm=0.5*(s1- complex(0,1)*s2)
    psi1=np.array([[1],[0]])
    psi2=np.array([[0],[1]])
    def prod2x2_2x1(A,B):
        n1=len(A)
        n2=len(B)
        P=np.array([[0],[0]])
        for i in range(0,n1):
            t=0
            for k in range(0,n2):
                
                t+=A[i][k]*B[k]
            P[i]=t
        return P
                
        
        
    sm_psi1= prod2x2_2x1(sm,psi1)
    sp_psi2= prod2x2_2x1(sp,psi2)
    print('s+ =\t',sp)
    print('s_ = \t',sm)
    print('psi1 =\t',psi1)
    print('psi2 = \t',psi2)
    print('s_*ps1 = \t',sm_psi1)
    print('s+*psi2=\t',sp_psi2)
    
    
    if (sm_psi1==psi2).all():
        print('s_*psi1=psi2')
    else :
        print('s_*psi1 is not equal to psi2')
    if (sp_psi2==psi1).all():
        print('s+*psi2=psi1')
    else :
        print('s+*psi2 is not equal to psi1')
#_____________________________________________________________________________________________________________
def main():
    print( 'Pauli matrices are as follows : \n','sx= \t',s1,'\n','sy= \t',s2,'\n','sz= \t',s3)
    while True:
        print('What do you want to do ?')
        print('''1. computing square of pauli matrices
2. calculating  trace of pauli matrices
3. computing and verifying the commutator of si,sj
4. computing and verifying the anti commutator si,sj
5. Construction of ladder operators
6. For closing the programme ''')
        l=int(input('Enter your Choice :\t'))
        if l==1:
            square_pauli()
        elif l==2:
            trace_pauli()
        elif l==3:
            commutator_function()
        elif l==4:
            anticommutator_function()
        elif l==5:
            ladder_operators()
        else:
            break
            


s1=np.array([[0,1],[1,0]],complex)
s2=np.array([[0+0.j,0-1.j],[0+1.j,0+0.j]],complex)
s3=np.array([[1,0],[0,-1]],complex)
main()
       
    
            
        


    
