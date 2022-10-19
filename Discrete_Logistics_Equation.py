import matplotlib.pyplot as plt
x0=5
a=5
b=0.00009
N=10


def maker(x0,a,b,N):
    X=[x0]
    for i in range(0,N):
        x=x0*(a-b*x0)
        X.append(x)
        x0=x
    return X
n=[i for i in range(0,N+1)]
X=maker(x0,a,b,N)
print(X)
plt.plot(n,X)
plt.show()
