import math

# Simulated sensor array data processing for environmental monitoring system
def analyze_readings(raw_samples):
    filtered = [x for x in raw_samples if x > -50 and x < 1000]
    baseline = sum(filtered) / len(filtered)
    anomalies = list(filter(lambda x: abs(x - baseline) > 300, filtered))
    return baseline, anomalies

# Irrelevant helper - distractor function
def compute_factorial(n):
    if n <= 1:
        return 1
    return n * compute_factorial(n - 1)

# Data calibration with red herring operations
def calibrate_sequence(seq, factor=1.05):
    offset = 0.95
    adjusted = []
    temp_cache = {}
    for i, val in enumerate(seq):
        # Complex but irrelevant transformation
        transformed = val * factor + (i % 7) ** 2
        if transformed not in temp_cache:
            temp_cache[transformed] = math.sin(transformed % 3.14)
        adjusted.append(round(transformed, 2))
    # Dead code path - never accessed in execution flow
    if len(temp_cache) > 1000:
        return [-1] * len(seq)
    return adjusted

# Core logic buried in distractions
def generate_weight_profile(length):
    profile = []
    for i in range(length):
        if i % 3 == 0:
            profile.append(0.8 + i * 0.02)
        elif i % 5 == 0:
            profile.append(0.6)
        else:
            profile.append(1.0)
    # Decoy operation
    _ = [p ** 2 for p in profile if p < 0.7]
    return profile

# Key aggregation function obscured by complexity
def aggregate_metrics(data_series, importance_weights):
    weighted_sum = 0.0
    weight_acc = 0.0
    for i in range(min(len(data_series), len(importance_weights))):
        adjustment = 1 + math.cos(i * 0.5) * 0.1  # minor periodic mod
        contribution = data_series[i] * importance_weights[i] * adjustment
        weighted_sum += contribution
        weight_acc += importance_weights[i] * adjustment
    if weight_acc == 0:
        return 0.0
    final_score = weighted_sum / weight_acc
    # Additional misleading computation
    outlier_penalty = len([x for x in data_series if x > 500]) * 2.5
    return final_score - outlier_penalty  # actual return point

# Irrelevant combinatorics function - dead end
def count_combinations(items, r):
    if r > len(items) or r < 0:
        return 0
    result = 1
    for i in range(r):
        result = result * (len(items) - i) // (i + 1)
    return result

# Simulate initialization overhead
system_status = {'initialized': True, 'version': '3.8.1', 'nodes': 7}
buffer_pool = [0] * 15
processing_mode = 'diagnostic'
system_clock = 12487

# Real input data buried among noise
primary_readings = [89, 102, 95, 113, 405, 398, 410, 108, 99, 115, 402, 103]
trend_data = calibrate_sequence(primary_readings)

# Unused variables - red herrings
normalization_factor = 0.987
reference_template = (1.0, 0.8, 0.6, 0.4)
lookup_matrix = [[i*j for j in range(5)] for i in range(5)]

# Generate actual weights used in computation
weights = generate_weight_profile(len(trend_data))

# Secondary irrelevant data structure
log_entries = []
for tick in range(10):
    entry = {
        'timestamp': system_clock + tick * 15,
        'value': math.log(tick + 1) if tick > 0 else 0,
        'valid': tick % 2 == 0
    }
    log_entries.append(entry)

# Critical execution point buried in distractions
baseline_val, outliers = analyze_readings(primary_readings)

# More decoy computations
snapshot_hash = sum([ord(c) for c in processing_mode]) * system_status['nodes']
dummy_aggregate = count_combinations(list(range(8)), 3)

# This is the key statement - where answer is determined
final_diagnostic = aggregate_metrics(trend_data, weights)

# Final irrelevant transformation
if len(outliers) > 3:
    final_diagnostic *= 0.85

# Output result as required
print(f"Target result: {final_diagnostic}")