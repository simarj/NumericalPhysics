n = int(input('Order : \t')) 
 
h = (n-1)//2 
A = [ [ 0 for c in range(n) ] for r in range(n) ] 
 
for r in range(n): 
    for c in range(n): 
        A[ (r+c-h)%n ][ (r-c+h)%n ] = r*n+c+1 
 
for r in range(n): 
    print(' '.join( '{:4d}'.format(x) for x in A[r] ))