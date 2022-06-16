def Merge(B, C):
    # Account for empty arrays created from uneven divisions
    if (B == None):
        return (C, 0)
    elif (C == None):
        return (B, 0)
    else:
        inversions = 0
        Blength = len(B[0])
        Clength = len(C[0])
        n = Blength+Clength

        output = ([0] * (n), 0)
        # Append infinity values for both arrays if either one finishegs before the other
        B[0].append(float('inf'))
        C[0].append(float('inf'))
        i = 0
        j = 0

        for x in range(0,n):
            if (B[0][i])<(C[0][j]):
                output[0][x] = B[0][i]
                i+=1
            else:
                output[0][x] = C[0][j]
                j+=1
                inversions += len(B[0])-i
        return (output, inversions)




def SplitAndCount(A):
    if len(A) == 1: # base case
        return (A, 0)
    else: # recursive case
        mid = len(A) // 2
        (B, leftInv) = SplitAndCount(A[:mid])
        (C, rightInv) = SplitAndCount(A[mid:])
        print((B, leftInv))
        (D, splitInv) = Merge((B, leftInv),(C, leftInv))
        return (D, leftInv+rightInv+splitInv)

print(SplitAndCount([5,4,3])[0])