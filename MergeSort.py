def Merge(B, C):
    # Account for empty arrays created from uneven divisions
    if (B == None):
        return C
    elif (C == None):
        return B
    else:
        n = len(B)+len(C)
        output = [0] * (n)
        # Append infinity values for both arrays if either one finishes before the other
        B.append(float('inf'))
        C.append(float('inf'))
        i = 0
        j = 0

        for x in range(0,n):
            if B[i]< C[j]:
                output[x] = B[i]
                i+=1
            else:
                output[x] = C[j]
                j+=1
        return output




def MergeSort(A):
    if len(A) == 1: # base case
        return A
    else: # recursive case
        mid = len(A) // 2
        B = MergeSort(A[:mid])
        C = MergeSort(A[mid:])
        return Merge(B, C)

print(MergeSort([5,4,3,2,1,0,-1]))