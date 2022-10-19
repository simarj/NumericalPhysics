def pi(n):
    import random
    import matplotlib.pyplot as plt
    import math
    nc=0
    ns=0
    X=[]
    Y=[]
    for i in range(n**2):
        x=random.uniform(-1,1)
        y=random.uniform(-1,1)
        plt.plot(x,y,'o')
        X.append(x)
        Y.append(y)
        od=math.sqrt(x**2+y**2)
        if od<=1:
            nc+=1

        ns+=1
    pi=4*nc/ns
    plt.show()
    #plt.scatter(X,Y)
    print('Value of pi for',n,'iterations is : \t',pi)
    err= abs((pi-3.14159265359)/3.14159265359)*100
    print('Error in Value of pi is',err,'%')
n=int(input('How many Iterations do you want :\t'))
pi(n)


            
        
