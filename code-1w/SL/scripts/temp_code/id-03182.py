from collections import defaultdict

# Simulate system diagnostics with performance metrics
def analyze_system_load(log_entries):
    frequency_map = defaultdict(int)
    temp_buffer = []
    total_load = 0
    peak_moment = 0

    for entry in log_entries:
        component, load_str = entry.split(':')
        load_val = int(load_str)
        frequency_map[component] += 1
        total_load += load_val

        if load_val > peak_moment:
            peak_moment = load_val

        if load_val > 80:
            temp_buffer.append(component)

    # Irrelevant aggregation (distractor)
    avg_load = total_load / len(log_entries) if log_entries else 0
    high_load_components = set(temp_buffer)

    return total_load, avg_load, frequency_map

# Evaluate processing efficiency
def calculate_efficiency(monitor_data):
    efficiency = 0
    transient_sum = 0
    cycle_count = 0

    for i, reading in enumerate(monitor_data):
        if i % 2 == 0 and reading > 0:
            efficiency += reading * (i + 1)
        else:
            transient_sum += reading
        cycle_count += 1

    # Fake normalization (not used later)
    if cycle_count > 0:
        normalized = transient_sum / cycle_count
    else:
        normalized = 0

    return efficiency

# Assess error patterns
def categorize_errors(error_stream):
    error_catalog = {}
    buffer_dict = {}
    total_errors = 0

    for code, timestamp in error_stream:
        total_errors += 1
        if code not in error_catalog:
            error_catalog[code] = 0
        error_catalog[code] += 1

        key = f"err_{code}"
        buffer_dict[key] = buffer_dict.get(key, 0) + 1

    # Dead code path (distractor)
    if total_errors == 0:
        safe_mode = True
    elif total_errors < 5:
        safe_mode = False
    else:
        safe_mode = False

    return error_catalog, total_errors

# Main evaluation logic
def evaluate_performance(metrics, logs):
    base_score = metrics * 1.5
    penalty = 0

    for level, count in logs.items():
        if count > 2:
            penalty += level * count * 0.1

    final_score = base_score - penalty
    return round(final_score, 4)

# Input data (simulated sensor readings and logs)
logs = [
    "cpu:95", "gpu:70", "cpu:85", "ram:60", "disk:45",
    "cpu:90", "gpu:75", "network:30", "cpu:88", "gpu:72"
]

monitor_data = [12, 15, 0, 18, 22, 5, 10]
error_events = [(404, 162345), (500, 162348), (404, 162352), (403, 162355), (404, 162360)]

# Step 1: Analyze system load
total, average, freq = analyze_system_load(logs)

# Step 2: Calculate efficiency from monitor
efficiency = calculate_efficiency(monitor_data)

# Step 3: Categorize errors
errors_by_type, total_err = categorize_errors(error_events)

# Step 4: Compute derived metric
weighted_metric = efficiency / (total_err + 1) if total_err > 0 else efficiency

# Step 5: Prepare for final scoring
stability_index = total / (len(logs) + 1)
diagnostic_trace = {k: v for k, v in freq.items() if v >= 2}

# Step 6: Final performance evaluation
final_score = evaluate_performance(efficiency, errors_by_type)

print(f"Result: {final_score}")