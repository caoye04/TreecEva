import math

# Simulated telemetry data from satellite subsystems
telemetry_stream = [183, 211, 176, 244, 198, 205, 169, 223]

calibration_map = {
    'sensor_a': lambda x: (x >> 3) & 7,
    'sensor_b': lambda x: (x ^ 25) % 11,
    'sensor_c': lambda x: int(math.log2(x & -x)) if x != 0 else 0
}

# Irrelevant signal processing functions (dead code path)
def analyze_signal_strength(signal):
    peak = max(signal)
    avg = sum(signal) / len(signal)
    return (peak - avg) * 1.5


def normalize_readings(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) for x in data] if max_val > min_val else [0] * len(data)

# Misleading transformation chain (partially unused)
filtered_data = [x for x in telemetry_stream if x > 180]
scaled_data = [int(x * 0.85) for x in filtered_data]
ranked_data = sorted(scaled_data, reverse=True)

# Distractor: complex but unused data structure
system_health_profile = {
    'vitals': { 'core_temp': 67, 'voltage': 12.4, 'clock_speed': 2100 },
    'flags': { 'overheat': False, 'low_power': False, 'sync_lock': True },
    'metrics': [
        sum(telemetry_stream) // len(telemetry_stream),
        len([x for x in telemetry_stream if x % 2 == 0]),
        abs(telemetry_stream[0] - telemetry_stream[-1])
    ]
}

# Core diagnostic logic (buried among distractors)
def extract_signature(values, key_offset):
    result = 0
    for i, val in enumerate(values):
        if i % 2 == 0:
            result ^= (val + key_offset) & 255
        else:
            result += (val ^ key_offset) % 17
    return result % 1000

# Red herring function that looks important but isn't used in final calculation
def compute_integrity_check(data):
    checksum = 0
    for d in data:
        checksum = (checksum * 31 + d) % 97
    return checksum

# Real processing begins here
log_data = tuple(abs(x - 200) for x in telemetry_stream)
system_state = {
    'mode': 'DIAGNOSTIC',
    'version': 0x1A,
    'active_sensors': {'sensor_a', 'sensor_c'},
    'timestamp': 1718934400
}

# Secondary distraction: unused list comprehension with string ops
diag_labels = [f"CHK{str(i).zfill(2).upper()}" for i in range(len(telemetry_stream))]
label_mask = sum(ord(c) for c in ''.join(diag_labels[:4])) % 89

# Actual critical computation chain
intermediate_scores = []
for item in log_data:
    score = 0
    if item > 20:
        score += calibration_map['sensor_a'](item)
    if item < 40:
        score += calibration_map['sensor_b'](item)
    score += calibration_map['sensor_c'](item)
    intermediate_scores.append(score)

# Conditional expression and set operation influencing final result
evaluation_mode = 'FULL' if 'sensor_b' not in system_state['active_sensors'] else 'REDUCED'
mode_factor = 2 if evaluation_mode == 'FULL' else 1

# Key aggregation using lambda and conditional logic
aggregate_func = lambda scores: sum(s ** mode_factor for s in scores) % 888
raw_diagnostic = aggregate_func(intermediate_scores)

# Final transformation involving bitwise and arithmetic operations
temporal_key = system_state['timestamp'] & 255
final_diagnostic = (raw_diagnostic ^ temporal_key) + extract_signature(telemetry_stream, 13)

# Dead code: looks like logging but unused
audit_trail = [
    f"LOG:{ts}:VAL{abs(v-200)}" for ts, v in zip(
        range(system_state['timestamp'], system_state['timestamp']+len(telemetry_stream)), 
        telemetry_stream)
]

# This prints the actual answer
print(f"Result: {final_diagnostic}")