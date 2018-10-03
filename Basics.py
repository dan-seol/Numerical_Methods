# Addition and subtraction
print(5 + 5)
print(5 - 5)

# Multiplication and division
print(3 * 5)
print(10 / 2)

# Exponentiation
print(4 ** 2)

# Modulo
print(18 % 7)

# How much is your $100 worth after 7 years?
print(100 * (1.1) ** 7)

# Create a variable savings
savings = 100

# Print out savings
print(savings)

# Create a variable factor
factor = 1.10

# Calculate result
result = savings * factor ** 7

# Print out result
print(result)

# Create a variable desc
desc = "compound interest"

# Create a variable profitable
profitable = True

desc = "compound interest"

# Assign product of factor and savings to year1
year1 = savings * factor

# Print the type of year1
print(type(year1))

# Assign sum of desc and desc to doubled
doubled = desc + desc

# Print out doubled
print(doubled)

# Definition of savings and result
savings = 100
result = 100 * 1.10 ** 7

# Fix the printout
print("I started with $" +str(savings) + " and now have $" + str(result) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float; there are bool() int() and str() and so on
pi_float = float(pi_string)

#Examples
print("I said " + ("Hey " * 2) + "Hey!")

print(True + False)

print("I can add integers, like " + str(5) + " to strings.")

# Supposed to make an error
# print("The correct answer to this multiple choice exercise is answer number " + 2

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas1 = [hall, kit, liv, bed, bath]

# Print areas
print(areas1)

# Adapt list areas
areas2 = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas2)

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath],
         ]

# Print out house
print(house)

# List slicing [a:b] (right endpoint does not get included)

# Create the areas list
areas3 = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas3[1])

# Print out last element from areas
print(areas3[-1])

# Print out the area of the living room
print(areas3[5])

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas3[3]+areas3[-3]

# Print the variable eat_sleep_area
print(eat_sleep_area)

# Use slicing to create downstairs
downstairs = areas3[:6]

# Use slicing to create upstairs
upstairs = areas3[-4:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)

# Correct the bathroom area
areas3[-1] = 10.50

# Change "living room" to "chill zone"
areas3[4] = "chill zone"

# Create the areas list and make some changes
areas4 = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas4+["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = list(areas)
#areas_copy = areas[:]

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)

# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)

help(max)
?max

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first+second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse = True)

# Print out full_sorted
print(full_sorted)

# string to experiment with: room
room = "poolhouse"

# Use upper() on room: room_up
room_up = room.upper()

# Print out room and room_up
print(room)
print(room_up)

# Print out the number of o's in room
print(room.count("o"))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 14.5 appears in areas
print(areas.count(14.5))

# Definition of radius
r = 0.43

# Import the math package
import math

# Calculate C
C = 2 * r * math.pi

# Calculate A
A = math.pi * r ** 2

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

# Definition of radius
r = 192500

# Import radians function of math package
from math import radians

# Travel distance of Moon over 12 degrees. Store in dist.
dist = r * radians(12)

# Print out dist
print(dist)

# Create list baseball
baseball1 = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a numpy array from baseball: np_baseball
np_baseball1 = np.array(baseball1)

# Print out type of np_baseball
print(type(np_baseball1))

height = [6, 5.12, 6.2, 5.5]
weight = [180, 140, 120, 160]

# Create a numpy array from height: np_height
np_height = np.array(height)

# Print out np_height
print(np_height)

# Convert np_height to m: np_height_m
np_height_m = 0.0254 * np_height[:]

# Print np_height_m
print(np_height_m)

# Create array from height with correct units: np_height_m
np_height_m = np.array(height) * 0.0254

# Create array from weight with correct units: np_weight_kg
np_weight_kg = np.array(weight) * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg / (np_height_m ** 2)

# Print out bmi
print(bmi)

# Create the light array

light = bmi < 21

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])

# True is converted to 1, False is converted to 0
np.array([True, 1, 2]) + np.array([3,4,False])

# Print out the weight at index 1
print(np_weight_kg[1])

# Print out sub-array of np_height: index 1 up to and including index 2
print(np_height[1:3])

# Create baseball, a list of lists
baseball2 = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball2 = np.array(baseball2)

# Print out the type of np_baseball
print(type(np_baseball2))

# Print out the shape of np_baseball
print(np_baseball2.shape)

# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create np_baseball (2 cols)
# np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
# print(np_baseball[49][:])

# Select the entire second column of np_baseball: np_weight
# np_weight = np_baseball[:, 1]

# Print out height of 124th player
# print(np_baseball[123][0])

