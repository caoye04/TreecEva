import math

# Simulate sensor data stream with noise and valid readings
def generate_sensor_stream():
    raw_values = [23.5, 19.0, 25.3, -999, 27.1, 22.0, -999, 28.4, 26.7, 24.0]
    return list(map(lambda x: x if x != -999 else None, raw_values))

# Noise filter using median thresholding
def calculate_median(values):
    filtered = [v for v in values if v is not None]
    sorted_vals = sorted(filtered)
    n = len(sorted_vals)
    return sorted_vals[n // 2] if n % 2 == 1 else (sorted_vals[n//2 - 1] + sorted_vals[n//2]) / 2

# Apply dynamic threshold to detect anomalies
def filter_anomalies(data, base_threshold):
    median_val = calculate_median(data)
    upper_bound = median_val + base_threshold
    lower_bound = median_val - base_threshold
    clean_data = []
    anomaly_count = 0
    for val in data:
        if val is not None and lower_bound <= val <= upper_bound:
            clean_data.append(val)
        else:
            clean_data.append(None)
            anomaly_count += 1
    return clean_data, anomaly_count

# Transform data using nonlinear scaling
def nonlinear_transform(values):
    transformed = []
    for v in values:
        if v is not None:
            # Apply logarithmic compression for dynamic range control
            compressed = math.log(v - 18.0) if v > 18.0 else 0.1
            scaled = compressed * 10
            transformed.append(round(scaled, 3))
        else:
            transformed.append(None)
    return transformed

# Aggregate function with weighted average
def compute_weighted_average(data):
    weights = [1, 1.2, 1.3, 1.1, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5][:len(data)]
    total, weight_sum = 0.0, 0.0
    for i, val in enumerate(data):
        if val is not None:
            total += val * weights[i]
            weight_sum += weights[i]
    return round(total / weight_sum, 3) if weight_sum > 0 else 0.0

# Secondary calculation - irrelevant to final output (distractor)
def compute_entropy(data):
    from collections import Counter
    counts = Counter([round(d) for d in data if d is not None])
    total = sum(counts.values())
    entropy = -sum((count/total) * math.log2(count/total) for count in counts.values())
    return round(entropy, 3)

# Main processing pipeline
def process_data(buffer, filters):
    temp_data = buffer.copy()
    
    # Apply multiple filtering stages (only last one matters)
    for f_type in filters:
        if f_type == 'threshold':
            temp_data, _ = filter_anomalies(temp_data, 3.5)
        elif f_type == 'transform':
            temp_data = nonlinear_transform(temp_data)
        elif f_type == 'smooth':  # Dead code path - never used
            temp_data = [x if x is None else x * 0.95 for x in temp_data]
    
    # Final aggregation
    aggregate_result = compute_weighted_average(temp_data)
    
    # Distractor variables (not used in final result)
    backup_snapshot = temp_data.copy()
    max_value = max([x for x in temp_data if x is not None], default=0)
    min_value = min([x for x in temp_data if x is not None], default=0)
    range_spread = max_value - min_value
    
    # Final output depends only on aggregated result
    scaling_factor = 2.5
    final_output = int(aggregate_result * scaling_factor)  # Key statement
    
    return final_output

# Irrelevant helper (dead code)
def debug_print_structure(obj):
    print(f"Object type: {type(obj)}")

# Execution flow
stream_buffer = generate_sensor_stream()
filters = ['threshold', 'transform']  # Note: 'smooth' would be ignored due to logic
intermediate_stats = {'count': len([x for x in stream_buffer if x is not None])}
entropy_diagnostic = compute_entropy([x for x in stream_buffer if x is not None])  # Distractor call

final_output = process_data(stream_buffer, filters)
print(f"Result: {final_output}")