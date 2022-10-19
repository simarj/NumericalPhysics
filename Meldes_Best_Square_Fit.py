from math import sqrt
from statistics import mean

from scipy import stats
import matplotlib.pyplot as plt
Mp=(0.741765479995351+0.8991657799591164)/2
mu=(0.0017409953197714547+0.001745903713490147)/2
#print(mu)
#print(Mp)
g=981
M=Ml=Mt=[5,7,10,12,15,17,20,25]
Msq=[i**2 for i in M]
dmu=sqrt((0.001/250)**2+(0.436/(250)**2)**2)


def Line(m,a,b):
    return m*a + b

#transverse
print('For transverse ')
f=52
Lt=[17.8216667,19.4833333,23.31,26.1633333,28.7066667,30.3733333,32.88833333,36.585]
Ltsq=[lt**2 for lt in Lt]
a,b,r_value, p_value, std_err=stats.linregress(Mt,Ltsq)


'''mu=g/(a*(f**2)*4)
Mp=b*(f**2)*4*mu/(g)
print(mu)
print(Mp)'''
print('Slope','Intercept')
print(a,b)

fa=(g/(a*mu*4))**0.5
fb=(g*Mp/(b*mu*4))**0.5

print('F(from slope)=',fa)
print('F(from intercept)=',fb)

Y2=[i*a+b for i in M]
res=[Y2[i]-Ltsq[i] for i in range(0,len(M))]
ressq=[i**2 for i in res]
print('Sum Of Residuals=',sum(res))

sysq=sum(ressq)/(len(ressq)-2)
print('Error In Y squared',sysq)
sasq=sysq/(len(ressq)*(mean(Msq)-mean(M)**2))
print('Error In Slope Squared', sasq)
print('Error In Slope',sasq**0.5)
df=sqrt((g*sasq/(16*mu*a**3))+(g*dmu**2/(16*a*mu**3)))
print('Error in Frequency by Slope',df)

plt.scatter(Mt,Ltsq)
Y=[i*a+b for i in range(0,30)]
plt.plot(range(0,30),Y)
plt.ylabel('(length of loop)^2:l^2 (cm^2))')
plt.xlabel('Mass in Pulley M (g)')
plt.title('y=(52.096041538438904)x+38.64304525761787')
plt.show()

print('_______________________________________________________________________')
#Longitudnal
print('For Longitudnal ')
f=52
Ll=[35.31,39.2766667,47.35,52.1766667,57.6666667,61.5666667,66.46,72.62]
Llsq=[ll**2 for ll in Ll]
a,b,r_value, p_value, std_err=stats.linregress(Mt,Llsq)
print('Slope','Intercept')
print(a,b)



mu=g/(a*(f**2))
Mp=b*(f**2)*mu/(g)
print(mu)
print(Mp)
fa=(g/(a*mu))**0.5
fb=(g*Mp/(b*mu))**0.5

print('F(from slope)',fa)
print('F(from intercept),',fb)

Y2=[i*a+b for i in M]
res=[Y2[i]-Llsq[i] for i in range(0,len(Ll))]
ressq=[i**2 for i in res]
print('Sum Of Residuals=',sum(res))

sysq=sum(ressq)/(len(ressq)-2)
print('Error In Y squared',sysq)
sasq=sysq/(len(ressq)*(mean(Msq)-mean(M)**2))
print('Error In Slope Squared', sasq)
print('Error In Slope',sasq**0.5)
df=sqrt((g*sasq/(16*mu*a**3))+(g*dmu**2/(16*a*mu**3)))
print('Error in Frequency by Slope',df)

plt.scatter(Mt,Llsq)
Y=[i*a+b for i in range(0,30)]
plt.plot(range(0,30),Y)
plt.ylabel('(length of loop)^2:l^2 (cm^2))')
plt.xlabel('Mass in Pulley M (g)')
plt.title('y=(207.79831968105447)x+186.84513819020913')
plt.show()




print('__________________________________________________________________________________')
print('Newton Rings')
# Newtons rings Calculation

n=[i for i in range(4,21)]
print(n)
d=[2.065,2.375,2.64,2.895,3.105,3.305,3.485,3.665,3.83,3.97,4.165,4.305,4.425,4.58,4.77,4.87,4.97]
dsq=[i**2 for i in d]
a,b,r_value, p_value, std_err=stats.linregress(n,dsq)
print('Slope','Intercept')
print(a,b)

plt.scatter(n,dsq)
Y=[ i*a+b for i in n]
plt.plot(n,Y)
plt.ylabel('Diameter D^2 (mm^2)')
plt.xlabel('n')
plt.title('y=(1.2819242034319873)x-0.7104580882390246')

#plt.show()

dh=0.00316227766
dl=1
l=22.6
h=0.16
e1=((2*l/6*h)*dl)**2
e2=(((1/2)-(l**2/(6*h**2)))*dh)**2

print(e1,e2)
dr=(e1+e2)**0.5
print(dr)
nsq=[i**2 for i in n]
R=532.121667

mn=mean(n)
print(mn)
res=[Y[i]-dsq[i] for i in range(0,len(n))]
ressq=[i**2 for i in res]
print('Sum Of residuals',sum(res))

sysq=sum(ressq)/(len(ressq)-2)
print('Print Error In Y squared',sysq)
sasq=sysq/(len(ressq)*(mean(nsq)-mean(n)**2))
print('Error in Slope Squared',sasq)
print('Error in SLope',sasq**0.5)
lam=a/(4*R)
print('Lamda (in A)',lam*10**7)
dlam=(((sasq)/((4*R)**2))+(a*dr/(4*R*R))**2)**0.5
print('Print(Error in Lamda (A)',dlam*10**7)




