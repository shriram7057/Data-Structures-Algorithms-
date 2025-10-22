def main():
    n = 3
    A = [[2, -1, -2], [-4, 6, 3], [-4, -2, 8]]
    L = [[0 for i in range(n)] for j in range(n)]
    U = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i > j:
                U[i][j] = 0
                L[i][j] = A[i][j]
            elif i == j:
                L[i][j] = 1
                U[i][j] = A[i][j]
            else:
                L[i][j] = 0
                U[i][j] = A[i][j]
    for k in range(n):
        for i in range(k + 1, n):
            L[i][k] = U[i][k] / U[k][k]
            for j in range(k, n):
                U[i][j] = U[i][j] - L[i][k] * U[k][j]
    print("L Matrix")
    for i in range(n):
        for j in range(n):
            print(L[i][j], end = " ")
        print()
    print("U Matrix")
    for i in range(n):
        for j in range(n):
            print(U[i][j], end = " ")
        print()
main()