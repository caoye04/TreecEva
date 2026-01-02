import itertools

# Simulated sensor data preprocessing with red herrings
def collect_diagnostics(sensor_log):
    diagnostics = []
    temp_offset = 0.0
    for entry in sensor_log:
        if entry.get('type') == 'TEMP':
            temp_offset += entry['value'] * 0.1
        elif entry.get('type') == 'VIBR':
            diagnostics.append(entry['value'] > 50)
    return diagnostics, temp_offset

# Irrelevant transformation chain (dead abstraction path)
def transform_readings(readings):
    processed = map(lambda x: x ** 2 + 3, readings)
    filtered = filter(lambda x: x > 100, processed)
    return list(filtered)

# Core logic disguised among distractors
def analyze_sequence(seq):
    a, b, c = 1, 1, 0
    for i in range(len(seq)):
        if i % 2 == 0:
            a = (a + seq[i]) % 17
        else:
            b = (b * (seq[i] % 5 + 1)) % 23
        c ^= i & 3
    return (a * b) ^ c

# Decoy function that appears important but is unused
def compute_health_index(log_data):
    total = sum([x['value'] for x in log_data if x.get('critical', False)])
    return total / (len(log_data) or 1)

# Another misleading utility with plausible name
def normalize_signal(signal):
    max_val = max(signal)
    return [s / max_val for s in signal]

# Real processing function buried in noise
def process_metrics(stream):
    # Hidden key variables
    base_values = [x for x in stream if x['sensor'] == 'PRIMARY']
    aux_data = [x for x in stream if x['sensor'] == 'AUX']
    
    # Distractor: complex-looking but unused structure
    history_buffer = [{'timestamp': i, 'cached': val['value']} 
                     for i, val in enumerate(stream) if val['value'] % 7 == 0]
    
    # Relevant computation embedded
    primary_vals = [x['value'] for x in base_values]
    mode_flag = len(primary_vals) % 4 == 2
    
    # Key intermediate result
    checksum = sum(primary_vals) % 97
    
    # Bit manipulation mixed with arithmetic
    shift_factor = len(aux_data) % 6
    adjusted_checksum = (checksum << shift_factor) & 0xFF
    
    # Use of itertools in non-trivial way (valid use)
    rolling_pairs = list(itertools.pairwise(primary_vals))
    pair_sum = sum(a + b for a, b in rolling_pairs if (a + b) % 3 == 0)
    
    # Conditional logic with nested dependencies
    if mode_flag and pair_sum > 50:
        efficiency_score = (adjusted_checksum + pair_sum) * 2
    elif not mode_flag:
        efficiency_score = adjusted_checksum - (pair_sum % 19)
    else:
        efficiency_score = checksum ^ pair_sum
    
    # Red herring: irrelevant final adjustment
    final_enhancement = 0
    for _ in range(3):
        final_enhancement = (final_enhancement * 2 + 1) & 0xF
    
    # Actual answer is efficiency_score, not enhanced
    return {'efficiency_score': efficiency_score, 'diagnostic': final_enhancement}

# Simulated input data
raw_log = [
    {'type': 'TEMP', 'value': 25},
    {'type': 'VIBR', 'value': 55},
    {'type': 'TEMP', 'value': 30}
]

auxiliary_signal = [10, 20, 30, 40]

# Main data stream with structured content
input_stream = [
    {'sensor': 'PRIMARY', 'value': 5},
    {'sensor': 'AUX', 'value': 8},
    {'sensor': 'PRIMARY', 'value': 7},
    {'sensor': 'PRIMARY', 'value': 11},
    {'sensor': 'AUX', 'value': 12},
    {'sensor': 'PRIMARY', 'value': 4},
    {'sensor': 'PRIMARY', 'value': 9},
    {'sensor': 'AUX', 'value': 15}
]

# Trigger diagnostic collection (irrelevant to final result)
diag_results, offset = collect_diagnostics(raw_log)

# Apply decoy transformation on auxiliary data (distractor)
transformed_aux = transform_readings(auxiliary_signal)

# Real execution point
final_output = process_metrics(input_stream)

# Print target result
Result: {final_output['efficiency_score']}