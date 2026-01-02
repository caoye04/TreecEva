def analyze_efficiency(records):
    # Irrelevant data transformation
    temp_stats = [r * 1.07 for r in records if r > 50]
    avg_temp = sum(temp_stats) / len(temp_stats) if temp_stats else 0

    # Decoy calculation with misleading name
    efficiency_index = (avg_temp ** 0.5) * 1.3
    return efficiency_index

# Unused but plausible function
def compute_resilience_factor(x, y):
    base = x ^ y
    shift = (base << 2) & 0xFF
    return shift - 17

# Simulated sensor readings (distractor data)
sensor_logs = [88, 92, 76, 101, 45, 63, 99, 54]
calibration_offset = 3.14159
adjusted_readings = [round(s - calibration_offset) for s in sensor_logs]

# Core data structures
baseline_metrics = {1, 2, 3, 4, 5, 6}
input_stream = [4, 5, 6, 7, 8]
metric_set = set(input_stream)  # Relevant conversion

# Phantom threshold logic (red herring)
threshold_flags = []
for val in input_stream:
    if val > 7:
        threshold_flags.append(True)
    elif val == 5:
        continue  # Dead branch
    else:
        threshold_flags.append(False)

# Fake aggregation
aggregated_weight = 0
for i in range(len(input_stream)):
    if i % 2 == 0:
        aggregated_weight += input_stream[i] * 0.3
    else:
        aggregated_weight -= input_stream[i] * 0.1

# Actual relevant logic buried within distractions
benchmark_data = {
    'weights': [3, 1, 4, 1, 5],
    'mask': {3, 4, 5},
    'offset': 2
}

# Linear search disguised as validation
def find_critical_index(data, target):
    for idx, value in enumerate(data):
        if value == target:
            return idx
    return -1

# Complex evaluation with multiple concepts
def evaluate_performance(metrics, config):
    # Step 1: Set intersection (required feature)
    core_overlap = metrics & config['mask']
    
    # Step 2: Weighted sum with index alignment
    weighted_sum = 0
    for i, w in enumerate(config['weights']):
        if (i + config['offset']) in core_overlap:
            weighted_sum += w * (i + 1)
    
    # Step 3: Conditional adjustment
    adjustment = 0
    if len(core_overlap) >= 2:
        adjustment = find_critical_index(config['weights'], 4) * 2
    
    # Step 4: Final computation
    raw_score = weighted_sum + adjustment
    
    # Step 5: Normalize by overlap size
    normalized_score = raw_score / len(core_overlap) if core_overlap else 0
    
    # Step 6: Add decoy influence (but actually unused)
    decoy_factor = analyze_efficiency(sensor_logs)
    final_score = int(normalized_score + 0.5)  # Round to nearest integer
    
    return final_score

# Execution point of interest
final_score = evaluate_performance(metric_set, benchmark_data)
print(f"Result: {final_score}")