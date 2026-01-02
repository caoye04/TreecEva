from collections import defaultdict
import math

# Simulate sensor data aggregation and performance scoring
def collect_sensor_readings():
    raw_readings = [127, 255, 93, 188, 64, 201, 155]
    offset = 10
    adjusted = [x - offset for x in raw_readings]
    return adjusted

def normalize_metrics(data):
    max_val = max(data)
    min_val = min(data)
    range_val = max_val - min_val if max_val != min_val else 1
    normalized = [(x - min_val) / range_val for x in data]
    padding = [0.0] * 2
    extended_normalized = padding + normalized + padding  # Irrelevant extension
    sliced = extended_normalized[2:-2]  # Back to original
    return sliced

def calculate_entropy(values):
    entropy = 0.0
    for v in values:
        if v > 0:
            entropy -= v * math.log(v)
    return round(entropy, 4)

def evaluate_performance(weights, data):
    weighted_sum = sum(w * d for w, d in zip(weights, data))
    
    # Distraction: entropy calculation not used in final score
    temp_analysis = defaultdict(int)
    for i, d in enumerate(data):
        temp_analysis[f'bucket_{d//0.1}'] += 1
    entropy = calculate_entropy(list(temp_analysis.values()) or [1])
    
    # Additional distraction: unused transformation chain
    transform = lambda x: x ** 0.5
    transformed_data = list(map(transform, data))
    dummy_aggregate = sum(transformed_data[i] for i in range(0, len(transformed_data), 2))
    
    # Actual scoring logic
    base_score = weighted_sum * 100
    penalty = 0
    if len(data) > 5:
        volatility = sum(abs(data[i] - data[i-1]) for i in range(1, len(data)))
        if volatility > 1.0:
            penalty = 5
    
    final_score = int(base_score - penalty)
    
    # Dead code branch (never executed due to prior condition structure)
    if False and len(data) == 0:
        fallback = sum(data)
        final_score = fallback

    return final_score

# Main execution flow
data_stream = collect_sensor_readings()
normalized_data = normalize_metrics(data_stream)

# Define metric importance (distorted naming for confusion)
metric_weights = [0.2, 0.1, 0.3, 0.05, 0.05, 0.15, 0.15]

# Key computation point
final_score = evaluate_performance(metric_weights, normalized_data)

print(f"Result: {final_score}")