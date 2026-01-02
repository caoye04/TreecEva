from itertools import combinations

# Simulate sensor fusion with weighted logic scoring
def analyze_readings(readings):
    base_score = 0
    temp_high_count = 0
    adjusted_values = []

    for r in readings:
        if r['temp'] > 37.5:
            temp_high_count += 1
        normalized = (r['pressure'] - 1013) / 100
        adjusted_values.append(normalized)

    # Irrelevant aggregation
    avg_adjusted = sum(adjusted_values) / len(adjusted_values) if adjusted_values else 0

    # Real contribution: count of high temp readings
    base_score += temp_high_count * 10

    return base_score


def calculate_stability_factor(history):
    # Dummy function with red herring computations
    changes = [abs(history[i] - history[i-1]) for i in range(1, len(history))]
    volatility = sum(changes) / len(changes) if changes else 0
    stability = 100 - volatility
    fake_correction = sum([x**2 for x in changes[-3:]]) if len(changes) >= 3 else 0  # Dead-end calc
    return stability // 10

# Main processing pipeline
def calculate_final_score(sensor_data, importance_weights):
    score = 0
    anomaly_flags = []

    # Process each sensor set
    for entry in sensor_data:
        reading_score = analyze_readings(entry['readings'])
        stability_tier = calculate_stability_factor(entry['timeline'])
        
        # Core logic: only stability_tier contributes directly
        score += stability_tier * importance_weights['stability']

        # Flag anomalies (unused later)
        if any(r['o2'] < 90 for r in entry['readings']):
            anomaly_flags.append(True)
    
    # Distractor block: complex but unused structure
    flagged_combinations = list(combinations(anomaly_flags, 2)) if len(anomaly_flags) >= 2 else []
    flag_logic = lambda x: all(x) or len(x) < 2
    spurious_value = len(flagged_combinations) if flag_logic(anomaly_flags) else 0

    # Key manipulation: offset based on unused spurious_value (but not actually used)
    # Final score depends only on accumulated stability tiers
    final_adjustment = 5 if spurious_value > 3 else -2
    
    # Only this line matters: previous logic just builds score from stability_tier
    score += final_adjustment  # This adjustment is deterministic

    return score

# Input data
weights = {'stability': 3, 'redundancy': 7}  # 'redundancy' never used

data = [
    {
        'readings': [
            {'temp': 36.8, 'pressure': 1020, 'o2': 95},
            {'temp': 38.1, 'pressure': 1005, 'o2': 88},
            {'temp': 37.9, 'pressure': 1030, 'o2': 92}
        ],
        'timeline': [100, 102, 101, 98, 97]  # decreasing trend
    },
    {
        'readings': [
            {'temp': 37.0, 'pressure': 1010, 'o2': 96},
            {'temp': 36.9, 'pressure': 1008, 'o2': 94}
        ],
        'timeline': [95, 96, 97, 97, 98]  # increasing
    }
]

# Execute main computation
final_score = calculate_final_score(data, weights)
print(f"Target result: {final_score}")