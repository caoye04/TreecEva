import math

# Irrelevant helper function (dead code path)
def unused_signal_filter(x):
    return [val for val in x if val > 0.5]

# Misleading intermediate computation
temp_offset = sum([math.sin(i * 0.1) for i in range(10)]) * 100
decoys = {'alpha': 327, 'beta': 884, 'gamma': temp_offset, 'zeta': None}

# Actual data pipeline setup
raw_readings = [12, 15, 22, 28, 35, 40, 45]
scaling_factor = 2.5

# Distractor: complex-looking but unused transformation chain
transformed_chain = list(map(lambda x: round(math.log(x + 1) ** 1.5), raw_readings))
shadow_state = {k: v * 0.9 for k, v in enumerate(transformed_chain)}

# Real signal preprocessing
def apply_noise_floor(data, floor=5.0):
    return [max(floor, x) for x in data]

def shift_phase(arr, steps):
    return arr[-steps:] + arr[:-steps]

adjusted_readings = apply_noise_floor(raw_readings)
rotated_buffer = shift_phase(adjusted_readings, 2)

# Tuple-based calibration metadata
calibration = (1.8, 'linear', lambda c: c * 0.75)
scale_param, mode, postprocess_func = calibration

# Dictionary configuration with red herring keys
baseline_config = {
    'threshold': 25,
    'gain': scale_param,
    'active': True,
    'mode': mode,
    'padding': 3,
    'legacy_mode': False,
    'debug_trace': [0, 0, 0],
    'version': '3.8'
}

# Core transformation using lambda and actual logic
transformed_data = list(map(lambda x: postprocess_func(x * scaling_factor), rotated_buffer))

# Decoy accumulation loop (unused result)
cumulative_error = 0.0
for i in range(len(transformed_data) - 1):
    cumulative_error += abs(transformed_data[i] - transformed_data[i+1])
cumulative_error = round(cumulative_error, 3)

# Conditional manipulation with nested logic
aggregated_score = 0
if baseline_config['active']:
    filtered = [x for x in transformed_data if x >= baseline_config['threshold']]
    if len(filtered) > 2:
        aggregated_score = sum(filtered) * baseline_config['gain']
    else:
        secondary_weight = 1.2
        aggregated_score = sum(transformed_data) * secondary_weight
else:
    aggregated_score = 50

# Final processing function with distractor variables
intermediate_flag = False
def process_metrics(data, config):
    base = sum(data)
    adjustment = 0
    
    # Nested condition tree with misleading branches
    if config['gain'] > 1.5:
        if config['padding'] % 2 == 1:
            adjustment = 15
        else:
            adjustment = -10
    elif config['legacy_mode']:
        adjustment = 100  # unreachable
    else:
        adjustment = 5
    
    # Critical red herring: modifies a variable not used in output
    local_copy = data[:]
    for idx in range(len(local_copy)):
        if local_copy[idx] > 30:
            local_copy[idx] *= 0.95
    
    # Actual answer derivation via multi-step logic
    raw_total = sum(data)
    threshold_applied = [x for x in data if x >= config['threshold']]
    bonus = len(threshold_applied) * 7
    penalty = 0
    
    for val in data:
        if val < 10:
            penalty += 3
    
    # Key formula combining multiple concepts
    result = (raw_total + adjustment + bonus - penalty) * 0.8
    
    # Dead assignment (distractor)
    result = round(result, 6)
    
    # Final override based on conditional rule
    if len(threshold_applied) >= 3:
        result = result * 1.1
    
    return result

# Execution point of interest
final_diagnostic = process_metrics(transformed_data, baseline_config)

# Print required output
print(f"Result: {final_diagnostic}")