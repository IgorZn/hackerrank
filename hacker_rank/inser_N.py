import random
def insert_sort(A):
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= k
    print(A)

def choise_sort(A):
    N = len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]




A = [5, 4, 3, 2, 1]
A_sorted = [1, 2, 3, 4, 5]


if __name__ == '__main__':
    print(A, A_sorted)
    insert_sort(A)
    print(A, A_sorted)
    print("OK" if A == A_sorted else "Fail")
