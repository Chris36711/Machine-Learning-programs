import math
import statistics
import numpy as np

data = [1, 2, 3, 4, 5]

print("Data =", data)

print("Square root of 16 =", math.sqrt(16))

print("Factorial of 5 =", math.factorial(5))

mean_val = statistics.mean(data)

print("Mean =", mean_val)

arr = np.array(data)

print("Array =", arr)

print("Sum =", np.sum(arr))

print("Maximum =", np.max(arr))

print("Minimum =", np.min(arr))