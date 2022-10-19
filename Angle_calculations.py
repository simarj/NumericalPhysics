import math

T=[(119,32,0),(120,31,30),(121,18,30),(119,40,30),(115,37,0),(120,31,30),(121,0,30),(119,19,0),(121,33,0),(121,2,30),(119,32,30),(121,35,0)]
#T=[(120,33,0),(120,25,30),(120,41,30),(120,23,30),(121,0,30),(121,29,0),(119,32,0),(119,31,30),(120,23,0),(120,31,30),(121,27,0),(121,2,30)]
print(len(T))
Dev=[(48,48,30),(49,39,30),(48,34,30),(48,13,30),(48,50,0),(49,1,0),(48,49,0),(49,4,30),(48,36,30),(47,58,30),(49,0,30),(48,7,30)]
#Dev=[(49,8,30),(49,11,0),(49,4,30),(49,4,30),(49,25,30),(49,23,30),(48,13,30),(48,14,30),(49,20,0),(49,19,30),(49,14,0),(49,15,30)]

print(len(Dev))

#*******************************************
def decidata(T):
    D=[]
    for i in range(0,len(T)):
        D.append(T[i][0]+T[i][1]/60 + T[i][2]/3600)
    return D

def mean(L):
    (Sd,Sm,Ss)=(0,0,0)
    for i in range(0,len(L)):
        Sd+=L[i][0]
        Sm+=L[i][1]
        Ss+=L[i][2]
    return (Sd,Sm,Ss)
    
#2A_mean=(120, 35, 2.5),sd=(1.2942147634549137),sem=(0,22,24.9)=0.37360762103494116
#A_mean=(60,17,31.25),sem=(0,11,12.49)=0.18680381051747058
A_DECI=(60,17,31.25)
eA_DECI=(0,22,24.9)
def error_calculation(D,m):
    
    print(D)
    print(m)
    '''l=list()
    for i in range(0,3):
        if type(m[i]/12) is int:
            g=1
        else:
            l[i]=math.floor(m[i]/12)'''
            
    
    M=m[0]/12+m[1]/(60*12)+m[2]/(3600*12)
    print(M)
    e=[(i-M)**2 for i in D]
    sd=sum(e)/((len(e)-1)**0.5)
    print(sd)
    sem=sd/((len(D))**0.5)
    print((sem))
    print(sem/2)
print('Angle of prism calculations')    
    
error_calculation(decidata(T),mean(T))

print('\n')
print('Angle of  Minimum Deviation calculation')
error_calculation(decidata(Dev),mean(Dev))
def rad(T):
    ad=(T[0])+(T[1]/60)+(T[2]/3600)
    ar=ad*math.pi/180
    return ar

    
# Min_Dev_Average=(49,4,32.5), sd=(0,33,21.4),sem=(0,9,37.7)
print('***************************')

'''A_DECI=(120, 35, 2.5)
eA_DECI=(0,22,24.9)'''
A_DECI=(60,17,31.25)
eA_DECI=(0,11,12.49)
D_DECI=(49,4,32.5)

eD_DECI=(0,9,37.7)
A=rad(A_DECI)
eA=rad(eA_DECI)
D=rad(D_DECI)
eD=rad(eD_DECI)
print(A,eA,D,eD)
print('****************************')
def Refractive_index(A,D,eA=0,eD=0):
    a=A
    R=math.sin((a+D)/2)/math.sin(a/2)
    dR_D=0.5*(math.cos((a+D)/2))*eD/math.sin(a/2)
    dR_A=0.5*eA*(1/(math.sin(a/2)**2))*math.sin(D/2)
    print((dR_D,dR_A))
    eR=((dR_D)**2+(dR_A)**2)**0.5
    print((R,eR))

    
Refractive_index(60.051*math.pi/180,48.727*math.pi/180,0.236*math.pi/180,0.20842323791938705*math.pi/180)    
def Cauchy(ln):
    