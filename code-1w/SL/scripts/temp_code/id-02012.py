import math

# Simulated system telemetry data with mixed signal types
def generate_telemetry():
    timestamps = list(range(100, 200, 3))
    readings = [round(math.sin(i / 10) * 50 + 100, 2) for i in range(len(timestamps))]
    statuses = ['OK' if x % 7 != 0 else 'ERR' for x in range(len(timestamps))]
    return list(zip(timestamps, readings, statuses))

# Irrelevant helper: converts time to hex (unused path)
def timestamp_to_hex(ts_list):
    return [hex(t) for t in ts_list]

# Data validation filter (partially used)
def validate_readings(readings):
    valid = []
    for r in readings:
        if 50 <= r <= 150:
            valid.append(r)
    return valid

# Legacy function: computes outdated metric (decoy)
def compute_legacy_index(vals):
    acc = 0
    for v in vals[:20]:
        if v > 100:
            acc += int(v % 7)
    return acc * 1.5

# Core processing pipeline
def analyze_pattern(seq):
    count_rising = 0
    for i in range(1, len(seq)):
        if seq[i] > seq[i-1] and (i + seq[i]) % 4 == 0:
            count_rising += 1
    return count_rising

# Bit manipulation for 'encoding' (misleading intermediate)
def encode_flags(status_list):
    flag_acc = 0
    for s in status_list:
        if s == 'OK':
            flag_acc ^= 13
        else:
            flag_acc <<= 1
    return flag_acc

# Real-time drift detector (distractor with side calculation)
def detect_drift(values):
    avg = sum(values) / len(values)
    deviations = [abs(v - avg) for v in values]
    threshold = 1.8 * (sum(deviations) / len(deviations))
    spikes = [d for d in deviations if d > threshold]
    return len(spikes)

# Central configuration map (contains red herring keys)
config = {
    'threshold': 95.0,
    'window_size': 12,
    'debug_mode': False,
    'legacy_compat': True,
    'max_variance': 400,
    'use_enhanced': False  # Unused in logic
}

data_log = generate_telemetry()

# Extract components for analysis
raw_timestamps, raw_readings, system_statuses = zip(*data_log)

# Preprocess: filter valid range (relevant)
filtered_readings = validate_readings(raw_readings)

# Compute auxiliary metrics (some irrelevant)
legacy_metric = compute_legacy_index(filtered_readings)  # Dead end
spike_count = detect_drift(filtered_readings)           # Not used later
rising_trend = analyze_pattern(filtered_readings)       # Used in final calc
encoded_flag = encode_flags(system_statuses)             # Misleading, not used

# Simulate environmental interference compensation (distraction block)
compensation_factor = 0
for i, val in enumerate(filtered_readings):
    if i % 5 == 0 and val > config['threshold']:
        compensation_factor += math.log(val - 90) if val > 90 else 0
compensation_factor = round(compensation_factor, 2)

# Determine operational mode based on pattern (red herring)
current_mode = 'STANDARD'
if encoded_flag > 100:
    current_mode = 'SECURE'
elif legacy_metric > 50:
    current_mode = 'LEGACY'

# Key computation: efficiency score derivation
baseline = sum(filtered_readings) / len(filtered_readings)
variance = sum((x - baseline) ** 2 for x in filtered_readings) / len(filtered_readings)
penalty = 0
for i, val in enumerate(filtered_readings):
    if i % 7 == 0 and val < baseline:
        penalty += 1.5

# Critical statement: combines trend, variance, and penalty
efficiency_score = int(
    (rising_trend * 10) 
    - (variance / 5) 
    - penalty 
    + (len([s for s in system_statuses if s == 'OK']) // 10)
)

# Final aggregation layer (only efficiency_score matters)
def process_metrics(log_data, cfg):
    readings_only = [item[1] for item in log_data]
    valid_vals = validate_readings(readings_only)
    trend = analyze_pattern(valid_vals)
    base = sum(valid_vals) / len(valid_vals)
    var = sum((x - base) ** 2 for x in valid_vals) / len(valid_vals)
    p = sum(1.5 for i, v in enumerate(valid_vals) if i % 7 == 0 and v < base)
    ok_count_bonus = len([item for item in log_data if item[2] == 'OK']) // 10
    score = int((trend * 10) - (var / 5) - p + ok_count_bonus)
    return {
        'final_score': score,
        'diagnostics': {"drift": spike_count, "legacy": legacy_metric},
        'timestamp': raw_timestamps[-1]
    }

final_output = process_metrics(data_log, config)
efficiency_score = final_output['final_score']

Result: {efficiency_score}