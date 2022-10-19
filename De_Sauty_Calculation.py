from math import sqrt
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import scipy.optimize as opt
Rv1=Rc1=[i for i in range(100,1100,100)]
Cc=2.5
Rc2=[i for i in range(100,1100,100)]
Rv2=[130,250,380,500,630,760,880,1010,1150,1260]
def table(Rc,Rv,Cc):
    tab=pd.DataFrame(columns=('Rc','Rv','Rv/Rc','Cx'))
    tab['Rc']=Rc 
    tab['Rv']=Rv 
    tab['Rv/Rc']=tab['Rv']/tab['Rc']
    tab['Cx']=tab['Rv/Rc']*Cc 
    tab.index+=1
    mn= tab['Cx'].sum()/len(tab)
    print(tab)
    print(mn)

table(Rc2,Rv2,Cc)

def linfit(X,Y):          
    D=stats.linregress(X,Y)
    a=D[0]
    b=D[1]
    print('Slope=',a)
    print('Error in Slope',D[4])
    print('Intercept',b)
    print('Error in intercept ',D.intercept_stderr)
    plt.scatter(X,Y,color='Orange')
    x=np.linspace(min(X),max(X),1000)
    y=[b+a*i for i in X]
    print('Cx from slope=',a*Cc)

    print('Error in Cx=',D[4]*Cc)
    plt.plot(X,Y)
    plt.xlabel('R1 in ohms')
    plt.ylabel('R2 in ohms')
    plt.title('Y='+str(a)+'*X+'+str(b))
    plt.grid(True)

    plt.show()
    
linfit(Rc2,Rv2)
def line(x,a,b):
    return a*x+b
p,cov=opt.curve_fit(line,Rc2,Rv2)
print(sqrt(cov[0][0]))