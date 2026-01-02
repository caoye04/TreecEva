def analyze_workload(entries):
    total_items = sum([e['count'] for e in entries])
    weighted_load = 0
    temp_factor = 0
    
    for entry in entries:
        load = entry['count'] * entry['complexity']
        if load > 50:
            temp_factor += 1
        weighted_load += load

    average_load = weighted_load / len(entries) if entries else 0
    adjustment = 1.0
    
    # Distractor: irrelevant temperature simulation
    temperature_buffer = []
    for i in range(3):
        temperature_buffer.append((i + 1) * 0.1)
    avg_temp = sum(temperature_buffer) / len(temperature_buffer) if temperature_buffer else 0

    normalized_load = min(weighted_load / 100.0, 10)
    return total_items, normalized_load, average_load


def filter_noisy_data(raw_samples):
    filtered = [s for s in raw_samples if s > 0.5]
    outlier_count = len([s for s in raw_samples if s < 0.1])
    # Dead code path - never used
    if outlier_count > 10:
        adjustment_flag = True
    return set(filtered)

def compute_efficiency(data, limit):
    base_score = 0
    penalty = 0
    
    for val in data:
        if val > limit:
            base_score += val * 2
        else:
            base_score += val
    
    # Apply diminishing returns using floor division
    if base_score > 100:
        penalty = base_score // 10
    
    final_score = base_score - penalty
    
    # Red herring computation
    debug_ratio = (base_score + 1) / (penalty + 1) if penalty > 0 else 0
    
    return int(final_score)

# Main execution
work_entries = [
    {'count': 8, 'complexity': 7},
    {'count': 12, 'complexity': 6},
    {'count': 5, 'complexity': 9},
    {'count': 15, 'complexity': 4}
]

raw_sensor_data = [0.8, 0.6, 0.9, 0.4, 0.7, 0.55, 0.3, 0.85, 0.2, 0.75]
threshold = 6.0

# Step 1: Analyze workload
item_count, norm_load, avg_load = analyze_workload(work_entries)

# Step 2: Filter sensor readings
valid_readings = filter_noisy_data(raw_sensor_data)

# Step 3: Prepare processed data using slicing and transformations
extended_readings = list(valid_readings) + [norm_load, avg_load]
sorted_data = sorted(extended_readings)
processed_data = sorted_data[1:-1]  # Slice to remove extremes

# Key statement
efficiency_score = compute_efficiency(processed_data, threshold)

# Print result
print(f"Result: {efficiency_score}")