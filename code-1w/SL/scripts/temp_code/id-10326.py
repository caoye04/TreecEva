import itertools

# Simulate sensor readings with noise filtering and threshold logic
def process_sensor_data(raw_readings):
    # Remove outliers using interquartile range approximation
    sorted_readings = sorted(raw_readings)
    q1 = sorted_readings[len(sorted_readings) // 4]
    q3 = sorted_readings[3 * len(sorted_readings) // 4]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    filtered = [x for x in raw_readings if lower_bound <= x <= upper_bound]

    # Misleading computation: normalized_power has no effect on final result
    total_power = sum(x ** 2 for x in filtered)
    normalized_power = total_power / len(filtered) if filtered else 0

    # Scale values to 0-100 range
    min_val, max_val = min(filtered), max(filtered)
    scaled_values = [(x - min_val) / (max_val - min_val) * 100 for x in filtered] if max_val > min_val else [50] * len(filtered)

    # Distractor list comprehension with string operations (no impact)
    status_labels = ['high' if v > 75 else 'medium' if v > 25 else 'low' for v in scaled_values]
    encoded_status = [s[0].upper() + f'{len(s)}' for s in status_labels]

    return scaled_values, encoded_status


def compute_aggregate(scaled, thresholds):
    # Apply dynamic weighting based on threshold crossings
    weights = []
    for val in scaled:
        w = 1.0
        for t in thresholds:
            if val > t:
                w += 0.1
        weights.append(w)
    
    # Weighted average calculation
    weighted_sum = sum(v * w for v, w in zip(scaled, weights))
    total_weight = sum(weights)
    aggregate = weighted_sum / total_weight if total_weight != 0 else 0

    # Red herring: entropy calculation not used in output
    entropy = 0
    for w in weights:
        if w > 0:
            entropy -= (w / total_weight) * __import__('math').log(w / total_weight + 1e-9)

    # Unrelated slicing operation for distraction
    mid_slice = scaled[len(scaled)//3 : 2*len(scaled)//3]
    temp_adjustment = sum(mid_slice) / len(mid_slice) * 0.05 if mid_slice else 0

    return round(aggregate + temp_adjustment, 4)

# Main execution
raw_data = [89, 92, 105, 45, 88, 90, 94, 300, 85, 87, 40, 91]  # Includes outlier 300
thresholds = [60, 75, 85]

# Extract components from processing
processed_values, labels = process_sensor_data(raw_data)

# Key computation step
final_score = compute_aggregate(processed_values, thresholds)

# Irrelevant itertools usage for interference
combinations = list(itertools.combinations_with_replacement([1, 2], 2))
dummy_shift = sum(len(str(c)) for c in combinations)

# Additional misleading variable
baseline_offset = sum(ord(ch) for ch in 'baseline') % 1000

print(f"Result: {final_score}")