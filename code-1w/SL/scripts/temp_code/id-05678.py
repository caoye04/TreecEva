import math

# Simulated sensor data processing system with red herrings

def collect_telemetry():
    return [23.4, 18.9, 20.1, 25.3, 19.8, 22.0, 24.7, 17.6]

def calculate_baseline(samples):
    return sum(samples) / len(samples)

def apply_calibration(raw_value, factor=1.02):
    # Irrelevant calibration function (not actually used in final path)
    return raw_value * factor

def analyze_outliers(data, limit=21.0):
    outliers = []
    for x in data:
        if x > limit:
            outliers.append(x)
    return outliers  # Dead end: result not used later

def generate_checksum(sequence):
    # Distractor function: looks important but unused
    chk = 0
    for i, val in enumerate(sequence):
        chk ^= int(val) ^ i
    return chk

def filter_anomalies(stream, window_size=3):
    # Heavily nested logic with misleading intermediate steps
    cleaned = []
    temp_buffer = []
    for val in stream:
        temp_buffer.append(val)
        if len(temp_buffer) > window_size:
            temp_buffer.pop(0)
        avg_window = sum(temp_buffer) / len(temp_buffer)
        if abs(val - avg_window) < 3.5:
            cleaned.append(val)
    return cleaned  # Another decoy – this output is discarded

def compute_entropy(values):
    # Complex-looking but irrelevant computation
    norm_vals = [v / sum(values) for v in values]
    entropy = 0
    for p in norm_vals:
        if p > 0:
            entropy -= p * math.log(p)
    return round(entropy, 4)

def evaluate_stability(ratio):
    # Unused recursive red herring
    if ratio < 1.0:
        return evaluate_stability(1 / ratio)
    elif ratio > 1.5:
        return False
    return True

# Real processing chain begins here — subtle distinction from decoys
prelim_thresholds = {
    'warning': 20.5,
    'critical': 24.0
}

adjustment_factor = 1.07  # Misleading constant; looks like it should be used

lambda_transform = lambda x: x ** 0.8 + 2.1  # Used only once in core logic

raw_data = collect_telemetry()

# Apply non-linear transformation relevant to final calculation
processed_data = [lambda_transform(x) for x in raw_data]

# Core diagnostic logic buried among distractions
status_flags = {}
for idx, val in enumerate(processed_data):
    if val > lambda_transform(prelim_thresholds['critical']):
        status_flags[idx] = 'CRITICAL'
    elif val > lambda_transform(prelim_thresholds['warning']):
        status_flags[idx] = 'WARNING'
    else:
        status_flags[idx] = 'NORMAL'

# Actual key operation embedded deep in logic
flag_count = {
    'CRITICAL': sum(1 for f in status_flags.values() if f == 'CRITICAL'),
    'WARNING': sum(1 for f in status_flags.values() if f == 'WARNING'),
    'NORMAL': sum(1 for f in status_flags.values() if f == 'NORMAL')
}

# Secondary transformation using dictionary operations
severity_map = {'CRITICAL': 3, 'WARNING': 2, 'NORMAL': 1}
dynamic_weights = {k: v * 0.9 for k, v in severity_map.items()}  # Weight decay simulation

weighted_score = 0
for flag_type, count in flag_count.items():
    weighted_score += count * dynamic_weights[flag_type]

# Final aggregation step — answer derived here
baseline_shift = calculate_baseline(raw_data) - 20.0
final_diagnostic = int(weighted_score * 100 + baseline_shift)

# Print required result
print(f"Result: {final_diagnostic}")