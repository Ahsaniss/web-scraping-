# Importing the NumPy library
import numpy as np
# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])
# Perform basic operations
print("Array:", arr)
# Addition
arr_add = arr + 2
print("Array after addition:", arr_add)
# Multiplication
arr_mul = arr * 3
print("Array after multiplication:", arr_mul)

# Mean
arr_mean = np.mean(arr)
print("Mean of the array:", arr_mean)

# Reshaping the array
arr_reshaped = arr.reshape((1, 5))
print("Reshaped array:", arr_reshaped)

# Creating a 2D array (Matrix)
matrix = np.array([[1, 2], [3, 4], [5, 6]])
print("2D Array (Matrix):\n", matrix)

# Matrix multiplication
matrix_mult = np.dot(matrix.T, matrix)  # Matrix multiplication of transpose with original
print("Matrix multiplication result:\n", matrix_mult)
