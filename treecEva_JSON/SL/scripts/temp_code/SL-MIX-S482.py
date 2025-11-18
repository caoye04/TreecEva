import itertools
from functools import reduce

# Sensor readings: each sublist represents one sensor's sequence of readings
sensor_readings = [
    [10, 12, 14, 13, 15],
    [5, 7, 6, 8, 9, 7],
    [20, 22, 21, 23, 25, 24, 26],
    [1, 3, 2, 4, 6, 5]
]

def calculate_stability_score(readings):
    if len(readings) < 2:
        return 0
    # Step 1: Calculate pairwise differences
    differences = [readings[i+1] - readings[i] for i in range(len(readings)-1)]
    # Step 2: Count differences within threshold
    count_within_threshold = sum(1 for diff in differences if abs(diff) <= 2)
    # Step 3: Calculate sum of readings
    sum_readings = sum(readings)
    # Stability score is count * sum
    return count_within_threshold * sum_readings

# Calculate stability scores for all sensors
stability_scores = list(map(calculate_stability_score, sensor_readings))

# Find median stability score
stability_scores.sort()
n = len(stability_scores)
median_stability_score = stability_scores[n//2] if n % 2 == 1 else (stability_scores[n//2 - 1] + stability_scores[n//2]) // 2

print(f"Result: {median_stability_score}")