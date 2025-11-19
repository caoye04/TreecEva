import heapq
import math

def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def gcd_list(lst):
    result = lst[0]
    for i in range(1, len(lst)):
        result = math.gcd(result, lst[i])
        if result == 1:
            break
    return result

# Initialize sensor grid data
sensor_readings = [
    [12, 28, 9],
    [15, 35, 21],
    [8, 16, 32]
]

# Generate Fibonacci weights for sensor positions
fib_weights = fibonacci_sequence(len(sensor_readings) * len(sensor_readings[0]))

# Apply Fibonacci weighting to sensor readings
weighted_sensors = []
for row_idx, row in enumerate(sensor_readings):
    weighted_row = []
    for col_idx, reading in enumerate(row):
        weight_index = row_idx * len(row) + col_idx
        weighted_value = reading * fib_weights[weight_index] if weight_index < len(fib_weights) else reading
        weighted_row.append(weighted_value)
    weighted_sensors.append(weighted_row)

# Flatten and apply prime-indexed adjustments
flattened_weighted = [item for sublist in weighted_sensors for item in sublist]
adjusted_readings = []
for idx, value in enumerate(flattened_weighted):
    if is_prime(idx + 1):  # 1-indexed position check
        adjusted_readings.append(value + (idx * 2))
    else:
        adjusted_readings.append(value)

# Use heap to find top-k values where k is GCD of original sensor sums
sensor_sums = [sum(row) for row in sensor_readings]
gcd_k = gcd_list(sensor_sums)
top_k_heap = heapq.nlargest(gcd_k, adjusted_readings)

# Apply exponential smoothing with lambda function
smoothing_factor = 0.3
exp_smooth = lambda current, previous: (smoothing_factor * current) + ((1 - smoothing_factor) * previous) if previous is not None else current

smoothed_values = []
prev_val = None
for val in top_k_heap:
    smoothed_val = exp_smooth(val, prev_val)
    smoothed_values.append(int(smoothed_val))
    prev_val = smoothed_val

# Calculate final aggregate signal as LCM of smoothed values
from functools import reduce
lcm = lambda a, b: abs(a*b) // math.gcd(a, b) if a and b else 0
final_aggregate_signal = reduce(lcm, smoothed_values) if smoothed_values else 0

print(f"Result: {final_aggregate_signal}")