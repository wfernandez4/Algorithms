def recmult(x,y):
    # If the max length of either of the two string is odd, this will divide x and y appropriately.
    n = max(len(str(x)), len(str(y)))
    if n%2 != 0:
        n-=1
    if n < 2: # base case
        return x*y
    else: # recursive segment
        a = int(x/(10**(n/2)))
        b = int(x%(10**(n/2)))
        c = int(y/(10**(n/2)))
        d = int(y%(10**(n/2)))
        return int((10**n)*(recmult(a,c)) + (10**(n/2))*(recmult(a,d)+recmult(b,c))+recmult(b,d))
        
print(recmult(34443, 333))