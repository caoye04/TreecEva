def analyze_temperature_readings(readings):
    warnings = []
    corrected = []
    outlier_threshold = 50
    adjustment_factor = 0.9
    
    for i, val in enumerate(readings):
        if abs(val) > outlier_threshold:
            warnings.append(f'High variance at index {i}')
            corrected.append(val * adjustment_factor)
        else:
            corrected.append(val)
    
    return corrected, warnings


def filter_and_aggregate(data, min_val=-10):
    filtered = [x for x in data if x >= min_val]
    total = sum(filtered)
    count = len(filtered)
    average = total / count if count > 0 else 0
    return average, filtered

# Simulate sensor drift correction
drift_compensation = lambda x, rate: [val + rate * i for i, val in enumerate(x)]

# Raw temperature data from sensors (in °C)
raw_readings = [3, -5, 67, 23, -15, 44, 8, 12, -8, 55]

# Apply drift compensation (simulated)
compensated_readings = drift_compensation(raw_readings, 0.5)

# Analyze and correct outliers
corrected_readings, alerts = analyze_temperature_readings(compensated_readings)

# Filter invalid readings and compute base average
base_average, valid_data = filter_and_aggregate(corrected_readings, min_val=-10)

# Additional processing: normalize around mean
mean_value = base_average
normalized = [round(x - mean_value, 2) for x in valid_data]

# Map normalized values with zip and enumerate to track shifts
shift_map = {}
for idx, (orig, norm) in enumerate(zip(valid_data, normalized)):
    shift_map[idx] = {'original': orig, 'shift': norm}

# Calculate dynamic weight based on position
weights = [0.8 + (i * 0.05) for i in range(len(normalized))]
weighted_sum = sum(n * w for n, w in zip(normalized, weights))

# Prepare processed data structure
processed_data = {
    'values': normalized,
    'total_shift': weighted_sum,
    'size': len(normalized),
    'baseline': mean_value
}

# Dummy function to simulate redundant computation
def compute_redundant_metrics(data):
    peak = max(data['values'], default=0)
    trough = min(data['values'], default=0)
    volatility = peak - trough
    phantom_metric = volatility * 0.1  # Unused later
    return volatility  # Not used in final path

# Irrelevant sorting operation (distractor)
sorted_values = sorted(processed_data['values'], reverse=True)
secondary_ranking = [v * 1.1 for v in sorted_values if v > 0]

# Core logic hidden among distractions
def calculate_adjusted_score(dataset):
    raw_shift = dataset['total_shift']
    n = dataset['size']
    base = dataset['baseline']
    
    # Actual score formula
    adjustment = 1 + (n * 0.01)
    score_component_1 = raw_shift * adjustment
    score_component_2 = base * 0.2
    
    # Final deterministic calculation
    final_score = score_component_1 + score_component_2
    
    # Dead code branch (never executed)
    if False:
        final_score -= 999  # Red herring
    
    return final_score

# Execute key statement
final_score = calculate_adjusted_score(processed_data)

print(f"Result: {final_score}")