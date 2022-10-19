import numpy as np
#System is AX=Yi, [A|Y1]
def lin_sys(A,Y): # A is some rXc and X is a cx1 matrix and Yi is some rx1 matrix then system to solve is A|Y1,Y2,...YN] 
    r=len(A)
    b=0
    c=len(A[0])
    cy=len(Y[0])
    for i in range(0,r):
        '''for s in range(0,cy):
            if A[i]==[0]*r and  Y[i][s]==[0]:
                b=1
        if b==1:
            break'''
            
        for j in range(0,c):   # this part is for the pivot row
            if i==j :
                I=i
                J=j
                pv=A[I][J]
                break

        #if pv==0:
            #break
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
            if t==0:
                continue
            for  j in range(0,c):

                A[I+k][j]+=-(t)*(A[I][j])
            for j in range(0,cy):
                Y[I+k][j]+=-(t)*(Y[I][j])
    #if b==1:
        #return 'no solution exist'
    #else:
    return np.matrix(A),np.matrix(Y)
A=[[1,2,0,0],[-5,3,-4,1],[1,1,-3,1],[1,0,2,-1]]
Y=[[12,18],[0,4],[2,8],[1,7]]
#A=[[29,38],[23,-22]]
#Y=[[19],[10]]
C=lin_sys(A,Y)
#print(C)
print(lin_sys(A,Y)[0])
print('\n')
print(lin_sys(A,Y)[1])

        
                    
    
