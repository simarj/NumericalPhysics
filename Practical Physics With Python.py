import numpy as np
import csv
import matplotlib.pyplot as mp
import math as m
#w=eval(input('Enter Class Width\t'))
n=eval(input('Enter No of Bins\t'))
#R=eval(input('Enter Range in (start,end) form \t'))
D=eval(input('Enter Data List\t'))
F=eval(input('Enter List of Fields in the desired order \t'))
j=int(input('Enter Number of Readings \t'))
R=[]
for i in range(1,j+1):
    
    r=eval('Enter Data for row in a list'+str(i)+'\t')
    R.append(r)
    
def f_Counter(D,n):
    R=[min(D),max(D)]
    w= (R[1]-R[0])/n
    m=R[0]
    L=[]
    while m<R[1]:
        t=str(m)+'-'+str(m+w)
        L.append(t)
        m=m+w
        for d in D:
            
        
        
    
