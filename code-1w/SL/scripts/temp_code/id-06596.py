def analyze_metrics(data_set):
    baseline = sum(data_set) / len(data_set)
    adjusted_values = [x * 0.9 + 5 for x in data_set if x > baseline]
    outlier_count = 0
    temp_sum = 0
    for val in adjusted_values:
        if val > 100:
            outlier_count += 1
        temp_sum += val
    
    # Irrelevant tracking variables
    processing_log = set()
    for i in range(len(data_set)):
        if data_set[i] > baseline:
            processing_log.add(f"high_{i}")
        else:
            processing_log.add(f"low_{i}")
    
    average_adjusted = temp_sum / len(adjusted_values) if adjusted_values else 0
    return average_adjusted, outlier_count, processing_log


def validate_entry(record):
    # Dummy validation with string operations
    if isinstance(record, str):
        clean = record.strip().lower()
        return clean.isalnum() and len(clean) > 3
    return False

benchmark_data = [88, 92, 95, 78, 85, 96, 87, 91, 89]

# Misleading pre-processing
raw_total = sum(benchmark_data)
dummy_weights = [1.1, 0.9, 1.0, 1.2, 0.8]
weighted_sum = 0
for i in range(len(benchmark_data)):
    weighted_sum += benchmark_data[i] % 10 * dummy_weights[i % 5]

# Actual logic obscured by noise
primary_avg, anomalies, log_set = analyze_metrics(benchmark_data)

category_map = {k: ('high' if k > 90 else 'medium') for k in benchmark_data}

# Conditional expression with string method distraction
evaluation_status = "valid" if all(validate_entry(str(x)) for x in benchmark_data) else "invalid"
status_flag = evaluation_status.upper().replace("I", "X")  # Red herring

# Core calculation buried in logic
scaling_factor = 1.05 if len(log_set.intersection({f'high_2', f'high_5'})) == 2 else 0.95
preliminary_score = primary_avg * scaling_factor
penalty = 2 * anomalies if anomalies > 0 else 0
final_score = int(preliminary_score - penalty)

# Print required output
print(f"Result: {final_score}")