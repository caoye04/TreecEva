def analyze_sensor_readings(readings):
    normalized = []
    offset = 0.1
    scaling_factor = 1.5
    
    for i, val in enumerate(readings):
        adjusted = (val + offset) * scaling_factor
        normalized.append(round(adjusted, 3))
    
    return normalized


def filter_outliers(data, threshold=2.0):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5
    filtered = [x for x in data if abs(x - mean) <= threshold * std_dev]
    
    # Distractor: unused outlier count
    outlier_count = len(data) - len(filtered)
    temp_debug_info = {'original_count': len(data), 'filtered_count': len(filtered)}
    
    return filtered


def calculate_optimal_yield(dataset):
    sorted_data = sorted(dataset)
    mid_index = len(sorted_data) // 2
    median_val = (sorted_data[mid_index] + sorted_data[~mid_index]) / 2
    
    # Simulate efficiency curve with decay factor
    decay_factor = 0.95
    efficiency_sequence = []
    cumulative_efficiency = 0
    
    for i in range(len(sorted_data)):
        raw_eff = sorted_data[i] / (i + 1) if i > 0 else sorted_data[0]
        decayed_eff = raw_eff * (decay_factor ** i)
        efficiency_sequence.append(decayed_eff)
        cumulative_efficiency += decayed_eff
    
    avg_efficiency = cumulative_efficiency / len(efficiency_sequence)
    peak = max(sorted_data)
    
    # Secondary distractor computation (not used in final result)
    harmonic_mean = len(sorted_data) / sum(1/x for x in sorted_data)
    geometric_mean = (1)
    for x in sorted_data:
        geometric_mean *= x
    geometric_mean = geometric_mean ** (1/len(sorted_data))
    
    # Final yield depends only on median and average efficiency
    yield_score = (median_val * 0.6) + (avg_efficiency * 0.4)
    return round(yield_score, 4)

# Main execution block
sensor_inputs = [0.88, 1.02, 0.94, 1.15, 0.81, 1.23, 0.77, 1.09, 0.99, 1.01, 0.85, 1.11]

# Step 1: Normalize sensor readings
processed_data = analyze_sensor_readings(sensor_inputs)

# Step 2: Remove statistical outliers
cleaned_data = filter_outliers(processed_data, threshold=1.8)

# Step 3: Compute derived metrics (some redundant)
data_stats = {}
data_stats['min'] = min(cleaned_data)
data_stats['max'] = max(cleaned_data)
data_stats['range'] = data_stats['max'] - data_stats['min']
data_stats['sum'] = sum(cleaned_data)

# Distractor loop: zipped iteration that doesn't affect outcome
tracking_log = []
for idx, (orig, clean) in enumerate(zip(sensor_inputs, cleaned_data[:len(sensor_inputs)])):
    diff = abs(clean - orig)
    tracking_log.append((idx, diff))

# Additional irrelevant state tracking
state_flags = {"calibrated": True, "mode": "high_res", "version": 2}
temp_aggregates = [sum(pair) for pair in zip(cleaned_data, cleaned_data[1:])]

# Key statement
final_yield = calculate_optimal_yield(cleaned_data)
print(f"Result: {final_yield}")