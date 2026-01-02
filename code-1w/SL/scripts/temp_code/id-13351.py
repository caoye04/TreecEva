def analyze_trend(values):
    trend = 0
    changes = []
    for i in range(1, len(values)):
        delta = values[i] - values[i-1]
        changes.append(delta)
        if delta > 0:
            trend += 1
        elif delta < 0:
            trend -= 1
    return trend

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return x * x + 2*x - 1

# Simulate sensor data with noise filtering
def filter_noisy_data(raw):
    filtered = [x for x in raw if abs(x - sum(raw)/len(raw)) < 2*sum(raw)/len(raw)*0.1]
    baseline = sum(filtered) / len(filtered) if filtered else 0
    adjusted = [x - baseline for x in filtered]
    return adjusted

# Main processing pipeline
def calculate_final_score(data, weights):
    # Step 1: Normalize data
    normalized = [d / sum(data) for d in data]
    
    # Step 2: Apply weights (element-wise multiplication)
    weighted_vals = [n * w for n, w in zip(normalized, weights)]
    
    # Step 3: Compute derived metrics (some are distractions)
    avg_weighted = sum(weighted_vals) / len(weighted_vals)
    squared_sum = sum([v**2 for v in weighted_vals])
    penalty_factor = 0.1 * len([v for v in weighted_vals if v < 0.05])  # Penalty for small contributions
    
    # Step 4: Trend analysis on weights (semi-relevant)
    weight_trend = analyze_trend(weights)
    trend_boost = 1 + (weight_trend / len(weights)) * 0.05
    
    # Step 5: Accumulate score components
    base_score = sum(weighted_vals)
    bonus = 0
    if avg_weighted > 0.1:
        bonus += 5
    if squared_sum > 0.02:
        bonus += 3
    
    # Step 6: Final calculation
    final_score = (base_score - penalty_factor) * trend_boost + bonus
    
    # Distraction variables
    temp_debug = [unused_helper(int(v)) for v in weighted_vals]
    metadata_log = {'entries': len(data), 'adjustments': penalty_factor, 'trend_shift': weight_trend}
    
    return final_score

# Input data
sensor_readings = [105, 210, 190, 208, 102]
importance_weights = [0.8, 1.2, 0.9, 1.1, 0.7]

# Filter and preprocess (irrelevant to final result but adds cognitive load)
processed_data = filter_noisy_data(sensor_readings)
scaled_weights = [w * 1.0 for w in importance_weights]  # Redundant scaling

# Execute main logic
distorted_inputs = [x * 0.99 for x in processed_data]  # Not used
final_score = calculate_final_score(sensor_readings, importance_weights)

print(f"Result: {final_score}")