from collections import defaultdict
from itertools import cycle

# Simulate sensor data stream with noise and valid readings
def generate_sensor_data():
    raw_values = [105, 98, 112, None, 103, 115, 97, None, 109, 111]
    timestamps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return list(zip(timestamps, raw_values))

# Process sensor stream and extract quality metrics
def analyze_readings(data_stream):
    stats = defaultdict(int)
    clean_readings = []
    spike_count = 0
    base_reference = 100
    cumulative_deviation = 0.0

    for ts, val in data_stream:
        if val is None:
            stats['missing'] += 1
            continue
        
        clean_readings.append(val)
        deviation = abs(val - base_reference)
        cumulative_deviation += deviation
        
        if deviation > 10:
            spike_count += 1

        if val > base_reference:
            stats['above_baseline'] += 1
        else:
            stats['at_or_below'] += 1

    # Distractor computation: entropy-like measure (not used in final score)
    entropy_proxy = 0.0
    for x in clean_readings:
        if x > 0:
            entropy_proxy -= (x / sum(clean_readings)) * (x / sum(clean_readings))

    # Additional irrelevant tracking
    rolling_averages = [sum(clean_readings[i:i+3]) / 3 
                        for i in range(len(clean_readings) - 2)]
    stats['smoothed_count'] = len(rolling_averages)

    # Key metrics for evaluation
    accuracy_metric = len(clean_readings) - spike_count
    consistency_metric = len(clean_readings) - stats['missing']
    stability_metric = int(cumulative_deviation)

    return {
        'accuracy': accuracy_metric,
        'consistency': consistency_metric,
        'stability': stability_metric,
        'spikes': spike_count,
        'readings_count': len(clean_readings)
    }

# Evaluate system performance based on weighted metrics
def evaluate_performance(metrics, weights):
    temp_result = 0
    weight_sum = sum(weights.values())
    
    # Normalize weights
    normalized_weights = {k: v / weight_sum for k, v in weights.items()}
    
    # Apply weights (only some are actually impactful)
    for key in metrics:
        if key in normalized_weights:
            temp_result += metrics[key] * normalized_weights[key]
    
    # Red herring: transform via bitwise then revert
    temp_encoded = temp_result ^ 255
    temp_decoded = temp_encoded ^ 255
    
    # Extra distraction: simulate time decay factor (constant here)
    time_factor = 1.0
    for _ in range(2):
        time_factor *= 0.99
    
    # Final score calculation — only temp_decoded matters
    final_score = int(temp_decoded * time_factor)  # time_factor ~0.98, but cast to int
    
    # Unused derived variables to increase cognitive load
    efficiency_ratio = final_score / (metrics['readings_count'] + 1)
    reliability_index = (metrics['consistency'] - metrics['spikes']) * 2
    
    return final_score

# Main execution flow
data_feed = generate_sensor_data()
processed_metrics = analyze_readings(data_feed)

# Weight configuration (some weights are zero, adding confusion)
weights_config = {
    'accuracy': 0.4,
    'consistency': 0.4,
    'stability': 0.2,
    'spikes': 0.0,  # This has no effect
    'readings_count': 0.0  # Also irrelevant
}

final_score = evaluate_performance(processed_metrics, weights_config)
print(f"Target result: {final_score}")