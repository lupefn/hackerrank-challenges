import math, sys, os, random

def flippingMatrix(matrix):
    upperQuadIdx = int(len(matrix) / 2)
    total = 0
    for i in range(upperQuadIdx):
        for j in range(upperQuadIdx):
            total += max([matrix[i][j], matrix[i][2*upperQuadIdx-1-j], matrix[2*upperQuadIdx-1-i][j], matrix[2*upperQuadIdx-1-i][2*upperQuadIdx-1-j]])
    return total

def sumUpperQuadrant(matrix, upperIdx):
    total = 0
    for i in range(upperIdx):
        total += matrix[i][0:upperIdx]
    return total

if __name__ == '__main__':
    fptr = sys.stdout

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
    # suma = 0
    # for i in range(n):
    #     for j in range(n):
    #         suma += max(max(a[i][j],a[2*n-i-1][j]),max(a[i][2*n-j-1],a[2*n-i-1][2*n-j-1]))
    # print(suma)