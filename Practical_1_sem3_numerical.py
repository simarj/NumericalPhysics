#Importings and definings
import matplotlib.pyplot as plt
import matplotlib.axes as axes
import numpy as np
import pandas as pd
import math
I_t=[]
err_t=[]
err_s=[]
I_s=[]
H=[]

#Function Defining
def List(a,b,n_in,f):
    X=np.linspace(a,b,n_in+1)
    Y=[f(x) for x in X]
    return X,Y
def trapz(X,Y):
    n_p=len(X)
    h=(X[-1]-X[0])/(n_p-1)
    I=h*0.5*(Y[0]+Y[-1]+2*sum([Y[i] for i in range(1,n_p-1)]))
    err=np.absolute(I_an-I)
    return I,err
def simp(X,Y):
    n_p=len(X) # this  must be an odd number
    n_i=n_p-1
    h=(X[-1]-X[0])/(n_i)
    I=(h/3)*(Y[0]+Y[-1]+4*sum([Y[2*i-1] for i in range(1,n_i//2+1)])+2*sum([Y[2*i] for i in range(1,n_i//2)]))                         
    err=np.absolute(I_an-I)
    return I,err,h
def One(f,a,b,n_i):
    X,Y=List(a,b,n_i,f)
    return trapz(X,Y), simp(X,Y)     #One function to get all
a,b=(0.1,1000)         # defining Interval
f,I_an_x =lambda x : np.exp(-x)*np.log(x) ,lambda x: -np.cos(x) # Defining Function and its Integral from analytic formula
m=0.5
#I_an= I_an_x(b)-I_an_x(a)   
I_an=0.577215664901533    #Definite Integral From analytical formula
N_i=501        #Number of Intervals must be odd(for simpson to work)
for i in range(1,2*N_i): #Program for comparing simpson and trapezoid with step-size with logplot of [h,I(h)] start
    if i%2 !=0:  #i or ni must be even so that n_p is odd on which simpson is based
       continue
    H.append((b-a)/(i+1))
    A=One(f,a,b,i)
    I_t.append(A[0][0])
    err_t.append(A[0][1])    
    I_s.append(A[1][0])
    err_s.append(A[1][1])
df=pd.DataFrame({'Interval Width':H,'Trapzoid':I_t,'Err_Trap':err_t,'Simpsons':I_s,'Err_Simp':err_s})
print(df)
plt.title('I(h) vs h for Function in the interval'+str((a,b)))
plt.xlabel('h')
plt.ylabel('I(h)')
plt.grid(True)
plt.plot(H,I_t,'-o',label='Trapezoid')
plt.plot(H,I_s,'-*',label='Simpson')
plt.plot(H,[I_an]*len(H),color='black',label='Analytic Value of Integral')
plt.legend()
plt.xscale('log')
plt.gca().invert_xaxis()
plt.show()  #Program for comparing simpson and trapezoid with step-size with logplot of [h,I(h)] ends
#Integral From Given List of Data
#V=[0,0.5,2,4.05,8.0,12.5,18,24.5,32,40.5,50]
#I=[0+i*0.1 for i in range(0,len(V))]
#print('Power(in mW)is:','Integral From Trapezoid='+str(trapz(I,V)[0]),'Integral From Simpson='+str(simp(I,V)[0]),sep='\n')    


