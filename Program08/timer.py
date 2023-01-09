"""
In this program, we use several methods compare the speed of numpy's built-in dot product
versus a loop-based dot product.  We visualize the results.
"""
# import packages - numpy, timeit and matplotlib.pyplot
import numpy as np
from timeit import timeit
import matplotlib.pyplot as plt

"""
Takes two vectors and returns their dot product. Uses only base python.
"""


def dot(A_arr, B_arr):
    dot_product = 0

    for a, b in zip(A_arr, B_arr):
        dot_product += a * b

    return dot_product


""" code inserted here """
# creating two vectors as numpy arrays
A_arr = np.random.randn(10 ** 3)
B_arr = np.random.randn(10 ** 3)

# converting the vector arrays to lists
A_list = list(A_arr)
B_list = list(B_arr)

""" 
Now we will see how the difference between the functions depends on the length of the vectors
This alternative writes a timer function that takes in the function to be times and it arguments.
Then it defines an equivalent (lambda) function with no arguments and times it.
"""


def time_function(func, *args, reps=10):
    """
    Passes *args into a function, func, and times it reps times, returns the average time in milliseconds (ms).
    """
    avg_time = timeit(lambda: func(*args), number=reps) / reps

    return avg_time * 1000


# find average of 10 runs of the loop-based function, using numpy arrays as input
time_function(dot, A_arr, B_arr)
# find average of 10 runs of the loop-based function, using numpy list as input
time_function(dot, A_list, B_list)
# find average of 10 runs of numpy's function
time_function(np.dot, A_arr, B_arr)

"""
Now see how the times change as the length of the vector grows. Build a function to time the different 
dot product functions at different lengths. Timing the function multiple times using the same vector 
might produce an inaccurate result, because the dot product may be faster to compute for some vectors. 
Repeat over different vectors to ensure a fair test.
"""


def time_dot_product(
        func,
        vector_length,
        input_type="array",
        data_reps=10,
        reps=2
):
    """
    Takes func, a function that performs a calculation on two vectors
    Returns the times (in ms) the function takes to run on std. normal generated vectors.

    Arguments:
    ----------
    func (function): a function that performs a calculation on two vectors
    vector_length (int): the length that the random vectors should be
    input_type (str): controls the data type of the random vector. Takes values \"list\" or \"array\"
    data_reps (int): the number of times to generate the data
    reps (int): the number of times to run the timer for each data set
    """

    """
                code inserted here:
    """
    total_time = 0

    for i in range(0, data_reps):

        A = np.random.standard_normal(vector_length)
        B = np.random.standard_normal(vector_length)

        if input_type == "list":
            A = list(A)
            B = list(B)

        inst_time = time_function(func, A, B, reps=reps)

        total_time += inst_time

    avg_time = total_time / data_reps

    return avg_time


# use this random seed for testing purposes
np.random.seed(123456)
print("dot product of 2 random vectors using random seed 123456: ",
      dot(np.random.standard_normal(1000), np.random.standard_normal(1000)))

# create an array, called lengths, of increasing times, 1, 10, 100, 1000, 10000, etc based upon number of orders of magnitude; experiement with this number on your computer to see what your machine can handle
ord_mag = 6
lengths = [10 ** n for n in range(0, ord_mag + 1)]

# time the loop-based function, using lists as inputs creating a list of times
""" code inserted here """
loop_list_times = [time_dot_product(dot, e, "list") for e in lengths]
loop_list_times

# time the loop-based function, using arrays as inputs creating a list of times
""" code inserted here """
loop_array_times = [time_dot_product(dot, e, "array") for e in lengths]
loop_array_times

# time numpy's dot product function creating a list of times
""" code inserted here """
np_times = [time_dot_product(np.dot, length) for length in lengths]
np_times

# plot numpy time vs loop with lists vs loop with arrays
# label each line accordingly
# title: Time Comparison of Dot Product Functions
# label X and Y accordingly
""" code inserted here """
plt.plot(lengths, loop_list_times, label="Loop-based function with lists as inputs")
plt.plot(lengths, loop_array_times, label="Loop-based function with arrays as inputs")
plt.plot(lengths, np_times, label="Numpy's function")
plt.title("Time Comparison of Dot Product Functions")
plt.xlabel("Length of Vectors")
plt.ylabel("Average Time (ms)")
plt.legend()
plt.show()

# graph the times for numpy's dot product alone to emphasize that they too are linear in the vector's length
# label & title everything accordingly
""" code inserted here """
plt.plot(lengths, np_times, label="Numpy's function", c="C2")
plt.title("Time Comparison of Dot Product Functions")
plt.xlabel("Length of Vectors")
plt.ylabel("Average Time (ms)")
plt.legend()
plt.show()
