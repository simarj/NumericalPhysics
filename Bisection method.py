def function(x,y):
    y=eval(y)
    return y(x)
#d=input('Enter Your Function')
#y='lambda x:'+d
def bisection_method(x0,x1,err):
    c=0
    if x0>x1:
        (x0,x1)=(x1,x0)
    
    while abs(x1-x0)/x0>err:
        c+=1    
        '''if function(x0,y)*function(x1,y)>0:
            print('No roots lie in the range',[x0,x1])
            break'''
        if function(x0,y)*function(x1,y)<0:
            x2=(x1+x0)/2
            if function(x0,y)*function(x2,y)>0:
                x0=x2
            elif function(x0,y)*function(x2,y)<0:
                x1=x2
    print('Root of function with the error of',err*100,'% is : \t',x2)
    print('No of iterations = \t',c)
d=input('Enter Your Function in terms of x:\t')
y='lambda x:'+d    
x0=eval(input('Enter x0:\t'))
print(function(x0,y))
x1=eval(input('Enter x1:\t'))
print(function(x1,y))
err=eval(input('Enter the error to which you want the root:\t'))
bisection_method(x0,x1,err)

        
    




