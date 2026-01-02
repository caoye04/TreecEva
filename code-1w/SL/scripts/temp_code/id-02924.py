import math

# Simulated sensor diagnostics system with red herrings and distractors
def analyze_signal_strength(signal):
    if signal > 90:
        return 'strong'
    elif signal > 50:
        return 'moderate'
    else:
        return 'weak'

# Irrelevant helper (dead function - never called)
def legacy_calibrate(x):
    return (x * 1.07) + 3.2

# Unused transformation (distractor)
transform_map = {
    'A': lambda x: x ** 2,
    'B': lambda x: x + 100,
    'C': lambda x: abs(x - 10)
}

# Sensor data with embedded noise and metadata
sensor_data = [
    {'id': 'S1', 'reading': 68.4, 'type': 'temperature', 'timestamp': 1678886400},
    {'id': 'S2', 'reading': 73.1, 'type': 'humidity', 'timestamp': 1678886405},
    {'id': 'S3', 'reading': 59.7, 'type': 'pressure', 'timestamp': 1678886410},
    {'id': 'S4', 'reading': 81.2, 'type': 'light', 'timestamp': 1678886415},
    {'id': 'S5', 'reading': 44.3, 'type': 'motion', 'timestamp': 1678886420}
]

# Threshold configuration (some keys are irrelevant)
thresholds = {
    'critical': 75.0,
    'warning': 60.0,
    'normal': 50.0,
    'offset_correction': 0.8,  # unused in logic
    'max_history': 10          # red herring
}

# Misleading accumulator (used in decoy path)
total_anomalies = 0
anomaly_log = []

# Decoy processing function (never invoked)
def generate_summary_report(data_list):
    stats = {}
    for item in data_list:
        t = item['type']
        if t not in stats:
            stats[t] = []
        stats[t].append(item['reading'])
    return {k: sum(v)/len(v) for k, v in stats.items()}

# Key processing function with complex control flow and distractors
def process_readings(data, config):
    cumulative_score = 0.0
    diagnostic_flags = []
    temp_buffer = []  # unused buffer - distraction

    # Real logic begins here
    for entry in data:
        val = entry['reading']
        reading_type = entry['type']

        # Bitwise flag encoding based on thresholds (relevant)
        flag = 0
        if val >= config['critical']:
            flag |= 0b100  # critical bit
        if val >= config['warning']:
            flag |= 0b010   # warning bit
        if val < config['normal']:
            flag |= 0b001    # low bit

        # Apply non-linear adjustment only for certain types
        adjusted = val
        if reading_type in ['temperature', 'light']:
            adjusted = math.log(val) * 10  # transform

        # Accumulate adjusted value only for specific pattern
        if 'S' in entry['id'] and int(entry['id'][1]) % 2 == 0:
            cumulative_score += adjusted

        # Store flag for later analysis
        diagnostic_flags.append(flag)

    # Secondary analysis on flags (bit manipulation)
    flag_sum = 0
    for f in diagnostic_flags:
        # Count set bits (Hamming weight)
        while f:
            flag_sum += f & 1
            f >>= 1

    # Complex conditional involving multiple concepts
    if len(diagnostic_flags) > 3:
        base = cumulative_score
        modifier = flag_sum * 1.5
        outcome = base + modifier
    else:
        outcome = cumulative_score

    # Red herring: slicing operation with no effect
    shadow_copy = diagnostic_flags[1:3]
    shadow_copy.reverse()

    # Final computation using lambda (required feature)
    finalize = lambda x: round(x * 1.02, 4)
    final_value = finalize(outcome)

    # Distractor: dictionary operations not affecting result
    summary_stats = {
        'count': len(data),
        'flags': diagnostic_flags,
        'derived': [round(math.sqrt(x), 2) for x in [flag_sum, int(cumulative_score)]]
    }

    # The real answer flows through here
    return final_value

# Execution point of interest
final_diagnostic = process_readings(sensor_data, thresholds)

# Print required output
print(f"Result: {final_diagnostic}")