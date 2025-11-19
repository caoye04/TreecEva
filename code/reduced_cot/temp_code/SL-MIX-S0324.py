from collections import defaultdict
import math

def is_valid_peak(readings, index, memo):
    if index in memo:
        return memo[index]
    if index <= 0 or index >= len(readings) - 1:
        memo[index] = False
        return False
    left_check = readings[index] > readings[index - 1]
    right_check = readings[index] > readings[index + 1]
    threshold_check = readings[index] > sum(readings) / len(readings)
    # Short-circuit evaluation with logical operations
    if left_check and right_check and threshold_check:
        result = True
    else:
        result = False
    memo[index] = result
    return result

def count_peaks_recursive(readings, index, accumulator, memo):
    if index >= len(readings):
        return accumulator
    if is_valid_peak(readings, index, memo):
        return count_peaks_recursive(readings, index + 2, accumulator + 1, memo)
    else:
        return count_peaks_recursive(readings, index + 1, accumulator, memo)

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Sensor readings derived from fibonacci sequence with some modifications
sensor_readings = [fibonacci(i) for i in range(1, 11)]
sensor_readings[5] += 10  # Introduce a potential peak

# Initialize tracking variables
memoization_cache = {}
peak_count = count_peaks_recursive(sensor_readings, 0, 0, memoization_cache)
print(f"Result: {peak_count}")