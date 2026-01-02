from itertools import compress, cycle

# Simulate sensor array readings with noise filtering and performance evaluation
def analyze_sensor_data(readings, thresholds):
    filtered = [r for r in readings if r >= thresholds[0]]
    normalized = [(f - min(filtered)) / (max(filtered) - min(filtered) + 1e-5) for f in filtered]
    
    # Irrelevant transformation (distractor)
    inverted = [1 - n for n in normalized]
    smoothed = [sum(normalized[i:i+3]) / 3 for i in range(len(normalized) - 2)] if len(normalized) > 2 else normalized
    
    return normalized, smoothed, inverted

def calculate_stability(data):
    diffs = [abs(data[i] - data[i-1]) for i in range(1, len(data))]
    stability = sum(diffs) / len(diffs) if diffs else 0.0
    return round(stability, 4)

def evaluate_performance(weights, outcomes):
    # Mix relevant and irrelevant operations
    base = sum(o * w for o, w in zip(outcomes, weights))
    adjustment = len([o for o in outcomes if o > 0.5]) * 0.1
    
    # Dummy calculation with no effect (dead code path)
    temp_result = None
    if False:
        temp_result = [o ** 2 for o in outcomes if o < 0.3]
    
    final_score = base + adjustment
    
    # Extra assignment to mislead (irrelevant)
    derived_metrics = {'score': final_score, 'bonus': adjustment}
    
    return final_score

# Main execution block
sensor_readings = [0.1, 0.4, 0.7, 0.3, 0.9, 0.6, 0.8, 0.2, 0.5]
thresholds = [0.25, 0.75]

# Preprocess step with multiple outputs (only first used)
primary_data, _, _ = analyze_sensor_data(sensor_readings, thresholds)

stability_index = calculate_stability(primary_data)

# Weighting factors for performance (domain-specific tuning)
metric_weights = [0.3, 0.5, 0.2]
raw_outcomes = [stability_index] + primary_data[:2]  # Composite input vector

# Key statement
final_score = evaluate_performance(metric_weights, raw_outcomes)

print(f"Result: {final_score}")