import numpy as np



# Reading the input

m = int(input("How many rows does your matrix have?"))
n = int(input("How many columns does your matrix have?"))

A = np.zeros(shape=(m,n))
B = np.zeros(shape=(m))
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
    X[x]=float(input("Initial guess:"))
C = np.linalg.eigvals(A)
lmda1 = max(C)
lmdan = min(C)
omega_0 = (lmda1+lmdan)/2
if lmda1 >= 1:
    print("Warning: SOR might not converge if continued to be iterated")
print("Type in your choice of omega (Should be larger than 0 and less than 2)")
print("Recommended value:")
print(omega_0)
omega = float((input("Omega:")))
#D, the diagonal matrix and omega*L, L referring to the subdiagonal entries of the coefficient matrix A
D = np.diagflat(np.diag(A))
omega_L = omega*(np.tril(A)-D)
E = np.linalg.inv(D+omega_L)
U = np.triu(A)-D
F = omega*B-(omega*U+(omega-1)*D).dot(X)
G = E.dot(F)
H= (omega*B-(omega*U+(omega-1)*D).dot(G))
I= E.dot(H)
print(G)
print(I)

