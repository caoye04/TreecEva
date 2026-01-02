def analyze_trend(data, threshold=0.5):
    trend_changes = 0
    prev = data[0]
    for i, val in enumerate(data[1:], 1):
        if val > prev and val > threshold:
            trend_changes += 1
        prev = val
    return trend_changes


def calculate_stability(sequence):
    diffs = [abs(a - b) for a, b in zip(sequence, sequence[1:])]
    avg_diff = sum(diffs) / len(diffs) if diffs else 0
    stability = 1 / (1 + avg_diff)
    return round(stability, 4)


def evaluate_performance(metrics, weights):
    # Normalize metrics
    normalized = [(m - min(metrics)) / (max(metrics) - min(metrics) + 1e-8) for m in metrics]
    
    # Apply weights
    weighted_sum = sum(n * w for n, w in zip(normalized, weights))
    
    # Secondary adjustment based on trend
    trend_metric = analyze_trend([metrics[0], metrics[2], metrics[4]])
    adjustment_factor = 0.9 + (trend_metric * 0.05)
    
    # Stability check (irrelevant to final result but adds cognitive load)
    stability = calculate_stability(metrics)
    temp_debug = stability * 100  # Distractor variable
    
    # Final computation
    raw_score = weighted_sum * adjustment_factor
    ceiling_limit = 100
    floor_limit = 0
    clamped_score = max(floor_limit, min(ceiling_limit, raw_score * 25))  # Scale to 0-100 range
    
    # Additional red herring: unused transformation
    transformed = [x**2 for x in normalized if x > 0.5]
    ignored_result = sum(transformed) // len(transformed) if transformed else 0
    
    # Key assignment
    final_score = int(round(clamped_score))
    return final_score

# Main execution
raw_data = [3, 7, 2, 9, 1]
weights_list = [0.2, 0.3, 0.1, 0.25, 0.15]

# Preprocessing with slicing and string-like distraction (irrelevant)
data_str = ''.join(map(str, raw_data))
reversed_slice = data_str[::-1]
numeric_slice = [int(x) for x in reversed_slice[1::2]]
offset_correction = sum(numeric_slice) % 4  # Not used later

# Actual relevant variables
processed_metrics = [x + offset_correction for x in raw_data]  # Offset doesn't affect relative scaling

# Execute key statement
final_score = evaluate_performance(processed_metrics, weights_list)

# Print result
print(f"Result: {final_score}")