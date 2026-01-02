import itertools

# Simulated aerospace telemetry diagnostics with embedded red herrings
def process_telemetry_chunk(chunk_data, mode):
    if mode == 'safe':
        return sum(x ** 2 for x in chunk_data if x > 0) // (len(chunk_data) or 1)
    else:
        return sum(abs(x) for x in chunk_data) % 97

# Irrelevant transformation - decoy function used nowhere
def encrypt_signal(data_stream):
    shifted = [(d * 11) % 256 for d in data_stream]
    return [s ^ 42 for s in shifted]

# Misleading fault simulator - looks important but unused
prev_fault_codes = [0x1A, 0x2F, 0x3C, 0x5D]
active_mask = 0b1101
calibration_offset = -17

# Core diagnostic logic chain
system_flags = {
    'voltage_stable': False,
    'thermal_ok': True,
    'comms_active': None,
    'redundancy_engaged': True
}

# Simulated telemetry time series with noise
raw_samples = [12, -5, 8, 19, 0, -3, 7, 14]
filtered_readings = [x for x in raw_samples if x != 0]

# Dead code path - unreachable due to control flow
if len(filtered_readings) < 5:
    fallback_mode = True
    secondary_buffer = [0] * 8
else:
    pass  # Placeholder - misleading no-op

# Real processing begins here
baseline = process_telemetry_chunk(filtered_readings, 'normal')

# Complex data restructuring with distractor operations
reading_pairs = list(itertools.combinations(filtered_readings, 2))
high_variance_pairs = [p for p in reading_pairs if abs(p[0] - p[1]) > 10]
skew_index = len(high_variance_pairs) * 3

# Phantom calibration sequence (unused)
temp_calibration = [x + calibration_offset for x in filtered_readings]
valid_calib = list(filter(lambda x: x > 0, temp_calibration))

# Critical state computation
status_weights = {
    'voltage_stable': 15,
    'thermal_ok': 25,
    'comms_active': 20,
    'redundancy_engaged': 40
}

# Weighted diagnostic score
health_score = 0
for flag, weight in status_weights.items():
    flag_value = bool(system_flags.get(flag, False))
    health_score += weight * (1 if flag_value else 0)

# Decoy aggregate metrics
phantom_metric_1 = sum(pow(x, 2) for x in itertools.islice(itertools.cycle([2,3]), 10))
phantom_metric_2 = ''.join(map(str, [skew_index, baseline]))

# Main telemetry log structure - core input
telemetry_log = {
    'timestamps': list(range(100, 100 + len(raw_samples))),
    'readings': raw_samples,
    'checksum': sum(raw_samples) ^ 0xFF
}

# Central analysis function with multiple concerns
def analyze_fault_sequence(log_entry, flags):
    readings = log_entry['readings']
    
    # Distractor: complex but unused bit manipulation
    magic_key = 0
    for i, val in enumerate(readings):
        magic_key ^= (val << 1) | (i & 1)
    
    # Compute rolling window average (relevant)
    window_avg = sum(readings[i:i+3]) / 3 for i in range(len(readings) - 2)
    avg_val = sum(window_avg) / len(list(window_avg)) if readings else 0
    
    # Boolean logic cascade with short-circuiting
    critical_alert = not flags['voltage_stable'] and (flags['comms_active'] or flags['redundancy_engaged'])
    warning_level = (avg_val > 10) or (len(readings) % 2 == 1)
    
    # Modular arithmetic component
    checksum_mod = log_entry['checksum'] % 13
    
    # Integer division and rounding
    base_diagnostic = int(avg_val // 1.5) * 10
    
    # Key logic step: combine health score with reading characteristics
    adjustment = 0
    if critical_alert:
        adjustment -= 15
    if warning_level:
        adjustment += 8
    
    # Final composition using modular constraint
    intermediate = (base_diagnostic + health_score + adjustment) % 1000
    final = (intermediate * 2) - (checksum_mod * 4)
    
    # Dead code - unreachable assignment
    if False:
        final = final ^ 0xDEADBEEF
        
    return final

# Execution point of interest
final_diagnostic = analyze_fault_sequence(telemetry_log, system_flags)
print(f"Result: {final_diagnostic}")