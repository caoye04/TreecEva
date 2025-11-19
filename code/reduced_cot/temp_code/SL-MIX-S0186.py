import math
from collections import defaultdict

def calculate_weighted_average(signals):
    n = len(signals)
    indexed_signals = [(signals[i], i) for i in range(n)]
    indexed_signals.sort(key=lambda x: x[0])
    
    # Take the upper half (divide and conquer concept)
    half_point = n // 2
    if n % 2 == 1:
        half_point += 1
    upper_half = indexed_signals[half_point:]
    
    # Compute weighted sum
    weighted_sum = 0
    for value, original_index in upper_half:
        weight = (original_index + 1) ** 2
        weighted_sum += value * weight
    
    return weighted_sum

# Sensor signal strengths
sensor_readings = [45, 23, 67, 12, 89, 34, 78, 56]
weighted_sum = calculate_weighted_average(sensor_readings)
print(f"Result: {weighted_sum}")