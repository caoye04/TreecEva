from collections import defaultdict

# Simulate sensor data aggregation and anomaly filtering
def collect_sensor_data():
    raw_data = [15, 23, 18, 47, 29, 31, 22]
    timestamps = list(range(1000, 1007))
    sensor_map = defaultdict(list)
    for t, val in zip(timestamps, raw_data):
        sensor_map['A'].append((t, val))
    return dict(sensor_map)

# Filter anomalies using simple statistical threshold (mean ± 2σ)
def filter_anomalies(data_list):
    values = [v for _, v in data_list]
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    lower, upper = mean_val - 2 * std_dev, mean_val + 2 * std_dev
    
    # Misleading intermediate: counting filtered elements (not used later)
    filtered_count = 0
    cleaned = []
    for item in data_list:
        if lower <= item[1] <= upper:
            cleaned.append(item)
        else:
            filtered_count += 1  # Distractor: not used in final logic
    
    # Extra computation: sort by timestamp (redundant since already sorted)
    cleaned.sort(key=lambda x: x[0])
    return [v for _, v in cleaned]

# Apply dynamic weighting based on signal stability
def compute_weights(sequence):
    diffs = [abs(sequence[i+1] - sequence[i]) for i in range(len(sequence)-1)]
    avg_change = sum(diffs) / len(diffs) if diffs else 0
    
    # Simulate adaptive sensitivity
    weight_map = defaultdict(float)
    weight_map['base'] = 0.8
    weight_map['stability_factor'] = 1.0 - min(avg_change / 10.0, 0.7)
    weight_map['final_adjustment'] = 0.95
    
    # Dead code path: never executed but adds confusion
    if len(sequence) > 100:
        weight_map['overhead_penalty'] = 0.1
    
    return [weight_map['base'], weight_map['stability_factor'], weight_map['final_adjustment']]

# Core processing function combining multiple metrics
def process_results(metrics, weights):
    # metrics contains various processed values
    base_metric = metrics['clean_mean']
    trend_metric = metrics['trend_strength']
    noise_level = metrics['residual_noise']

    # Weighted combination
    weighted_sum = base_metric * weights[0]
    weighted_sum += trend_metric * weights[1] * 1.1  # Emphasis on trend
    weighted_sum -= noise_level * weights[2] * 0.3  # Penalty for noise

    # Intermediate transformation with distractors
    temp_offset = 5.5
    adjustment_cycle = 3
    if adjustment_cycle > 2:
        temp_offset *= 0.9  # Minor tweak

    weighted_sum += temp_offset  # Add fixed offset

    # Additional irrelevant bit manipulation (distractor)
    magic_flag = 0b1010 ^ 0b1100  # XOR operation with no effect
    magic_flag <<= 2
    magic_flag |= 0b11

    # Final non-linear scaling
    final_score = int((weighted_sum ** 1.05) + 0.5)
    return final_score

# Main execution flow
data_blocks = collect_sensor_data()
signal_stream = filter_anomalies(data_blocks['A'])

# Derive key metrics from cleaned data
metrics = {}
metrics['clean_mean'] = sum(signal_stream) / len(signal_stream)
trend_diffs = [signal_stream[i+1] - signal_stream[i] for i in range(len(signal_stream)-1)]
metrics['trend_strength'] = abs(sum(t for t in trend_diffs if t > 0))
metrics['residual_noise'] = sum(x % 3 for x in signal_stream)  # Artificial noise measure

# Compute adaptive weights
weights = compute_weights(signal_stream)

# Critical statement
final_score = process_results(metrics, weights)

# Print result as required
print(f"Result: {final_score}")