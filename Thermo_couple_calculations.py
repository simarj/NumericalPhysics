import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import pandas as pd

E=2.12
R=10010
r=21.2
L=600
lsfrs=pd.DataFrame({'E':[E],'R':[R],'r':[r],'L':[L]})
print(lsfrs)

#l=[600-26.6,600-82.9,409.8,436.3,500-77.0,500-95.6,400-27.1,400-44.3,400-92.7,219.9]
'''l=[573.4,517.1,490.2,463.7,423.0,404.4,372.9,355.57,307.3,281.1]
T1=[98.5,92.5,87.5,82.5,77.5,72.5,67.5,62.5,57.5,52.5]
T2=[0,0,0,1,1,2,2.5,3.5,4,5]
'''
l=[600-34.4,600-76.8,500-1.3,500-36.9,500-69.7,400-7.4,400-27.3,400-51.4,400-75.3,300-4.4]
T1=[98,93,88,82.5,78,72,67,63,58.5,56]
T2=[0.5,0.5,0.5,1,1,1.5,1.5,1.5,2,2]
T=[T1[i]-T2[i] for i in range(len(T1))]
Ob=pd.DataFrame({'T1(*C)':T1,'T2(*C)':T2,'T1-T2(*C)':T,'l(cm)':l})
print(Ob.to_string(index=False))
lsf=stats.linregress(T,l)
m=lsf.slope
c=lsf.intercept
em=lsf.stderr
ec=lsf.intercept_stderr
lsfrs=pd.DataFrame({'Slope':[m],'Intercept':[c],'Error in Slope':[em],'Error in Intercept':[ec]})
print(lsfrs.to_string(index=False))
tf=E*r*m/((R+r)*L)
etf=tf*em/m
print('Thermo emf produced(mV/*C)= \t',tf,etf)
Y=[t*m+c for t in T]
plt.plot(T,l,'o',label='original data')
plt.plot(T,Y,label='Best fit line')
plt.xlabel('Temprature Difference (*C)')
plt.ylabel('Balancing Length (cm)')
plt.title('T vs l')
plt.show()

