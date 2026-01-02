import math

def preprocess_data(raw):
    # Normalize and filter data (some steps are red herrings)
    normalized = [x / max(raw) for x in raw]
    filtered = [x for x in normalized if x > 0.1]
    squared_devs = [(x - sum(filtered)/len(filtered))**2 for x in filtered]
    variance = sum(squared_devs) / len(squared_devs) if filtered else 0
    return filtered  # variance is computed but not used later

def calculate_weighted_sum(values, weights):
    weighted = sum(v * w for v, w in zip(values, weights))
    scaling_factor = 1.0 + math.log(len(values) + 1)  # unused distraction
    offset_correction = sum(1 for v in values if v > 0.5) * 0.01  # irrelevant
    return weighted

def evaluate_thresholds(arr):
    # Complex logic that doesn't affect final result
    count_high = 0
    status_flags = []
    for val in arr:
        if val > 0.7:
            count_high += 1
            status_flags.append(True)
        else:
            status_flags.append(False)
    temp_result = count_high * 2  # dead computation
    return len(status_flags)  # returned but unused

def calculate_final_score(data, weights):
    # Core logic hidden among distractions
    adjusted_data = [d * 1.1 for d in data]
    
    # Irrelevant bitwise manipulation
    magic_key = 0
    for i in range(len(adjusted_data)):
        magic_key ^= int(adjusted_data[i] * 100) & 7
    
    # Actual relevant calculation
    base_score = calculate_weighted_sum(adjusted_data, weights)
    penalty = 0
    for d in adjusted_data:
        if d < 0.3:
            penalty += 0.5
    
    # Final formula
    final = base_score - penalty
    debug_log = f'Score breakdown: base={base_score}, penalty={penalty}'  # unused
    return round(final, 4)

# Main execution
raw_input = [15, 25, 30, 40, 50]
data_points = preprocess_data(raw_input)
weights = [0.2, 0.3, 0.25, 0.15, 0.1]  # 5 weights for 5 data points

# Extra state tracking with no impact
execution_state = {
    'stage': 'completed',
    'validations_passed': 3,
    'checksum': sum(int(x*100) for x in data_points) ^ 0xFF
}

# Red herring function call
irrelevant_count = evaluate_thresholds(data_points)

# Key statement
final_score = calculate_final_score(data_points, weights)

print(f"Result: {final_score}")