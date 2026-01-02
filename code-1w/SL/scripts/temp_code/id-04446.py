def monitor_system_metrics(raw_inputs):
    baseline = 42
    adjustment_factor = 1.618
    temp_cache = []
    diagnostic_log = set()
    anomaly_count = 0

    for entry in raw_inputs:
        if isinstance(entry, dict) and 'signal' in entry:
            signal_val = entry['signal']
            adjusted = signal_val * adjustment_factor
            if adjusted > baseline:
                temp_cache.append(adjusted)
                if adjusted % 2 == 0:
                    diagnostic_log.add(int(adjusted))
            else:
                anomaly_count += 1

    filtered_diagnostics = {x for x in diagnostic_log if x > 50}
    return temp_cache, filtered_diagnostics, anomaly_count


def compute_stability_index(data_stream):
    cumulative = 0
    weight_sequence = [0.1, 0.2, 0.3, 0.4]
    temp_vals = []

    for i, val in enumerate(data_stream):
        weighted_val = val * weight_sequence[i % 4]
        cumulative += weighted_val
        temp_vals.append(weighted_val)

    average_weighted = cumulative / len(data_stream) if data_stream else 0
    stability_score = abs(cumulative - average_weighted * 2)
    return stability_score, temp_vals

def evaluate_threshold_coverage(metrics, bounds):
    coverage_map = {}
    total_bounds = len(bounds)
    hit_count = 0

    for i, bound in enumerate(sorted(bounds)):
        covered = any(x >= bound for x in metrics)
        coverage_map[bound] = covered
        if covered:
            hit_count += 1

    hit_ratio = hit_count / total_bounds if total_bounds else 0
    return hit_ratio, coverage_map

# Irrelevant helper (decoy function)
def unused_signal_validator(seq):
    return all(isinstance(x, float) for x in seq)

# Unused constant (red herring)
MAX_PHASE_CAPACITY = 999

# Simulated sensor input (real data source)
sensor_readings = [
    {'signal': 30}, {'signal': 60}, {'signal': 25},
    {'signal': 80}, {'signal': 45}, {'signal': 70}
]

# Step 1: Extract primary data
processed_data, active_diagnostics, errors = monitor_system_metrics(sensor_readings)

# Step 2: Compute derived index
index_value, _ = compute_stability_index(processed_data)

# Step 3: Define evaluation thresholds
threshold_candidates = {40, 65, 75, 85, 90}
decoy_set = {10, 20, 30}  # Unused distraction

# Step 4: Assess coverage
coverage_rate, _ = evaluate_threshold_coverage(processed_data, threshold_candidates)

# Step 5: Complex conditional logic with distractors
status_flags = []
if len(active_diagnostics) > 2:
    status_flags.append(1)
if coverage_rate > 0.6:
    status_flags.append(2)
if index_value < 100:
    status_flags.append(4)

aggregated_flag = sum(status_flags)

# Distractor block: irrelevant transformation
shadow_copy = [x * 0.95 for x in processed_data if x > 55]
shadow_sum = sum(shadow_copy)

# Critical computation path
working_set = set(processed_data)
refined_diagnostics = working_set.intersection(active_diagnostics)

# Final analysis with key variable assignment
def analyze_fluctuations(data_points, reference_set):
    fluctuation_score = 0
    base_anchor = 55

    for point in data_points:
        if point in reference_set:
            fluctuation_score += int(point // 3)
        elif point > base_anchor:
            fluctuation_score += 5
        else:
            fluctuation_score -= 2

    secondary_modifier = len(reference_set) * 3
    final_score = fluctuation_score + secondary_modifier

    # Dead code branch (never executed due to logic)
    if False:
        final_score *= 2
        for _ in range(3):
            final_score -= 10

    return final_score

final_diagnostic = analyze_fluctuations(collected_data=processed_data, threshold_set=active_diagnostics)

print(f"Result: {final_diagnostic}")