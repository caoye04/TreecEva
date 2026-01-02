from collections import defaultdict

# Simulate environmental temperature readings over time
def process_readings(sensor_data, correction_factor=1.05):
    adjusted = [round(x * correction_factor, 2) for x in sensor_data]
    return adjusted

# Calculate weighted average with decay factor
def calculate_weighted_average(values, weights):
    if len(values) != len(weights):
        raise ValueError("Mismatched lengths")
    total = sum(val * weight for val, weight in zip(values, weights))
    norm = sum(weights)
    return round(total / norm, 3)

# Determine threshold based on trend and confidence
def calculate_threshold(readings, weights):
    trend = calculate_weighted_average(readings, weights)
    deviation = abs(readings[-1] - trend)
    confidence = 0.9 if deviation < 5 else 0.7
    return int(trend * confidence) if trend > 80 else int(trend * 0.85)

# Main data
raw_readings = [78, 82, 85, 90, 93, 95, 97]
weights = [0.1, 0.1, 0.15, 0.2, 0.2, 0.15, 0.1]

# Process data
adjusted_readings = process_readings(raw_readings)
baseline = sum(adjusted_readings) / len(adjusted_readings)

# Irrelevant distraction: counting occurrences (minimal interference)
dist_counts = defaultdict(int)
for val in adjusted_readings:
    dist_counts[int(val)] += 1

unused_var = [x for x in adjusted_readings if x > 90]

# Key computation
threshold_score = calculate_threshold(adjusted_readings, weights)

print(f"Result: {threshold_score}")