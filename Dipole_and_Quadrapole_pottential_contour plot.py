import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
q, eps0 = 1.602e-19, 8.854e-12
d = 10
k= 1/4/np.pi/eps0 * q * d
def v(x,y):

     v=k*x/(np.sqrt(x**2+y**2)**3)
     return v
     
x=np.linspace(-10,10,1000)
y=np.linspace(-10,10,1000)
z=np.linspace(-10,10,1000)
X,Y= np.meshgrid(x,y)

V=v(X,Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax = fig.add_subplot(111)
L = np.linspace(V.min()*0.0001,V.max()*0.0001,100)

ax.contour(X,Y,V,levels=L,colors='black')
plt.show()






                     
