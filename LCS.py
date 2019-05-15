"""
Наибольшая общая подпоследовательность
"""

def lcs(a, b):
    F = [[0] * (len(b)+1) for i in range(len(a)+1)]
    print(F)
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                F[i][j] = 1 + F[i-1][j-1]
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])

    return F[-1][-1]

print(lcs([x for x in range(15)], [x for x in range(15)]))
