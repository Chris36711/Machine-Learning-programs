import numpy as np
import statistics

data = [10, 20, 30, 40, 50, 20, 30]

print("Data:", data)

mean_value = statistics.mean(data)
median_value = statistics.median(data)
mode_value = statistics.mode(data)

variance_value = statistics.variance(data)
std_value = statistics.stdev(data)

print("Mean =", mean_value)

print("Median =", median_value)

print("Mode =", mode_value)

print("Variance =", variance_value)

print("Standard Deviation =", std_value)