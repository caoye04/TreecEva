import math

def analyze_signal(pattern):
    # Irrelevant signal processing function (dead code path)
    magnitude = sum([p ** 2 for p in pattern])
    return math.sqrt(magnitude) if magnitude > 0 else 0

def validate_checksum(entry):
    # Unused validation logic (distractor)
    total = 0
    for c in str(entry):
        if c.isdigit():
            total += int(c)
    return total % 7 == 0

def transform_sequence(seq, factor):
    # Decoy transformation with bit manipulation (misleading intermediate)
    shifted = [(x << 1) ^ factor for x in seq]
    return [s % 100 for s in shifted]

def compute_entropy(values):
    # Seemingly important but unused entropy calculation
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    probs = [freq_map[v] / len(values) for v in freq_map]
    return -sum(p * math.log2(p) for p in probs)

def extract_timestamp(record):
    # String parsing distractor
    if 'T' in record:
        time_part = record.split('T')[1][:6]
        return int(time_part.lstrip('0')) if time_part.lstrip('0') else 0
    return -1

def process_metrics(data_log, state_config):
    # Core logic buried among distractions
    base_score = 0
    
    # Relevant: extract sensor readings
    readings = [entry['value'] for entry in data_log if entry['type'] == 'sensor']
    
    # Relevant: apply dynamic gain based on mode
    gain = 1.5 if state_config['mode'] == 'turbo' else 0.8
    amplified = [r * gain for r in readings]
    
    # Distractor: unused transformation
    dummy_seq = transform_sequence(readings, 3)
    
    # Relevant: filter out extreme values
    filtered = [val for val in amplified if 10 <= val <= 400]
    
    # Distractor: fake checksum validation loop
    valid_entries = 0
    for d in data_log:
        if isinstance(d['id'], int) and validate_checksum(d['id']):
            valid_entries += 1  # Never used
    
    # Relevant: calculate adjusted mean
    mean_val = sum(filtered) / len(filtered) if filtered else 0
    
    # Relevant: correction factor from config
    corr_factor = state_config.get('calibration', 1.1)
    corrected_mean = mean_val * corr_factor
    
    # Distractor: string-based timestamp extraction
    timestamps = []
    for entry in data_log:
        ts = extract_timestamp(entry['timestamp'])
        if ts > 0:
            timestamps.append(ts)
    
    # Distractor: entropy of timestamps (unused)
    if timestamps:
        ts_entropy = compute_entropy([t % 10 for t in timestamps])
    
    # Relevant: final adjustment using min threshold
    threshold = max(25, state_config['threshold'])
    final_diagnostic = int(max(corrected_mean - threshold, 5))
    
    # Distractor: irrelevant dictionary aggregation
    summary = {
        'count': len(data_log),
        'modes': list(set(state_config.keys())),
        'flags': {k: v for k, v in state_config.items() if isinstance(v, bool)}
    }
    
    return final_diagnostic

# Simulated input data
log_data = [
    {'id': 1001, 'type': 'sensor', 'value': 20, 'timestamp': '2023-12-01T123045'},
    {'id': 1002, 'type': 'sensor', 'value': 150, 'timestamp': '2023-12-01T123105'},
    {'id': 1003, 'type': 'sensor', 'value': 300, 'timestamp': '2023-12-01T123125'},
    {'id': 1004, 'type': 'status', 'value': 1, 'timestamp': '2023-12-01T123145'},  # not sensor
    {'id': 1005, 'type': 'sensor', 'value': 400, 'timestamp': '2023-12-01T123205'},
    {'id': 1006, 'type': 'sensor', 'value': 500, 'timestamp': '2023-12-01T123225'}  # will be filtered
]

system_state = {
    'mode': 'turbo',
    'calibration': 1.2,
    'threshold': 30,
    'debug': False,
    'timeout': 150
}

# Key execution point
final_diagnostic = process_metrics(log_data, system_state)

# Output result
print(f"Result: {final_diagnostic}")