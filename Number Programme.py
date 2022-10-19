def lam(x):
    k=x
    lam=0
    while k>=10 and lam<10:
        r=k%10
        lam=lam+r
        t=k//10
        k=t
    return lam
x=int(input('Enter an integer'))
print('lambda(',x,')=\t',lam(x))
    
    
