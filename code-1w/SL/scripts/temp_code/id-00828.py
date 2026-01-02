import math

# Simulated sensor array diagnostics with interference
sensor_ids = ['S1', 'S2', 'S3', 'S4']
baseline_readings = {sid: (ord(sid[1]) * 1.5) for sid in sensor_ids}
offset_map = {'S1': 2, 'S2': -1, 'S3': 3, 'S4': 0}

# Irrelevant calibration data (distractor)
calibration_matrix = [[1, 0], [0, 1]]
scaling_factor = 1.0  # Unused in final computation

# Simulate environmental noise (mostly unused)
noise_profile = []
for i in range(4):
    val = (i ** 2 + 1) * 0.1
    noise_profile.append(val)

# Primary logic trail with red herrings
raw_sequence = [3, 7, 2, 8, 1, 9]
filtered_stream = [x for x in raw_sequence if x > 5]
decay_weights = [0.9 ** i for i in range(len(filtered_stream))]
weighted_sum = sum(filtered_stream[i] * decay_weights[i] for i in range(len(filtered_stream)))

# Dummy transformation chain (dead path)
transform_log = []
temp_val = weighted_sum
for _ in range(3):
    temp_val = math.sin(temp_val) + 0.1
    transform_log.append(temp_val)

# Conditional signal inversion (irrelevant due to condition not met)
signal_inverted = False
inversion_threshold = 100
if weighted_sum > inversion_threshold:
    filtered_stream = [-x for x in filtered_stream]
    signal_inverted = True

# Key data structure: logic trail built from multiple sources
logic_trail = {
    'source': 'ARRAY_ALPHA',
    'readings': filtered_stream,
    'weighting': decay_weights,
    'aggregate': weighted_sum,
    'flags': [False, True, False],
    'checksum': sum(ord(c) for c in 'S4') + 7
}

# Threshold policy with decoy entries
thresholds = {
    'critical': 8.0,
    'warning': 5.5,
    'info': 2.0,
    'debug': 0.1,  # Unused level
    'legacy_mode': False,
    'tolerance_window': [0.5, 1.5]  # Unused
}

# Secondary auxiliary function (decoy - never called)
def legacy_diagnose(data):
    return sum(d ** 0.5 for d in data if d > 0) / len(data)

# Core analysis with conditional expression and dictionary operations
def analyze_pattern(trail, config):
    readings = trail['readings']
    total = trail['aggregate']
    
    # Red herring computation
    entropy = 0.0
    for r in readings:
        if r > 0:
            entropy -= (r / total) * math.log(r / total)
    
    # Determine severity using nested conditions and dictionary lookup
    level = 'info'
    if total > config['critical']:
        level = 'critical'
    elif total > config['warning']:
        level = 'warning'
    else:
        level = 'normal'
    
    # Flag-based override (short-circuit logic - appears relevant but isn't triggered)
    override_active = False
    if trail['flags'][0] and not trail['flags'][1]:
        override_active = True
    
    # Conditional expression determining diagnostic code
    base_code = 1000 if level == 'critical' else (500 if level == 'warning' else 100)
    modifier = 10 if trail.get('corrupted', False) else 5
    
    # Final computation with distractor-influenced but deterministic result
    checksum_adj = trail['checksum'] % 25
    diagnostic_score = base_code + modifier + checksum_adj
    
    # Additional irrelevant transformation
    normalized_score = diagnostic_score / 11.5
    if normalized_score > 100:
        normalized_score = math.sqrt(normalized_score)
    
    return int(diagnostic_score)

# Misleading pre-check (unused result)
preliminary = analyze_pattern({'readings': [1,2], 'aggregate': 3, 'flags': [0,0,0], 'checksum': 10}, thresholds)

# Critical execution point
final_diagnostic = analyze_pattern(logic_trail, thresholds)

# Output result as required
print(f"Result: {final_diagnostic}")