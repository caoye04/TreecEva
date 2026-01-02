import math

# Simulated telemetry data from satellite subsystems
telemetry_stream = [
    {'temp': 78, 'power': 120, 'signal': 85, 'timestamp': 1001},
    {'temp': 82, 'power': 118, 'signal': 83, 'timestamp': 1002},
    {'temp': 85, 'power': 125, 'signal': 80, 'timestamp': 1003},
    {'temp': 90, 'power': 130, 'signal': 75, 'timestamp': 1004},
    {'temp': 95, 'power': 140, 'signal': 70, 'timestamp': 1005}
]

# Irrelevant lookup table for deprecated systems
legacy_codes = {1: 'A', 2: 'B', 3: 'C'}
deprecated_map = {k: chr(65 + k) for k in range(1, 10)}

# Distractor: unused signal processing chain
buffer_cache = []
def cache_signal(x):
    buffer_cache.append(x * 1.05)
    return buffer_cache[-1]

# Real-time filter (never called)
def apply_kalman(signal_list):
    smoothed = []
    for i, s in enumerate(signal_list):
        if i == 0:
            smoothed.append(s)
        else:
            smoothed.append(0.7 * s + 0.3 * smoothed[i-1])
    return smoothed

# Auxiliary function with red herring logic
def assess_health(power_val, temp_val):
    if power_val > 135:
        return 'CRITICAL'
    elif temp_val > 92:
        return 'WARNING'
    else:
        return 'NORMAL'

# Unused diagnostic tree
HEALTH_MATRIX = {
    'NORMAL': lambda x: x * 0.9,
    'WARNING': lambda x: x * 1.1,
    'CRITICAL': lambda x: x * 1.3
}

# Core transformation pipeline
def extract_signals(data_list):
    signals = [entry['signal'] for entry in data_list]
    powers = [entry['power'] for entry in data_list]
    temps = [entry['temp'] for entry in data_list]
    return signals, powers, temps

# Bit manipulation for error checking (used later)
def compute_parity(value):
    parity = 0
    while value > 0:
        parity ^= (value & 1)
        value >>= 1
    return parity

# Checksum based on bitwise operations
def generate_checksum(num_list):
    checksum = 0
    for num in num_list:
        checksum ^= int(math.sqrt(num) * 10)  # Introduce non-linearity
    return checksum

# Data normalization with distractor branches
def normalize_range(values, method='linear'):
    min_v, max_v = min(values), max(values)
    if method == 'linear':
        return [(v - min_v) / (max_v - min_v + 1e-8) for v in values]
    elif method == 'log':
        return [math.log(1 + v - min_v) for v in values]  # Not used
    else:
        return values

# Misleading statistical summary (unused)
def compute_entropy(signal_vals):
    from collections import Counter
    counts = Counter(signal_vals)
    total = len(signal_vals)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Main processing function with hidden logic path
def process_metrics(log_data, state_config):
    # Step 1: Extract relevant telemetry
    sigs, pwr, tmps = extract_signals(log_data)
    
    # Step 2: Normalize signals (only linear branch taken)
    norm_sigs = normalize_range(sigs, method=state_config.get('norm', 'linear'))
    
    # Step 3: Compute derived metrics
    avg_power = sum(pwr) / len(pwr)
    peak_temp = max(tmps)
    
    # Step 4: Apply bitmask-based validation
    valid_count = 0
    for i, s in enumerate(sigs):
        if compute_parity(s) == compute_parity(pwr[i]):
            valid_count += 1
    
    # Step 5: Generate checksum for data integrity (red herring)
    _ = generate_checksum(sigs)
    _ = generate_checksum(pwr)
    
    # Step 6: Conditional weighting based on system mode
    weight = 1.0
    if state_config['mode'] == 'ECO':
        weight = 0.8
    elif state_config['mode'] == 'TURBO':
        weight = 1.2
    
    # Step 7: Hidden aggregation logic
    base_score = 0
    for i in range(len(norm_sigs)):
        contribution = norm_sigs[i] * (1 + 0.01 * (tmps[i] - 70))
        base_score += contribution
    
    # Step 8: Final adjustment using bitwise and arithmetic combo
    adjusted = int((base_score * 100) ^ valid_count)  # XOR with count
    final_value = adjusted * weight
    
    # Step 9: Apply override if safety threshold breached (not triggered)
    if peak_temp > 100:
        final_value = 999  # Dead code path
    
    # Step 10: Round to nearest integer
    return int(round(final_value))

# System state configuration (critical)
system_state = {
    'mode': 'NORMAL',
    'version': '2.1.5',
    'debug': False,
    'norm': 'linear'
}

# Log data preprocessing (adds distraction)
processed_entries = []
for entry in telemetry_stream:
    entry_copy = entry.copy()
    entry_copy['temp_f'] = entry['temp'] * 9/5 + 32
    processed_entries.append(entry_copy)

# Distractor: string-based event logging
log_template = "Event at {timestamp}: Sensor {sensor_id} recorded {value}"
event_log = []
for entry in telemetry_stream:
    message = log_template.format(timestamp=entry['timestamp'], sensor_id='S1', value=entry['signal'])
    event_log.append(message.upper())

# Actual execution point
log_data = telemetry_stream
final_diagnostic = process_metrics(log_data, system_state)
print(f"Result: {final_diagnostic}")