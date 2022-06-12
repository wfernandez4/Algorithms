def karatsuba(x,y):

    # If the max length of either of the two string is odd, this will divide x and y appropriately.
    # This handles odd numbers that may be incorrectly divided otherwise.

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
        # This is an improvement from the recursive multiplication algorithm. Instead of four recursive
        # calls, this uses three. This is best explained by describing Karatsuba's intuitive
        # algorithm:
        # 1. a*c
        # 2. b*d
        # 3. (a+b)(c+d) (p = a+b) (q = c+d)
        # 4. z = Step 3 - step 2 - step 1 = pq - bd - ac
        # 5. Using the original algorithm:
        # x*y = (10^n)(Step 1) + (10^(n/2))(Step 4) + (Step 2)  can be rewritten as x*y = (10^n)(ac) + (10^(n/2))(z) + (bd)
        # So, we only need to recursively compute ac, pq, and bd!

        a = int(x/(10**(n/2))) # first half of x
        b = int(x%(10**(n/2))) # second half of x
        c = int(y/(10**(n/2))) # first half of y
        d = int(y%(10**(n/2))) # second half of y

        ac = karatsuba(a,c)
        bd = karatsuba(b,d)
        pq = karatsuba(a+b,c+d)
        z = pq - ac - bd


        return int((10**n)*(ac) + (10**(n/2))*(z)+ (bd))
        
print(karatsuba(34443, 2))