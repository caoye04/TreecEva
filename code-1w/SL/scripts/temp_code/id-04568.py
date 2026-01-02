import math

# Simulated sensor array diagnostics with interference
raw_readings = [3, 7, 12, 18, 25, 33, 42, 52]
offset_calibration = 1.5
temp_buffer = [x * 1.01 for x in raw_readings if x > 10]

# Irrelevant noise: historical averages with no impact
historical_avg = sum([2.1, 3.4, 4.5, 5.6, 6.7]) / 5
baseline_shift = lambda x: x + 0.05

# Data transformation pipeline
scaling_factor = 2.0
data_offset = 5
transformed_data = []
for val in raw_readings:
    adjusted = (val + offset_calibration) * scaling_factor
    if adjusted > 30:
        adjusted -= data_offset
    transformed_data.append(round(adjusted, 2))

# Decoy function: looks important but unused
def compute_fidelity(x):
    return sum([math.sin(i) for i in x])

# Real processing begins here
metric_weights = {"w1": 0.3, "w2": 0.7}
def threshold_func(x):
    return x > 40

# Misleading intermediate: complex but irrelevant structure
audit_trail = set()
for i in range(len(transformed_data)):
    audit_trail.add((i, round(math.cos(transformed_data[i]), 3)))

# Another red herring: tuple unpacking with dummy values
config_flags = (True, False, 'legacy')
enable_enhanced, _, mode_flag = config_flags

# Core logic hidden among distractions
aggregated_score = 0
for i, val in enumerate(transformed_data):
    weight = metric_weights["w1"] if i % 2 == 0 else metric_weights["w2"]
    penalty = math.log(val) if val > 45 else 0
    aggregated_score += val * weight - penalty

# Secondary processing chain
intermediate_diagnostics = []
def process_chain(data_list):
    result = []
    for item in data_list:
        # Complex-looking but ultimately discarded computation
        shadow_val = (item ** 0.5) * 1.1
        if shadow_val < 10:
            result.append(item * 0.9)
        else:
            result.append(item * 1.05)
    return result

# Unused but plausible-looking call
shadow_diagnostics = process_chain(transformed_data)

# Actual analysis function used
def analyze_metrics(data, threshold_fn):
    above_threshold = list(filter(threshold_fn, data))
    below_threshold = [x for x in data if not threshold_fn(x)]
    
    # Distractor: elaborate but unused calculation
    outlier_score = 0
    if len(above_threshold) > 0:
        mean_high = sum(above_threshold) / len(above_threshold)
        outlier_score = sum([(x - mean_high) ** 2 for x in above_threshold])
    
    # Critical path: subtle dependency on earlier loop
    adjustment_factor = 1.1 if len(above_threshold) >= 3 else 0.9
    base_metric = sum(below_threshold) / len(below_threshold) if below_threshold else 0
    
    # Final result depends on this specific combination
    final_value = base_metric * adjustment_factor
    
    # Dead code branch: never executed due to logic
    if enable_enhanced and mode_flag == 'debug':
        final_value += 100  # decoy increment
    
    return round(final_value, 4)

# Key execution point
final_diagnostic = analyze_metrics(transformed_data, threshold_func)

# Output requirement
print(f"Result: {final_diagnostic}")