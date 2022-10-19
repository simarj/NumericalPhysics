import matplotlib.pyplot as mp
import numpy as np
k=8.85*10**9
def fun():
    f=1/x**2

def plot(R):
    X=np.arrange(R[0],R[1],0.01)
    
    F=[f for x in X ]
    '''E2=[e2 for x in X]
    E3=[e3 for x in X]
    mp.plot(X,E1)
    mp.plot(X,E2)'''
    mp.plot(X,E1)
    #mp.legend(['For Point Charge','For Line Charge of Length'+str(l),'For an Infinite Line Charge'])
    mp.show()
    
