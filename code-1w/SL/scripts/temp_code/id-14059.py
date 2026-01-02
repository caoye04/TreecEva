import math

# Simulated sensor fusion system for environmental monitoring

# === Real data inputs (relevant) ===
raw_readings = [32, 18, 25, 45, 28, 37, 21, 33]
threshold = 30
sample_weights = [0.8, 1.1, 0.9, 1.3, 1.0, 1.2, 0.7, 1.0]

# === Irrelevant variables (distractors) ===
baseline_calibration = [0.5, 0.6, 0.4, 0.7, 0.5]  # unused in final logic
temp_unit = 'Celsius'
system_uptime_hours = 127
maintenance_log = {'status': 'ok', 'last_check': '2023-08-01'}
scaling_factor = 2.718  # never applied

# === Preprocessing function with red herrings ===
def preprocess_sensors(data, weights):
    weighted_sum = 0
    total_weight = 0
    adjusted_values = []
    
    for i in range(len(data)):
        if i % 3 == 0:
            # Dummy transformation that doesn't affect outcome
            anomaly_score = (data[i] * 1.5) % 7
        elif i == 4:
            # Dead code path
            normalized = data[i] / max(data)
        else:
            # Actual processing branch
            adjusted = data[i] * weights[i]
            adjusted_values.append(adjusted)
            weighted_sum += adjusted
            total_weight += weights[i]
    
    mean_adjusted = weighted_sum / total_weight if total_weight > 0 else 0
    return adjusted_values, mean_adjusted

# === Auxiliary function (decoy) ===
def compute_entropy(values):
    # This function is defined but not used in critical path
    prob_dist = {}
    total = sum(values)
    for v in values:
        p = v / total
        prob_dist[v] = p
    entropy = -sum(p * math.log(p) for p in prob_dist.values())
    return round(entropy, 4)

# === Core analysis with mixed concepts ===
def filter_high_impact(readings, limit):
    high_impact = []
    indices = set()
    for idx, val in enumerate(readings):
        if val > limit:
            high_impact.append(val)
            indices.add(idx)
    return high_impact, indices

# === Data structure transformation layer ===
def build_summary_table(raw, processed, threshold):
    summary = {}
    for i, raw_val in enumerate(raw):
        status = 'normal'
        if i >= len(processed):
            continue  # skip mismatched indices
        if processed[i] > threshold * 1.1:
            status = 'elevated'
        summary[f'sensor_{i}'] = {
            'raw': raw_val,
            'processed': round(processed[i], 2),
            'status': status
        }
    
    # Unused dictionary operations (distraction)
    keys_list = list(summary.keys())
    sorted_keys = sorted(keys_list, reverse=True)
    temp_map = {k: len(k) for k in sorted_keys}
    _ = {**temp_map, **{'extra': 0}}  # dead merge
    
    return summary

# === Main diagnostic engine ===
def analyze_readings(logs):
    # Extract only elevated readings using set filtering
    elevated_set = set()
    all_values = []
    
    for entry in logs.values():
        all_values.append(entry['processed'])
        if entry['status'] == 'elevated':
            elevated_set.add(round(entry['processed']))
    
    # Red herring: unused sorting and transformations
    sorted_values = sorted(all_values)
    mid_point = len(sorted_values) // 2
    median_guess = (sorted_values[mid_point] + sorted_values[~mid_point]) / 2
    
    # Decoy statistical computation
    variance_proxy = sum((x - sum(all_values)/len(all_values))**2 for x in all_values)
    _ = variance_proxy / len(all_values)  # computed but unused
    
    # Critical logic: count how many unique elevated values exceed dynamic threshold
    dynamic_floor = sum(all_values) / len(all_values) + 5
    qualified_elevated = {v for v in elevated_set if v > dynamic_floor}
    
    # Final score based on set size and arithmetic combination
    base_count = len(qualified_elevated)
    multiplier = 3 if len(qualified_elevated) >= 2 else 1
    penalty = 7 if 42 in elevated_set else 0  # irrelevant condition
    
    result = base_count * multiplier * 100 - penalty
    return int(result)

# === Execution flow with branching distractions ===
if __name__ == "__main__":
    # Step 1: Process raw sensor data
    processed_data, avg_val = preprocess_sensors(raw_readings, sample_weights)
    
    # Step 2: Filter significant deviations
    high_readings, positions = filter_high_impact(processed_data, threshold)
    
    # Step 3: Build detailed log (contains irrelevant dict/set ops)
    processed_logs = build_summary_table(raw_readings, processed_data, threshold)
    
    # Step 4: Compute decoy metrics (dead end)
    if avg_val > 25:
        _ = compute_entropy(processed_data)
        shadow_flag = True
        # Following block never executes
        if shadow_flag and False:
            fallback = []
            for x in processed_data:
                fallback.append(x * scaling_factor)
    
    # Step 5: Generate final diagnostic (TARGET INTERVENTION POINT)
    final_diagnostic = analyze_readings(processed_logs)
    
    # Output target variable
    print(f"Result: {final_diagnostic}")