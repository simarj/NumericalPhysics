import mathplotlib.pyplot as mp
import numpy as np
k=8.85*10**9
def point_charge(r,q):
    e=k*q*r**(-2)
def line_charge(r,z,q,l):
    e=
def infinte_line_charge(r,q):
    e=
def plot(c,R,r):
    X=np.arrange(R[0],R[1],0.01)
    e1= point_charge(r,q)
    e2= line_charge(r,z,q,l)
    e3=infinte_line_charge(r,q)
    E1=[e1 for x in X ]
    E2=[e2 for x in X]
    E3=[e3 for x in X]
    mp.plot(X,E1)
    mp.plot(X,E2)
    mp.plot(X,E3)
    mp.legend(['For Point Charge','For Line Charge of Length'+str(l),'For an Infinite Line Charge'])
    mp.show()
    
        
