import numpy as np
import matplotlib.pyplot as m
from tabulate import tabulate
x1=np.array([250,500,750,1000,1250,1500,1750,2000,2250,2500,2750])
x=x1+250
y1=np.array([11.13,12.11,13.46,15.97,17.03,20.10,20.87,22.62,23.35,24.04,25.84])
y2=np.array([10.37,11.56,13.17,16.14,17.57,19.98,21.15,20.38,23.14,24.29,25.84])
y3=(y1+y2)/80
y=(y32)
l=[]
n=np.mean(x*y)-(np.mean(x)*np.mean(y))
d=np.mean(x2)-(np.mean(x)**2)
b=n/d                                       #Slope
a=(np.mean(y)-b*(np.mean(x)))      #Intercept
yp=[]
ei=[]
eis=[]
o=0
for i in range(len(x)):
    p=[x[i],y1[i],y2[i],round(y3[i],2),round(y[i],4)]
    l.append(p)
    yip=a+(bx[i])
    np.append(yp,[yip])
    e=y[i]-yip
    es=e2
    np.append(ei,e)
    np.append(eis,es)
    o+=es
uy=(o/(len(y)-2))
ub=(uy(1/2))/(len(y)*d)
ua=((uy*(1/2))np.mean(x**2))/(len(y)d)
head=['Mass(g)','Time(10 osc inc)(s)','Time(10 osc dec)(s)','Time Period(s)','T^2(s^2)']
print(tabulate(l,headers=head, tablefmt='grid'))
print('Slope=',b)
print('Intercept=',a)
print('Uncertainty in slope=',ub)
print('Uncertainty in intercept=',ua)
l1=[]
l2=[]
for i in range(0,len(x),len(x)-1):
    h=a+b*(x[i])
    l1.append(h)
    l2.append(x[i])
m.xlabel("Mass(g)")
m.ylabel("T^2(s^2)")
m.scatter(x,y,c='black')
m.plot(l2,l1,c='red')
