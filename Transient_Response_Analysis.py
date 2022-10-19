from matplotlib import pyplot as plt
from scipy import stats
import scipy.optimize as opt
import numpy as np
R=1e3
C=1e-6
ta=R*C
n=[0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5]

Tc=[i*ta for i in n]
Vc=[0,0.1,0.8,2.6,3,3.4,3.6,3.8,3.9,3.9,4]

Vm=4
def Char(t,vm,tc):
    return vm*(1-np.exp(-t/tc))
print('For Charging')
p,pcov=opt.curve_fit(Char,Tc,Vc)
print('(Vm,Time_constant',p)
print('Error in Vm=',(pcov[0][0])**0.5)
print('Error in Time Constant=', (pcov[1][1])**0.5)
X=np.linspace(min(Tc),max(Tc),1000)
Y=[ Char(i,p[0],p[1]) for i in X]
plt.plot(X,Y)
plt.grid(True)
plt.scatter([0,ta,2*ta,3*ta,4*ta,5*ta],[0,0.8,3,3.6,3.9,4])
plt.xlabel('t (s)')
plt.ylabel('V (volts)')
plt.show()



print('____________________________________________For Discharing______________________________________')
Td=[i*ta for i in range(0,6)]
Vd=[4,1.6,0.5,0.2,0.1,0]
def disc(t,vm,td):
    return vm*(np.exp(-t/td))
p,pcov=opt.curve_fit(disc,Td,Vd)
print('(Vm,Time_constant',p)
print('Error in Vm=',(pcov[0][0])**0.5)
print('Error in Time Constant=', (pcov[1][1])**0.5)
plt.scatter(Td,Vd)
X=np.linspace(0,max(Tc))
Y=[ disc(i,p[0],p[1]) for i in X]
plt.plot(X,Y)
plt.grid(True)
plt.xlabel('t (s)')
plt.ylabel('V (volts)')
plt.show()


