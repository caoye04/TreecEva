def analyze_signal_strength(signal_sequence, baseline):
    adjusted_peaks = []
    noise_floor = 0.05
    peak_threshold = baseline * 0.7
    for val in signal_sequence:
        if val > peak_threshold:
            adjusted_peaks.append(val * 0.9)
    return len(adjusted_peaks) > 3

# Irrelevant helper (dead function - not used)
def deprecated_normalization(x):
    return (x + 1) / 2 if x < 0 else x / (x + 1)

# Signal data from sensor array (simulated)
sensor_readings = [0.12, 0.81, 0.93, 0.25, 0.76, 0.88, 0.41]

# Distractor variables (unused but plausible)
calibration_offset = 0.03
reference_frame = [0.1, 0.3, 0.5]
validation_checkpoints = {"start": 0, "mid": 3, "end": 7}

# Simulate multi-stage processing chain
stages = ['input', 'filter', 'amplify', 'normalize', 'diagnose']
stage_weights = {'input': 1, 'filter': 0.8, 'amplify': 1.5, 'normalize': 0.7, 'diagnose': 1.2}

# Complex transformation with list comprehension and filtering
processing_chain = [
    (idx * stage_weights[stage]) ** 0.5 
    for idx, stage in enumerate(stages) 
    if 'i' in stage and idx % 2 == 0
]

# Red herring: unused transformation path
legacy_pipeline = [w * 0.95 for w in stage_weights.values() if w > 1.0]

# Threshold configuration (only some are used)
thresholds = {
    'critical': 2.1,
    'warning': 1.3,
    'info': 0.8,
    'debug': 0.2
}

# Decoy logic block (never executed)
if False:
    temp_result = 0
    for k in thresholds:
        temp_result += len(k)
    debug_trace = temp_result

# Key recursive function for diagnostic scoring
def compute_diagnostic_score(seq, depth):
    if depth <= 0 or len(seq) == 0:
        return 0.0
    mid = len(seq) // 2
    left_part = seq[:mid]
    right_part = seq[mid+1:]
    current = seq[mid] * (depth * 0.6)
    # Recursive calls
    left_score = compute_diagnostic_score(left_part, depth-1)
    right_score = compute_diagnostic_score(right_part, depth-2)
    return current + left_score + right_score * 0.5

# Secondary metric based on character logic (case conversion + counting)
def count_uppercase_chars(tag_list):
    combined = ''.join(tag_list)
    return len([c for c in combined if c.isupper()])

labels = ['SensorA', 'DiagB', 'NodeC', 'EventD']
label_score = count_uppercase_chars(labels)  # Returns 8

# Actual computation path disguised among distractors
intermediate_flags = [
    analyze_signal_strength(sensor_readings, 0.75),
    len(processing_chain) >= 2,
    label_score % 3 == 2
]

flag_value = sum([1 for f in intermediate_flags if f])

# Main aggregation function
def aggregate_metrics(chain, limits):
    raw_sum = sum(chain)
    penalty = 0
    if raw_sum > limits['warning']:
        penalty = raw_sum * 0.1
    elif raw_sum < limits['debug']:
        penalty = -0.5
    base_score = raw_sum - penalty
    recursion_input = [base_score, flag_value, 2.1, 1.8]
    final_component = compute_diagnostic_score(recursion_input, 3)
    return int(base_score * final_component)  # Final integer result

# Execute key statement
diagnostic_state = True if flag_value > 1 else False
final_diagnostic = aggregate_metrics(processing_chain, thresholds)
print(f"Target result: {final_diagnostic}")