"""
demo of how to use numpy's random generator and lists
also covers doing dot product calculation
"""
import numpy as np

# create the vectors as numpy arrays
A_arr = np.random.randn(10**2)
B_arr = np.random.randn(10**2)

# copy the vectors as lists
A_list = list(A_arr)
B_list = list(B_arr)

print("\nArray: ", A_arr)
print("\nList: ", A_list)

dot_product = 0
for a, b in zip(A_arr, B_arr):
    dot_product += a * b
print("\nDot Product from arrays: ", dot_product)

# 3D Array
array = np.random.randn(2, 2 ,2)
print("3D Array filled with random values : \n", array)

# Multiplying values with 3
print("\nArray * 3 : \n", array *3)

# Or we can directly do so by
array = np.random.randn(2, 2, 2) * 3 + 2
print("\nArray * 3 + 2 : \n", array)
