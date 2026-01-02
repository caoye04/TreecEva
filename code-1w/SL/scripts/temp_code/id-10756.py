from collections import defaultdict

# Simulate system performance metrics over time
def collect_metrics():
    data = [120, 85, 90, 100, 110, 95, 130]
    outliers = []
    avg = sum(data) / len(data)
    for x in data:
        if abs(x - avg) > 20:
            outliers.append(x)
    return data, outliers

def normalize(value, min_val, max_val):
    if max_val == min_val:
        return 0.5
    return (value - min_val) / (max_val - min_val)

def calculate_trend(values):
    trend = 0
    for i in range(1, len(values)):
        trend += values[i] - values[i-1]
    return trend  # Irrelevant for final score but adds computation

def evaluate_performance(raw_metrics, weights):
    # Initialize containers
    processed = defaultdict(float)
    temp_buffer = []
    
    # Normalize metrics (only first four are used in final calculation)
    relevant_metrics = raw_metrics[:4]
    min_m, max_m = min(relevant_metrics), max(relevant_metrics)
    
    for i, val in enumerate(relevant_metrics):
        normalized = normalize(val, min_m, max_m)
        processed[f'metric_{i}'] = normalized
        temp_buffer.append(normalized * 2)  # Distractor: extra processing
    
    # Weighted sum using only the first four
    weighted_sum = 0.0
    for i, key in enumerate(processed.keys()):
        weighted_sum += processed[key] * weights[i]
    
    # Additional logic that looks important but doesn't affect result
    if len(raw_metrics) > 5:
        growth = calculate_trend(raw_metrics)
        adjustment = growth * 0.01  # Computed but unused
    
    final_score = int(weighted_sum * 100)  # Critical assignment
    
    # Dead code path (never executed under normal inputs)
    if False:
        fallback = sum(temp_buffer) / len(temp_buffer)
        final_score = int(fallback * 10)
    
    return final_score

# Main execution
metrics, outlier_list = collect_metrics()
scale_weights = [0.2, 0.3, 0.25, 0.25]  # Sum to 1.0

# Extraneous variable
system_load = sum(metrics) * 0.01

final_score = evaluate_performance(metrics, scale_weights)
print(f"Result: {final_score}")