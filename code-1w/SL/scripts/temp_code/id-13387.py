def analyze_system_load(base_load, peak_events):
    # Irrelevant transformation - red herring
    adjusted_load = sum(base_load) * 0.85 + len(peak_events)
    stress_factor = 0
    for event in peak_events:
        if event > 90:
            stress_factor += 1
    # Dead code path - never used
    if stress_factor > 10:
        return -1
    return adjusted_load

# Simulated system telemetry (distraction data)
system_telemetry = [76, 82, 91, 65, 88, 95, 70]
event_spikes = [92, 97, 85, 101, 89]

# Unused but plausible-looking diagnostic function
def compute_health_index(data):
    sorted_data = sorted(data, reverse=True)
    top_three_avg = sum(sorted_data[:3]) / 3
    return round(top_three_avg - len(data) * 0.1, 2)

# Core logic disguised among distractors
def transform_metrics(raw_values):
    processed = []
    for val in raw_values:
        if val >= 80:
            processed.append(val * 1.2)
        elif val >= 60:
            processed.append(val * 1.1)
        else:
            processed.append(val * 0.9)
    return [int(x) for x in processed]

# Bit manipulation decoy
def obfuscate_key(value):
    key = value ^ 0xFF
    key = (key << 2) & 0xFF
    return key | 0x33

# Set-based filtering with meaningful use
def filter_anomalies(data_list):
    all_values = set(data_list)
    outliers = {x for x in all_values if x > 90}
    normal_range = {x for x in all_values if 60 <= x <= 89}
    # Critical intersection determining final behavior
    valid_entries = normal_range.difference(outliers)
    return sorted(list(valid_entries))

# Primary evaluation engine
def evaluate_performance(metrics, benchmark):
    # Step 1: Transform input
    transformed = transform_metrics(metrics)
    
    # Step 2: Filter using set operations
    cleaned = filter_anomalies(transformed)
    
    # Step 3: Compute weighted contributions
    total_weight = 0
    running_score = 0
    
    for idx, val in enumerate(cleaned):
        weight = 1.0 + (idx * 0.1)  # Increasing weight by position
        contribution = val * weight
        running_score += contribution
        total_weight += weight
    
    # Step 4: Normalize
    normalized_score = running_score / total_weight
    
    # Step 5: Apply benchmark offset (critical step)
    adjustment = len(benchmark) - 5
    final_normalized = normalized_score - adjustment * 2.5
    
    # Step 6: Floor to integer (answer determination)
    return int(final_normalized)

# Input datasets
metric_set = [75, 80, 88, 55, 92, 67, 77]
benchmark_data = [10, 20, 30, 40, 50, 60]

# Distraction variables
temp_analysis = analyze_system_load(system_telemetry, event_spikes)
diagnostic_code = obfuscate_key(42)
baseline_check = compute_health_index([70, 75, 80])

# Actual execution point of interest
final_score = evaluate_performance(metric_set, benchmark_data)

# Output result as required
print(f"Result: {final_score}")