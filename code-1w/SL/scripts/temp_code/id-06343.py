from itertools import combinations

# Simulate sensor array diagnostics with weighted reliability scoring
def analyze_sensor_group(group, base_threshold):
    if len(group) < 2:
        return 0.0
    variance = sum((x - sum(group)/len(group))**2 for x in group) / len(group)
    return variance < base_threshold

def generate_feedback_signals(sensors):
    signals = {}
    for i, sensor in enumerate(sensors):
        signals[f'sensor_{i}'] = [val * (0.95 + i*0.02) for val in sensor]
    # Irrelevant transformation
    dummy_transform = {k: [v[i] * v[-(i+1)] for i in range(len(v))] for k, v in signals.items()}
    return signals

def compute_stability_index(readings_list):
    total_fluctuation = 0.0
    for readings in readings_list:
        for i in range(1, len(readings)):
            total_fluctuation += abs(readings[i] - readings[i-1])
    return total_fluctuation / (len(readings_list) * 10) if readings_list else 0.0

# Core logic with distraction
sensors_data = [
    [102, 104, 103, 105, 106],
    [205, 207, 208, 206, 209],
    [51,  49,  50,  52,  53],
    [75,  77,  76,  78,  77]
]

feedback_map = generate_feedback_signals(sensors_data)

# Misleading intermediate analysis
reliability_flags = []
for key, readings in feedback_map.items():
    mean_val = sum(readings) / len(readings)
    stable = all(abs(readings[i] - mean_val) < 10 for i in range(len(readings)))
    reliability_flags.append(stable)

# Dummy combinatorial check (unused but plausible)
dummy_pairs = list(combinations(range(len(sensors_data)), 2))
false_alert_count = 0
for idx1, idx2 in dummy_pairs:
    set1 = set(map(lambda x: round(x), sensors_data[idx1]))
    set2 = set(map(lambda x: round(x), sensors_data[idx2]))
    if len(set1 & set2) > 0:
        false_alert_count += 1

# Actual weighting scheme
weights = {
    'sensor_0': 0.8,
    'sensor_1': 1.2,
    'sensor_2': 0.9,
    'sensor_3': 1.1
}

# Real performance aggregation
def aggregate_performance(feedback, weight_map):
    valid_groups = 0
    total_weighted_variance = 0.0
    
    for name, signal in feedback.items():
        w = weight_map.get(name, 1.0)
        # Extract original index from name
        orig_idx = int(name.split('_')[1])
        original = sensors_data[orig_idx]
        
        # Compute normalized deviation
        deviations = [abs(signal[i] - original[i]) for i in range(len(original))]
        avg_dev = sum(deviations) / len(deviations)
        
        # Weighted contribution only if below threshold
        if avg_dev < 5.0:
            valid_groups += 1
            total_weighted_variance += avg_dev * w
    
    # Secondary validation using enumerate and zip
    adjustment_factor = 0.0
    for i, (dev, weight) in enumerate(zip(
        [sum(abs(sensors_data[j][k] - feedback[f'sensor_{j}'][k]) for k in range(5)) / 5 
         for j in range(4)],
        [weights[f'sensor_{j}'] for j in range(4)]
    )):
        if i % 2 == 0:
            adjustment_factor += dev * weight * 0.1  # Minor correction
    
    # Final score computation
    base_score = (valid_groups * 25) + (10 - total_weighted_variance)
    final_adjustment = base_score * (1 + adjustment_factor / 100)
    return int(round(final_adjustment))

# Execute main logic
stability = compute_stability_index(sensors_data)
stability_bonus = int(stability * 10)

final_score = aggregate_performance(feedback_map, weights)

# Print result as required
print(f"Target result: {final_score}")