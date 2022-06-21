def recmult(x,y):

    # This recursive algorithm can handle largest integers of even or odd length. However, we subtract
    # 1 from from n if the largest number is odd. This is to make sure the formula is using the correct 
    # exponents.

    n = max(len(str(x)), len(str(y)))
    if n%2 != 0:
        n-=1
    if n < 2: # base case
        return x*y
    else: # recursive segment

        # Number x can be divided into first half a and second half b
        # Number y can be divided into first half c and second half d
        # x can be expressed as: (a*10^(n/2))+b
        # y can be expressed as: (c*10^(n/2))+d
        # Thus, x*y = (10^n)(ac) + (10^(n/2))(ad+bc) + bd
        # This algorithm uses four recursive calls as shown below. Karatsuba's algorithm
        # improves this by using only three recursive calls.

        a = int(x/(10**(n/2))) # first half of x
        b = int(x%(10**(n/2))) # second half of x
        c = int(y/(10**(n/2))) # first half of y
        d = int(y%(10**(n/2))) # second half of y

        return int((10**n)*(recmult(a,c)) + (10**(n/2))*(recmult(a,d)+recmult(b,c))+recmult(b,d))
        
print(recmult(123456, 123))