# Create np_baseball (3 cols)
#np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
#print(np_baseball + updated)

# Create numpy array: conversion
#conversion = np.array([0.0254, 0.453592, 1])

# Print out product of np_baseball and conversion
#print(np_baseball * conversion)

# Create np_height from np_baseball
np_height = np_baseball2[:, 0]

# Print out the mean of np_height
print(np.mean(np_height))

# Print out the median of np_height
print(np.median(np_height))

# Print mean height (first column)
avg = np.mean(np_baseball2[:,0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_baseball2[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball2[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball2[:,0], np_baseball2[:,1])
print("Correlation: " + str(corr))

# Convert positions and heights to numpy arrays: np_positions, np_heights
# np_positions = np.array(positions)
# np_heights = np.array(heights)

# Heights of the goalkeepers: gk_heights
# gk_heights = np_heights[np_positions == 'GK']

# Heights of the other players: other_heights
## other_heights = np_heights[np_positions != 'GK']

# Print out the median height of goalkeepers. Replace 'None'
## print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
## print("Median height of other players: " + str(np.median(other_heights)))


#Linear Algebra in python
## Matrix and vector products

dot(a, b[, out])	Dot product of two arrays.
linalg.multi_dot(arrays)	Compute the dot product of two or more arrays in a single function call, while automatically selecting the fastest evaluation order.
vdot(a, b)	Return the dot product of two vectors.
inner(a, b)	Inner product of two arrays.
outer(a, b[, out])	Compute the outer product of two vectors.
matmul(a, b[, out])	Matrix product of two arrays.
tensordot(a, b[, axes])	Compute tensor dot product along specified axes for arrays >= 1-D.
einsum(subscripts, *operands[, out, dtype, ...])	Evaluates the Einstein summation convention on the operands.
linalg.matrix_power(M, n)	Raise a square matrix to the (integer) power n.
kron(a, b)	Kronecker product of two arrays.
#Decompositions
linalg.cholesky(a)	Cholesky decomposition.
linalg.qr(a[, mode])	Compute the qr factorization of a matrix.
linalg.svd(a[, full_matrices, compute_uv])	Singular Value Decomposition.
#Matrix eigenvalues
linalg.eig(a)	Compute the eigenvalues and right eigenvectors of a square array.
linalg.eigh(a[, UPLO])	Return the eigenvalues and eigenvectors of a Hermitian or symmetric matrix.
linalg.eigvals(a)	Compute the eigenvalues of a general matrix.
linalg.eigvalsh(a[, UPLO])	Compute the eigenvalues of a Hermitian or real symmetric matrix.
#Norms and other numbers
linalg.norm(x[, ord, axis, keepdims])	Matrix or vector norm.
linalg.cond(x[, p])	Compute the condition number of a matrix.
linalg.det(a)	Compute the determinant of an array.
linalg.matrix_rank(M[, tol])	Return matrix rank of array using SVD method
linalg.slogdet(a)	Compute the sign and (natural) logarithm of the determinant of an array.
trace(a[, offset, axis1, axis2, dtype, out])	Return the sum along diagonals of the array.
#Solving equations and inverting matrices
linalg.solve(a, b)	Solve a linear matrix equation, or system of linear scalar equations.
linalg.tensorsolve(a, b[, axes])	Solve the tensor equation a x = b for x.
linalg.lstsq(a, b[, rcond])	Return the least-squares solution to a linear matrix equation.
linalg.inv(a)	Compute the (multiplicative) inverse of a matrix.
linalg.pinv(a[, rcond])	Compute the (Moore-Penrose) pseudo-inverse of a matrix.
linalg.tensorinv(a[, ind])	Compute the ‘inverse’ of an N-dimensional array.
#Exceptions
linalg.LinAlgError	Generic Python-exception-derived object raised by linalg functions.
Linear algebra on several matrices at once
#New in version 1.8.0.
#Several of the linear algebra routines listed above are able to compute results for several matrices at once, if they are stacked into the same array.
#This is indicated in the documentation via input parameter specifications such as a : (..., M, M) array_like. This means that if for instance given an input array a.shape == (N, M, M), it is interpreted as a “stack” of N matrices, each of size M-by-M. Similar specification applies to return values, for instance the determinant has det : (...) and will in this case return an array of shape det(a).shape == (N,). This generalizes to linear algebra operations on higher-dimensional arrays: the last 1 or 2 dimensions of a multidimensional array are interpreted as vectors or matrices, as appropriate for each operation.
    scipy.linalg.lu(a, permute_l=False, overwrite_a=False, check_finite=True)[source]