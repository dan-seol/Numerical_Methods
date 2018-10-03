import numpy as np

k=1

# Reading the input

m = int(input("How many rows does your matrix have?"))
n = int(input("How many columns does your matrix have?"))

A = np.zeros(shape=(m,n))
B = np.zeros(shape=(m))
X_0 = np.zeros(shape=(m))
X = np.zeros(shape=(m))
for k in range(0, m):
    for l in range(0, n):
                print("Entries for the matrix A")
                A[k][l] = float(input("Type:"))
for b in range(0, m):
    print("Entries for the constant vector b")
    B[b] =float(input("Returns:"))

for x in range(0,m):
    print("Type in your initial guesses")
    X_0[x]=float(input("Initial guess:"))
#TOL
print("What is your error tolerance?")
TOL = float(input("TOL:"))

#Maximum number of iterations
print("How many times do you want to iterate at most?")
M = int(input("M:"))

#Extracting inverse of the diagonal part
D =  np.diagflat(np.diag(A))
D_inv = np.linalg.inv(D)
C= D_inv.dot((-A+D))

while k <= M:
    X = C.dot(X_0) + D_inv.dot(B)
    print(X)

    if np.linalg.norm(X-X_0) < TOL:
      print("Successful! :)")

      break
    X_0 = X
    print(k)
    k = k+1
print("Maximum number of iterations exceeded")










