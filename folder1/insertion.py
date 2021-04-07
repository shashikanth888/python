import random

def ins_sort(A, n):
    count = 0
    for i in range(1,n):
        j = i-1
            # print(i,j)
        if A[i] < A[j]:
            tmp = A[i]
            for k in range(i, j, -1):
                print(A)
                # print("i,j is ",i,j)
                count+=1
                A[k] = A[k-1]
            A[j] = tmp
    print(A, count)

A = list(range(10))
A.reverse()
print(A)
ins_sort(A, len(A))