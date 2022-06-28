# LA HW3
# Samin Mahdipour - 9839039
# part III
import numpy as np

# get data
n = int(input("Enter  n:"))
r = np.zeros(n, dtype=int)
c = np.zeros(n, dtype=int)
print("Enter array R : ")
for i in range(0, n):
    r[i] = int(input(f"r[{i}]: "))
print("Enter array C : ")
for i in range(0, n):
    c[i] = int(input(f"c[{i}]: "))
# make toeplitz
toeplitz = np.zeros([n, n], dtype=float)
# 1) add verctors
for i in range(0, n):
    toeplitz[i][0] = c[i]
for j in range(1, n):
    toeplitz[0][j] = r[j]
# 2) generate others
for i in range(0, n):
    for j in range(0, n):
        if (i + 1 < n) and (j + 1 < n):
            toeplitz[i + 1][j + 1] = toeplitz[i][j]
print("Toeplitz matrix : ")
print(toeplitz)
# make an upper Triangular
for i in range(0, n):
    head = toeplitz[i][i]
    check = i + 1
    while check != n :
        item = toeplitz[check][i]
        removing = np.zeros(n, dtype=float)
        removing[0] = float ( (float(toeplitz[i][0]) / head) * item)
        removing[1] = float ( (float(toeplitz[i][1]) / head) * item)
        removing[2] = float ( (float(toeplitz[i][2]) / head) * item)
        toeplitz[check] = toeplitz[check] - removing
        check = check + 1
print("Upper triangular matrix")
print(toeplitz)
# calculating determinant
determinant = 1
for i in range(0,n):
    determinant = determinant * toeplitz[i][i]
print(f"Determinant is {determinant}")