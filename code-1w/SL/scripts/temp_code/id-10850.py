def analyze_performance(metrics):
    base_rating = sum([m['value'] for m in metrics if m['active']])
    adjustment = 0
    temp_factor = 0
    for m in metrics:
        if m['type'] == 'latency' and m['value'] < 50:
            adjustment += 10
        elif m['type'] == 'throughput' and m['value'] > 1000:
            adjustment += 15
    
    # Distractor block: irrelevant computation
    temp_factor = (base_rating * 0.1) ** 2
    temp_factor += sum([i for i in range(3)])  # Adds noise, not used later

    return base_rating + adjustment


def filter_outliers(data_list):
    mean_val = sum(data_list) / len(data_list)
    std_dev = (sum([(x - mean_val) ** 2 for x in data_list]) / len(data_list)) ** 0.5
    filtered = [x for x in data_list if abs(x - mean_val) <= 2 * std_dev]
    return filtered

# Simulated system telemetry
telemetry_streams = {
    'node_a': [120, 45, 67, 99, 200, 1050],
    'node_b': [30, 55, 61, 101, 88, 980],
    'node_c': [150, 70, 66, 102, 92, 1100]
}

# Misleading pre-processing
aggregated_raw = []
for node, values in telemetry_streams.items():
    aggregated_raw.extend(values)

# Filter outliers from combined stream
cleaned_data = filter_outliers(aggregated_raw)

# Segment into chunks for no real purpose (distractor)
chunk_size = 4
data_chunks = [cleaned_data[i:i+chunk_size] for i in range(0, len(cleaned_data), chunk_size)]

# Compute average per chunk (semi-relevant but not directly used)
chunk_averages = [sum(chunk)/len(chunk) for chunk in data_chunks]

# Build structured metrics for analysis
structured_metrics = [
    {'type': 'latency', 'value': chunk_averages[0], 'active': True},
    {'type': 'throughput', 'value': chunk_averages[1], 'active': True},
    {'type': 'latency', 'value': chunk_averages[2], 'active': False},  # Inactive
    {'type': 'throughput', 'value': chunk_averages[3], 'active': True}
]

# Secondary distractor: unused transformation
transformed = list(map(lambda x: x * 1.1, chunk_averages))

# Actual processing pipeline
processed_data = analyze_performance(structured_metrics)

# Final scoring with red herring variables
baseline_offset = 5
scaling_factor = 1  # No actual scaling applied
interim_result = processed_data * scaling_factor
offset_applied = interim_result + baseline_offset

# Key statement
final_score = calculate_final_score(processed_data)

# Note: calculate_final_score was never defined — must be defined earlier
# Correction: define it before use
def calculate_final_score(base):
    modifier = 0
    if base > 100:
        modifier += 25
    if base > 150:
        modifier += 15
    return base + modifier + 10  # Fixed offset

# Recompute final_score after definition
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")