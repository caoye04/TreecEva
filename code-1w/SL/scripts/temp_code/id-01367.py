import itertools

# Simulated sensor data processing with noise filtering and diagnostic evaluation
def collect_sensor_readings():
    raw_samples = [105, 92, 110, 88, 97, 103, 85, 95, 100, 90]
    noise_floor = 85
    filtered_readings = [x for x in raw_samples if x > noise_floor]
    return filtered_readings

# Secondary irrelevant function - decoy for power analysis
def calculate_power_profile(readings):
    baseline = 1.8
    adjustments = []
    for val in readings:
        if val > 100:
            adjustments.append(baseline * 1.15)
        elif val > 90:
            adjustments.append(baseline * 1.05)
        else:
            adjustments.append(baseline)
    total_power = sum(adjustments)
    avg_power = total_power / len(adjustments) if adjustments else 0
    return round(avg_power, 3)

# Unused transformation - dead code path (red herring)
def transform_to_frequency_domain(signal):
    transformed = []
    for i in range(len(signal)):
        component = 0
        for j, val in enumerate(signal):
            component += val * (i + 1) * (j % 3 + 1)
        transformed.append(component % 1000)
    return transformed

# Core logic: signal quality analysis
def evaluate_stability_metrics(data):
    if len(data) < 3:
        return 0
    
    # Compute moving differences
    diffs = [abs(data[i] - data[i-1]) for i in range(1, len(data))]
    avg_diff = sum(diffs) / len(diffs)
    peak_variation = max(diffs)
    
    # Stability score based on variation
    stability_score = 100 - (avg_diff * 2) - (peak_variation * 0.5)
    return int(stability_score)

# Complex conditional aggregation using itertools
def group_and_evaluate(readings):
    sorted_vals = sorted(readings, reverse=True)
    high_group = list(itertools.takewhile(lambda x: x >= 100, sorted_vals))
    mid_group = list(itertools.dropwhile(lambda x: x >= 100, sorted_vals))
    mid_filtered = list(itertools.filterfalse(lambda x: x < 90, mid_group))
    
    # Misleading intermediate metric
    compression_ratio = len(high_group) / len(readings) if readings else 0
    
    # Real signal relevance: count of consistent high performers
    consistency_count = 0
    for a, b in itertools.pairwise(high_group):
        if abs(a - b) <= 5:
            consistency_count += 1
    
    return consistency_count, compression_ratio  # second return value is distraction

# Main diagnostic analyzer
def analyze_signal_quality(buffer):
    # Irrelevant pre-checks (distractors)
    if not buffer:
        return -1
    
    temp_adjustment = 0
    for val in buffer:
        if val in [88, 92, 105]:
            temp_adjustment += 0.5  # meaningless accumulation
    
    # Actual key computations
    base_score = sum(buffer) // len(buffer)  # integer average
    stability = evaluate_stability_metrics(buffer)
    
    # Extract consistency metric
    consistency, _ = group_and_evaluate(buffer)
    
    # Apply weighted fusion (core formula)
    diagnostic_value = base_score + stability + (consistency * 10)
    
    # Red herring: unused threshold check
    if diagnostic_value > 250:
        flag_mode = 'OVERDRIVE'
    else:
        flag_mode = 'STANDARD'
    
    # Final adjustment based on parity (hidden rule)
    if len(buffer) % 2 == 1:
        diagnostic_value -= 7
    else:
        diagnostic_value += 3
    
    return diagnostic_value

# --- Execution Flow ---
sensor_data = collect_sensor_readings()

# Decoy usage of itertools
paired_combinations = list(itertools.combinations(sensor_data, 2))
mean_pairs = [sum(pair)/2 for pair in paired_combinations]
median_proxy = sorted(mean_pairs)[len(mean_pairs)//2] if mean_pairs else 0

# Power profile calculation - irrelevant but plausible
power_usage = calculate_power_profile(sensor_data)

# Frequency domain transformation - dead end
frequency_components = transform_to_frequency_domain(sensor_data)

# Key execution point
final_diagnostic = analyze_signal_quality(sensor_data)

# Output result
print(f"Result: {final_diagnostic}")