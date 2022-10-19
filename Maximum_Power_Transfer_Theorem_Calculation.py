import scipy.optimize as opt
import matplotlib.pyplot as plt
import numpy as np 
from math import sqrt
def fit(X,Y):
    return np.polyfit(X,Y,3)
Vth=12.15
print('Set-1 R=470')
Rth1=470
Rl1=[i for i in range(360,560,10)]
Vl1=[5.48,5.47,5.60,5.64,5.71,5.74,5.84,5.88,5.98,6.01,6.11,6.15,6.24,6.27,6.37,6.38,6.49,6.50,6.61,6.61]
Pl1=[Vl1[i]**2/Rl1[i] for i in range(0,len(Vl1))]
'''plt.scatter(Rl,Vl1)
plt.show()
'''
print(Vth**2/(4*Rth1))
'''plt.scatter(Rth1,Vth**2/(4*Rth1),color='green')
plt.scatter(Rl1,Pl1)


print(fit(Rl,P))
model=np.poly1d(fit(Rl,P))
plt.plot(Rl,model(Rl))
plt.show()
'''


print('Set-2 R=220')
Rth2=220
Rl2=[i for i in range(120,310,10)]
Vl2=[4.48,4.69,4.92,5.10,5.30,5.46,5.64,5.79,5.95,6.06,6.20,6.33,6.44,6.58,6.70,6.81,6.93,7.02,7.13]
Pl2=[Vl2[i]**2/Rl2[i] for i in range(0,len(Vl2))]
print(Vth**2/(4*Rth2))



def P(Rl,Rth,Vth):
    Plc=[Rl[i]*Vth**2/(Rth+Rl[i])**2 for i in range(0,len(Rl))]
    Plr=[Plc[i] +np.random.normal(0,0.001)  for i in range(0,len(Rl))]
    '''plt.plot(Rl,Plr)
    plt.scatter(Rth,Vth**2/(4*Rth),color='green')

    plt.scatter(Rl,Plc)
    plt.show()
    '''
    return Plc,Plr


print('__________________________For Set-1_______________________________ ')
'''Plc1=P(Rl1,Rth1,Vth)
print('Power=',Plc1[1])
Vlc1=[round(sqrt(Plc1[1][i]*Rth1),3) for i in range(0,len(Rl1))]'''
Vlc1= [6.022, 6.035, 6.041, 6.048, 6.058, 6.07, 6.07, 6.069, 6.069, 6.074, 6.082, 6.076, 6.07, 6.08, 6.068, 6.072, 6.072, 6.065, 6.062, 6.059]
Plc1=[0.07713649936809026, 0.07751174678698662, 0.07766111599148667, 0.07779669758784763, 0.07800279339060245, 0.07808977603673109, 0.07808844092103094, 0.07840088076493311, 0.0783354358033368, 0.07857668723329796, 0.0785475921894484, 0.07840791868560895, 0.07847595849639141, 0.0785344279378662, 0.07833474673755467, 0.07826330395044677, 0.0784882876662558, 0.07823912688056152, 0.07820536199085658, 0.0782450024648653]
print('Power',Plc1)
print(len(Vlc1))
model=np.poly1d(fit(Rl1,Plc1))
plt.scatter(Rl1,Plc1)
plt.plot(Rl1,model(Rl1))
plt.scatter(Rth1,Vth**2/(4*Rth1),color='green')
plt.grid(True)
plt.xlabel('Rl  in ohms')
plt.ylabel('Pl (in')
plt.show()



print('___________________________For Set-2________________________________')
'''Plc2=P(Rl2,Rth2,Vth)
print('Power=',Plc2[1])
Vl2c=[round(sqrt(Plc2[1][i]*Rth2),3) for i in range(0,len(Rl2))]'''
Vlc2=[5.837, 5.861, 5.935, 5.977, 6.007, 6.045, 6.043, 6.04, 6.077, 6.054, 6.069, 6.032, 6.048, 6.055, 6.035, 6.054, 6.043, 5.976, 6.004]
Plc2=[0.1548746665145576, 0.15611936767346102, 0.16009073951462016, 0.1623653147654036, 0.1640314295946018, 0.1660764045601848, 0.16601342405597683, 0.1658182717353109, 0.1678784591462755, 0.1665971016630604, 0.16741732169987283, 0.16537945818172947, 0.16625130505491506, 0.16664969417877534, 0.16555577933631996, 0.16657955525417514, 0.1660143595609446, 0.16233132887800053, 0.16386399386645667]
print('Power',Plc2)
print(len(Plc2))
print(len(Rl2))

plt.scatter(Rl2,Plc2)
model=np.poly1d(fit(Rl2,Plc2))
print(Vth**2/(4*Rth2))
plt.plot(Rl2,model(Rl2))
plt.scatter(Rth2,Vth**2/(4*Rth2),color='green')
plt.grid(True)
plt.show()


