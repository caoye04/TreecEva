from itertools import compress, cycle

def analyze_pattern(values):
    trend = []
    for i in range(1, len(values)):
        trend.append(1 if values[i] > values[i-1] else -1 if values[i] < values[i-1] else 0)
    return trend

def calculate_final_score(raw_data, importance_weights):
    # Irrelevant transformation (distractor)
    normalized = [x / max(raw_data) for x in raw_data]
    
    # Semi-relevant filtering (some values are excluded but not used later)
    valid_indices = [i for i, x in enumerate(raw_data) if x > sum(raw_data) / len(raw_data)]
    filtered_data = list(compress(raw_data, [i in valid_indices for i in range(len(raw_data))]))
    
    # Core logic begins
    base_total = sum(x * w for x, w in zip(raw_data, importance_weights))
    adjustment_factor = 0
    
    # Analyze pattern to determine adjustment
    direction_changes = analyze_pattern(raw_data)
    change_count = sum(1 for i in range(1, len(direction_changes)) if direction_changes[i] != direction_changes[i-1])
    
    # Extra distraction: unused statistical calculation
    mean_val = sum(raw_data) / len(raw_data)
    variance_proxy = sum((x - mean_val) ** 2 for x in raw_data) / len(raw_data)
    entropy_like_metric = 0
    for x in raw_data:
        if x > 0:
            entropy_like_metric += x * x  # Not actually entropy, just looks complex

    # Real adjustment based on oscillation frequency
    if change_count > 2:
        adjustment_factor = 5
    elif change_count == 0:
        adjustment_factor = -3
    else:
        adjustment_factor = 1
    
    # Apply conditional bonus using cycle (itertools)
    bonus_sequence = cycle([2, -1, 3])
    bonus = sum(next(bonus_sequence) for _ in range(len(raw_data)))
    
    # Final computation
    final_score = base_total + adjustment_factor + bonus
    return final_score

# Input data
sensor_readings = [12, 15, 10, 18, 16, 20]
feature_weights = [0.5, 0.8, 0.3, 1.0, 0.7, 0.9]

# Misleading pre-processing (dead path)
data_copy = sensor_readings[:]
data_copy.sort(reverse=True)
median_approx = data_copy[len(data_copy)//2]

# Key execution point
temp_result = sum(sensor_readings[i] * feature_weights[i] for i in range(len(sensor_readings)))
final_score = calculate_final_score(sensor_readings, feature_weights)

print(f"Result: {final_score}")