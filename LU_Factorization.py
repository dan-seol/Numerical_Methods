import numpy as np
import scipy as sp
from scipy import linalg
from fractions import Fraction
# Printing the output
def pprint(A):
    r = A.shape[0]
    c = A.shape[1]
    for i in range(0, r):
        line = ""
        for j in range(0, c):
            line += str(A[i][j]) + "\t\t"

        print(line)
    print("")
# Reading the input

m = int(input("How many rows does your matrix have?"))
n = int(input("How many columns does your matrix have?"))

A = sp.zeros(shape=(m,n))
B = sp.zeros(shape=(m))
for k in range(0, m):
    for l in range(0, n):
                print("Entries for the matrix A")
                A[k][l] = float(input("Type:"))
for b in range(0, m):
    print("Entries for the constant vector b")
    B[b] =float(input("Returns:"))
sp.set_printoptions(precision=3)
print(linalg.lu(A, permute_l=False, overwrite_a=False, check_finite=True))
t = bool(input("Do you also want to solve the system?"))
print("---------------------------------------------------------------")
if t == True:
    print(linalg.lu_solve(linalg.lu_factor(A),B))
