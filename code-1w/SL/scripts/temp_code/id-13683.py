from collections import defaultdict, Counter

# Simulated sensor array data from a spacecraft subsystem
sensor_ids = ['S1', 'S2', 'S3', 'S4', 'S5']
timestamps = [100, 105, 110, 115, 120]
raw_readings = [
    [0.85, 0.91, 0.78, 0.88, 0.90],
    [0.83, 0.89, 0.77, 0.85, 0.87],
    [0.86, 0.92, 0.79, 0.89, 0.91],
    [0.84, 0.90, 0.76, 0.86, 0.88],
    [0.87, 0.93, 0.80, 0.90, 0.92]
]

# Irrelevant auxiliary data (distractor)
calibration_offsets = {'S1': 0.02, 'S2': -0.01, 'S3': 0.03, 'S4': 0.00, 'S5': 0.01}
deprecated_sensors = ['S6', 'S7']
redundant_flag = True

# Misleading preprocessing (dead path)
def apply_calibration(readings, offsets):
    return [[val + offsets[f'S{i+1}'] for i, val in enumerate(row)] for row in readings]

calibrated = apply_calibration(raw_readings, calibration_offsets)  # Computed but unused

# Extract time-series per sensor using zip and enumerate (relevant)
sensor_data = {}
for i, sensor in enumerate(sensor_ids):
    sensor_data[sensor] = [raw_readings[t][i] for t in range(len(timestamps))]

# Compute rolling average over last 3 timestamps (key transformation)
recent_averages = {}
for sensor, values in sensor_data.items():
    recent_averages[sensor] = sum(values[-3:]) / 3

# Baseline thresholds derived from nominal behavior
baseline_readings = {
    'S1': 0.84, 'S2': 0.91, 'S3': 0.78, 'S4': 0.87, 'S5': 0.89
}

# Health signature: deviation classification
health_signature = []
for sensor in sensor_ids:
    avg = recent_averages[sensor]
    baseline = baseline_readings[sensor]
    if abs(avg - baseline) < 0.01:
        health_signature.append(0)
    elif avg > baseline:
        health_signature.append(1)
    else:
        health_signature.append(-1)

# Auxiliary statistical analysis (distractor)
frequency_count = Counter(health_signature)
flag_threshold_exceeded = any([v > 2 for v in frequency_count.values()])

# Complex nested processing function with red herrings
status_log = []
error_accumulator = defaultdict(int)


def analyze_component_health(signature, map_ref):
    code_phase = 0
    diagnostic_score = 0
    mode_weights = [0.5, 1.0, 1.5]

    # Use of enumerate and complex control flow
    for idx, flag in enumerate(signature):
        if idx % 2 == 0:
            code_phase ^= 1
            # Bit manipulation decoy
            diagnostic_score += (flag << 1) & 3
        else:
            # Unused logical branch
            temp_state = (flag + code_phase) or 5
            error_accumulator[f'mode_{temp_state}'] += 1

    # Real logic hidden among distractions
    aggregate = sum(abs(x) for x in signature)
    severity = aggregate * 10

    # Conditional expression with tuple unpacking (idiomatic python)
    action, level = ('reset', 3) if severity > 30 else ('monitor', 1)
    status_log.append(f'{action}:{level}')

    # Actual contribution to final result
    return severity + len(map_ref.keys())


# Secondary distraction: system mode simulation
current_mode = 'STANDBY'
mode_registry = {0: 'INIT', 1: 'ACTIVE', 2: 'STANDBY', 3: 'DIAGNOSTIC'}
for k, v in mode_registry.items():
    if v == current_mode:
        current_mode = mode_registry.get(k-1, 'UNKNOWN')

# Core computation disguised among irrelevant operations
temp_buffer = [x for x in range(8) if x % 2 == 0]
buffer_sum = sum(temp_buffer)  # Distractor computation

# Final processing with slicing and zip
extended_signature = health_signature + [health_signature[0]]
paired_diffs = [abs(a - b) for a, b in zip(extended_signature[:-1], extended_signature[1:])]
smoothed_value = sum(paired_diffs[1:-1]) / len(paired_diffs[1:-1]) if len(paired_diffs) > 2 else 0


def process_metrics(sig, base):
    # Multiple concepts: dict lookup, list comp, arithmetic, conditionals
    base_factor = sum(base.values()) * 0.1
    sig_parity = sum(1 for x in sig if x > 0) >= sum(1 for x in sig if x < 0)
    adjustment = base_factor if sig_parity else -base_factor

    # Critical use of slicing and enumeration
    weighted_sum = 0
    for i, val in enumerate(sig[::2]):  # Every other element
        weighted_sum += val * (i + 1)

    # Hidden correct path: combine weighted signal and base adjustment
    intermediate = abs(weighted_sum) * 100 + adjustment

    # Dead branches and decoy variables
    if intermediate < 0:
        final = intermediate ** 2
    else:
        final = int(intermediate)  # This is taken

    # One more distraction: unused tuple unpacking
    metadata_tags = ['VERIFIED', 'ENCRYPTED', 'LOGGED']
    if len(metadata_tags) == 3:
        status, _, _ = metadata_tags  # Unrelated

    return final


# Execute main logic
final_diagnostic = process_metrics(health_signature, baseline_readings)

# Print result as required
print(f"Result: {final_diagnostic}")