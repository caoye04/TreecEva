from collections import defaultdict

# Simulate sensor data aggregation and anomaly adjustment
raw_readings = [12, 15, 12, 18, 14, 15, 21, 12, 14]
threshold = 13

def count_anomalies(data, limit):
    return sum(1 for x in data if x > limit)

def adjust_for_drift(values, factor=0.9):
    return [int(x * factor) for x in values]

def generate_lookup(keys, default=0):
    lookup = defaultdict(lambda: default)
    for k in keys:
        lookup[k] += 1
    return lookup

def compute_ranking(scores, deductions):
    base_total = sum(scores)
    penalty_adjustment = sum(deductions) * 2
    bonus = len(scores) if base_total > 100 else 0
    intermediate = base_total - penalty_adjustment + bonus

    # Irrelevant transformation (distractor)
    squared_values = [x**2 for x in scores]
    avg_square = sum(squared_values) / len(squared_values)
    dummy_threshold_check = avg_square > 200  # Not used in result

    # Another red herring: tracking frequency of scores
    freq_map = generate_lookup(scores)
    unique_count = len(freq_map)

    # Actual computation path
    modifier = 3 if unique_count >= 5 else 1
    adjusted_total = intermediate * modifier

    # More misleading logic
    outlier_count = count_anomalies(scores, threshold)
    if outlier_count > 3:
        adjusted_total -= 10  # This branch won't trigger

    # Final irrelevant operation
    normalized = adjusted_total / 10.0
    rounded_normalized = round(normalized, 2)

    return int(rounded_normalized)

# Data processing pipeline
filtered_data = [x for x in raw_readings if x % 3 == 0]  # Only multiples of 3
points = adjust_for_drift(filtered_data, 1.1)
penalties = [1, 2, 1]

# Additional distractor variables
stats_summary = {
    'max': max(raw_readings),
    'min': min(raw_readings),
    'range': max(raw_readings) - min(raw_readings)
}
duplicate_tracker = set()
duplicates_found = 0
for val in raw_readings:
    if val in duplicate_tracker:
        duplicates_found += 1
    else:
        duplicate_tracker.add(val)

# Key execution point
final_score = compute_ranking(points, penalties)
print(f"Result: {final_score}")