from collections import defaultdict
import math

# Simulate sensor data with noise and redundancy
def generate_noisy_data():
    raw_values = [12.5, 13.0, 11.8, 14.2, 13.1, 12.9, 13.3]
    timestamps = ['t0', 't1', 't2', 't3', 't4', 't5', 't6']
    return dict(zip(timestamps, raw_values))

def apply_filter(data, method='moving_avg'):
    filtered = []
    values = list(data.values())
    for i in range(len(values)):
        if i == 0:
            filtered.append(values[i])
        else:
            # Irrelevant smoothing logic (not used later)
            prev = filtered[-1]
            curr = values[i]
            smoothed = (prev + curr) / 2
            filtered.append(smoothed if method == 'moving_avg' else curr)
    return filtered

def calculate_entropy(arr):
    # Dead-end computation: entropy not used in final result
    freq_map = defaultdict(int)
    for val in arr:
        freq_map[round(val)] += 1
    total = len(arr)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def calculate_final_score(data, weights):
    values = list(data.values())
    
    # Step 1: Normalize values to z-scores (using hardcoded mean/std)
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    std_dev = math.sqrt(variance)
    z_scores = [(x - mean_val) / std_dev for x in values]
    
    # Step 2: Apply weight transformation via lambda
    transformer = lambda z, w: z * w
    weighted_z = [transformer(z, weights[i % len(weights)]) for i, z in enumerate(z_scores)]
    
    # Step 3: Aggregate using max deviation from zero
    max_positive = max(x for x in weighted_z if x > 0)
    min_negative = min(x for x in weighted_z if x < 0)
    peak_deviation = max(max_positive, abs(min_negative))
    
    # Step 4: Adjust score based on data length multiplier (distraction)
    length_factor = len(values) * 0.1  # Not actually applied
    
    # Step 5: Final score is average of absolute weighted z-scores
    abs_weighted = [abs(z) for z in weighted_z]
    final_score = sum(abs_weighted) / len(abs_weighted)
    
    # Red herring: string processing with no impact
    status_msg = "Processing complete".upper().replace(" ", "_")
    log_entry = f"STATUS:{status_msg}:COUNT={len(values)}"
    
    return round(final_score, 4)

# Main execution
sensor_data = generate_noisy_data()
processing_weights = [0.8, 1.2, 0.9]

# Intermediate transformations (some irrelevant)
smoothed_readings = apply_filter(sensor_data)
entropy_value = calculate_entropy(smoothed_readings)  # Unused

# Critical statement
final_score = calculate_final_score(sensor_data, processing_weights)

print(f"Result: {final_score}")