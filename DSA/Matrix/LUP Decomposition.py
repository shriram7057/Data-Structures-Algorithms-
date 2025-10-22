def main():
    n = 3
    A = [[2, -1, -2], [-4, 6, 3], [-4, -2, 8]]
    L = [[0 for i in range(n)] for j in range(n)]
    U = [[0 for i in range(n)] for j in range(n)]
    P = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i > j:
                U[i][j] = 0
                L[i][j] = A[i][j]
                P[i][j] = 0
            elif i == j:
                L[i][j] = 1
                U[i][j] = A[i][j]
                P[i][j] = 1
            else:
                L[i][j] = 0
                U[i][j] = A[i][j]
                P[i][j] = 0
    for k in range(n-1):
        max = 0
        pivot = k
        for i in range(k, n):
            if U[i][k] > max:
                max = U[i][k]
                pivot = i
        if pivot != k:
            for j in range(n):
                temp = U[k][j]
                U[k][j] = U[pivot][j]
                U[pivot][j] = temp
                temp = P[k][j]
                P[k][j] = P[pivot][j]
                P[pivot][j] = temp
                if j < k:
                    temp = L[k][j]
                    L[k][j] = L[pivot][j]
                    L[pivot][j] = temp
        for i in range(k+1, n):
            L[i][k] = U[i][k]/U[k][k]
            for j in range(k, n):
                U[i][j] = U[i][j] - L[i][k]*U[k][j]
    print("L Matrix")
    for i in range(n):
        for j in range(n):
            print(L[i][j], end=" ")
        print()
    print("U Matrix")
    for i in range(n):
        for j in range(n):
            print(U[i][j], end=" ")
        print()
    print("P Matrix")
    for i in range(n):
        for j in range(n):
            print(P[i][j], end=" ")
        print()
main()