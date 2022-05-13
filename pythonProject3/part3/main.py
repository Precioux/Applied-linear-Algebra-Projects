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
toeplitz = np.zeros([n, n], dtype=int)
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
