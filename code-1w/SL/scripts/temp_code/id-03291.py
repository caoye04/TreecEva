import math

# Simulated system telemetry data with mixed relevance
data_log = [
    {'timestamp': 1623456780, 'power_draw': 230.5, 'temp_core': 67.3, 'status_flag': 0b1010},
    {'timestamp': 1623456789, 'power_draw': 235.1, 'temp_core': 69.1, 'status_flag': 0b1110},
    {'timestamp': 1623456798, 'power_draw': 240.3, 'temp_core': 71.5, 'status_flag': 0b1111},
    {'timestamp': 1623456807, 'power_draw': 238.7, 'temp_core': 70.2, 'status_flag': 0b1101}
]

# Irrelevant historical constants (distractors)
BASELINE_VOLTAGE = 220.0
CALIBRATION_FACTOR = 0.987
MAX_TEMP_LIMIT = 85.0
MIN_POWER_DRAW = 100.0
REFERENCE_TIMESTAMP = 1623456000

# Decoy functions that are defined but not used
def analyze_pattern(seq):
    return sum(x['power_draw'] * 0.1 for x in seq if x['temp_core'] > 70)

def compute_entropy(values):
    return -sum(p * math.log2(p) for p in values if p > 0)

def legacy_checksum(data):
    return sum(len(str(val)) for entry in data for val in entry.values()) % 17

# Real processing begins here
aggregated_metrics = []
outlier_count = 0
rolling_average = 0.0

for record in data_log:
    # Extract relevant fields
    power = record['power_draw']
    temp = record['temp_core']
    flag = record['status_flag']
    
    # Bit manipulation to extract operational modes (relevant)
    mode_active = (flag & 0b1100) >> 2
    error_state = (flag & 0b0011)
    
    # Compute efficiency factor using conditional expression
    efficiency_factor = 1.0 if temp < 70 else (0.85 if temp < 75 else 0.6)
    
    # Update rolling average (simple linear search pattern over last two)
    if len(aggregated_metrics) >= 1:
        prev_power = aggregated_metrics[-1]['smoothed_power']
        rolling_average = (prev_power + power) / 2
    else:
        rolling_average = power
    
    # Detect outliers based on rate of change
    if len(aggregated_metrics) > 0:
        delta = abs(power - aggregated_metrics[-1]['raw_power'])
        if delta > 10.0:
            outlier_count += 1
    
    # Pack processed entry
    aggregated_metrics.append({
        'raw_power': power,
        'smoothed_power': rolling_average,
        'thermal_effort': max(0, temp - 65) * efficiency_factor,
        'mode': mode_active,
        'errors': error_state
    })

# Define threshold function as lambda (required feature)
threshold_func = lambda x: x['thermal_effort'] > 3.0 and x['mode'] == 0b11

# Another decoy set operation with no impact
irrelevant_set_a = {1, 2, 3, 4, 5}
irrelevant_set_b = {4, 5, 6, 7, 8}
set_intersection = irrelevant_set_a & irrelevant_set_b  # Unused result
set_union = irrelevant_set_a | irrelevant_set_b         # Dead code path
complement_ops = [x for x in set_union if x not in set_intersection]  # Distractor list

# Core processing function with nested logic
valid_entries = 0
total_effort = 0.0
consistency_bonus = 0

for item in aggregated_metrics:
    meets_threshold = threshold_func(item)
    
    # Multi-condition filtering with short-circuit evaluation
    if item['mode'] == 3 and item['errors'] == 0 and meets_threshold:
        valid_entries += 1
        total_effort += item['thermal_effort']
    elif item['mode'] == 2 and item['thermal_effort'] > 2.0:
        total_effort += item['thermal_effort'] * 0.5  # Partial credit
    else:
        pass  # Explicit dead branch for confusion

# Additional distraction: combinatorics-inspired but unused calculation
n = len(data_log)
k = 2
combinations_n_choose_k = math.factorial(n) // (math.factorial(k) * math.factorial(n - k)) if n >= k else 0
combination_scorer = lambda c, v: v * (c % 4)  # Unused lambda

# Final processing with tuple unpacking and conditional assignment
raw_sum = sum(m['raw_power'] for m in aggregated_metrics)
normalized_base = raw_sum / len(aggregated_metrics)

# Key statement: process_metrics includes distractors and real computation
def process_metrics(log_data, thresh_fn):
    # Red herring variables
    stability_metric = 0.0
    peak_deviation = 0.0
    penalty_factor = 1.0
    
    # Recompute something already known (distraction)
    reverified_count = 0
    for d in log_data:
        if d['temp_core'] > 65:
            reverified_count += 1
    
    # Actual new work: use set to track unique modes (set operation)
    active_modes = set()
    for m in aggregated_metrics:
        active_modes.add(m['mode'])
    
    mode_complexity = len(active_modes) if len(active_modes) > 1 else 1
    
    # Compute final efficiency score
    base_score = total_effort * 100
    if valid_entries >= 2:
        consistency_bonus = 50
    elif valid_entries == 1:
        consistency_bonus = 20
    else:
        consistency_bonus = 0
    
    # Introduce nonlinear scaling via logarithmic adjustment
    diversity_enhancer = math.log(mode_complexity + 1)
    
    # Final formula with multiple factors (some irrelevant)
    efficiency_score = (
        base_score + 
        consistency_bonus + 
        (diversity_enhancer * 10) - 
        (outlier_count * 5)  # Penalty for instability
    )
    
    # Dead code: these variables are computed but unused
    final_normalized = efficiency_score / (normalized_base + 1)
    adjusted_ratio = final_normalized * math.pi
    
    return efficiency_score  # Only this matters

# Execute key statement
final_output = process_metrics(data_log, threshold_func)

# Print result as required
print(f"Target result: {final_output}")