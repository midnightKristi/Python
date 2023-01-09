# demo of how to time a vector function (or any function) using timeit

# import packages
import numpy as np
from timeit import timeit


def time_function(
        func,
        *args,
        reps=10):
    """
    Passes *args into a function, func, and times it reps times, returns the average time in milliseconds (ms).
    """

    avg_time = timeit(lambda: func(*args), number=reps) / reps

    return avg_time * 1000


def some_array_function(A, B):
    total = 0
    for a, b in zip(A, B):
        total += a / b
    return total


def time_some_array_function(
        func,
        vector_length,
        data_reps=10,
        reps=2):
    """
    Takes func, a function that perfroms a calculation on two vectors
    Returns the times (in ms) the function takes to run on std. normal generated vectors.

    Arguments:
    ----------
    func (function): a function that perfroms a calculation on two vectors
    vector_length (int): the length that the random vectors should be
    data_reps (int): the number of times to generate the data
    reps (int): the number of times to run the timer for each data set
    """

    total_time = 0

    for i in range(0, data_reps):
        A = np.random.standard_normal(vector_length)
        B = np.random.standard_normal(vector_length)
        total_time += time_function(func, A, B, reps=reps)

    avg_time = total_time / data_reps
    return avg_time


# test the array function using a constant seed
np.random.seed(543)
print(some_array_function(np.random.standard_normal(1000), np.random.standard_normal(1000)))

# test the timing function for several increasing vector sizes
times = [time_some_array_function(some_array_function, e) for e in [10, 100, 1000, 10000, 100000, 1000000]]

print(times)
