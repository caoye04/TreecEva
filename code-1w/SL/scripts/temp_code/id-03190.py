import itertools

# Simulated telemetry data from a distributed sensor network
def collect_telemetry(nodes):
    readings = []
    for node in nodes:
        base = hash(node) % 100
        seq = [(base + i * 7) % 85 for i in range(5)]
        readings.extend(seq)
    return readings

# Legacy checksum (irrelevant but looks important)
def compute_legacy_checksum(data):
    acc = 0
    for x in data[:10]:
        acc = (acc * 31 + x) % 65536
    return acc + 1000  # red herring

# Data cleansing with distraction logic
def cleanse_data(raw):
    cleaned = [x for x in raw if x > 10]
    temp_sum = sum([x for x in cleaned if x % 2 == 0])  # unused path
    adjusted = [x - 5 for x in cleaned]
    outlier_threshold = 75
    filtered = list(itertools.dropwhile(lambda x: x < outlier_threshold, sorted(adjusted)))
    return filtered if len(filtered) > 3 else [0]  # decoy branch

# Core transformation pipeline
def transform_sequence(series):
    if not series:
        return [0]
    transformed = []
    for i, val in enumerate(series):
        if i % 2 == 0:
            transformed.append(val ^ (i + 3))  # bitwise XOR
        else:
            transformed.append(val * 2 + (val & 7))  # AND operation
    return transformed

# State-aware accumulator (with misleading intermediate)
def accumulate_diagnostics(vals, state):
    accum = 0
    mode_flag = state['mode'] > 1
    shift_param = 2 if mode_flag else 3
    
    # Decoy accumulation path
    temp_accum = 0
    for v in vals[::2]:
        temp_accum += v % 9
    temp_accum *= 5  # never used
    
    # Actual accumulation
    for idx, v in enumerate(vals):
        if idx % 3 == 0:
            accum += (v >> shift_param)  # right shift
        elif state['active']:
            accum -= (v & 15)  # mask lower bits
    return abs(accum)

# Main processing function
def process_metrics(log_input, sys_state):
    # Irrelevant string preprocessing (distractor)
    metadata_tags = ['node_X', 'sensor_Y', 'ver_3.1']
    tag_concat = ''.join(metadata_tags)
    tag_hash = len(tag_concat) * 3  # looks important, unused
    
    # Key execution path begins
    cleansed = cleanse_data(log_input)
    
    # Another distraction: simulate redundant validation
    valid_count = 0
    for item in cleansed:
        if item in range(20, 80):
            valid_count += 1
    compliance_ratio = valid_count / len(cleansed) if cleansed else 0  # dead metric
    
    # Transform and analyze
    signal_chain = transform_sequence(cleansed)
    
    # Introduce tuple unpacking distraction
    aux_data = [(15, 23), (44, 19), (37, 12)]
    for a, b in aux_data:
        if a > b:
            a, b = b, a  # dummy swap
    
    # Final diagnostic computation
    diagnostic_score = accumulate_diagnostics(signal_chain, sys_state)
    calibration_offset = sum(x * 0.1 for x in signal_chain if x < 30)  # float distractor
    final_diagnostic = diagnostic_score - int(calibration_offset)
    
    return final_diagnostic

# Execution entry point
if __name__ == '__main__':
    network_nodes = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
    raw_logs = collect_telemetry(network_nodes)
    
    # System state with meaningful flags
    system_state = {
        'mode': 2,
        'active': True,
        'version': '2.4'
    }
    
    # Redundant checksum call (dead path)
    _ = compute_legacy_checksum(raw_logs)
    
    # Critical statement
    final_diagnostic = process_metrics(raw_logs, system_state)
    print(f"Result: {final_diagnostic}")