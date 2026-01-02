import math

def analyze_system_load(timestamps, thresholds):
    if not timestamps:
        return 0
    
    # Irrelevant transformation (red herring)
    normalized = [t % 86400 for t in timestamps if t > 0]
    spike_count = sum(1 for n in normalized if n > thresholds[0])
    
    # Distractor: complex but unused calculation
    baseline_adjustment = sum(math.sin(n / 1000) for n in normalized[:10]) if len(normalized) > 5 else 0
    adjusted_spikes = spike_count - int(abs(baseline_adjustment))

    # Real logic buried here
    valid_intervals = []
    for i in range(1, len(timestamps)):
        diff = timestamps[i] - timestamps[i-1]
        if 1 <= diff <= thresholds[1]:
            valid_intervals.append(diff)
    
    # This is actually used later
    interval_score = sum(v ** 0.5 for v in valid_intervals) if valid_intervals else 0.0
    
    # Dead code path (never reached due to prior logic)
    anomaly_flag = False
    if len([x for x in timestamps if x < 0]) > 2:
        anomaly_flag = True  # Never affects anything
        temp_result = ''.join([chr(i % 127) for i in timestamps])  # Obfuscated distraction
    
    return interval_score

# Simulate error detection with bit flags (mostly irrelevant)
def detect_errors(config_code):
    errors = 0
    if config_code & 0b1010:
        errors |= 0b0001
    if (config_code >> 3) & 1:
        errors ^= 0b1110
    if config_code < 0:
        errors += 7
    
    # Meaningless string transformation
    hex_trace = ''.join([hex(i)[-1] for i in range(config_code % 15) if i % 3 != 0])
    
    # Only this line matters
    return bin(errors).count('1') if config_code % 7 == 0 else 3

# Main processing chain
def aggregate_metrics(log_entries, error_flags):
    if not log_entries:
        return -1
    
    # Key data extraction
    durations = [entry['end'] - entry['start'] for entry in log_entries if 'start' in entry and 'end' in entry]
    
    # Distractor: elaborate but unused structure
    metadata_map = {f"frame_{i}": {"seq": i, "hash": (i*7 + 3) % 19} for i in range(len(log_entries))}
    
    # Real accumulation
    total_duration = sum(durations)
    filtered_durations = [d for d in durations if d > 100]
    bonus = 50 if len(filtered_durations) >= 2 else 0
    
    # Conditional expression with actual impact
    base_score = total_duration * 0.1 if total_duration > 500 else total_duration * 0.25
    
    # Critical dependency on error count
    penalty = error_flags * 17
    
    # Unused complex list comprehension
    derived_signals = [math.log(d+1) * (i % 4) for i, d in enumerate(durations) if d % 10 == 0]
    
    # Final computation (only this matters)
    result = int(base_score - penalty + bonus)
    
    # Decoy function call (no side effects)
    def noise_function():
        return ''.join(sorted('diagnostics', reverse=True))
    
    return result

# Execution begins here
config_settings = [14, 21, 7, 35]
timing_log = [
    {'start': 1000, 'end': 1200, 'type': 'A'},
    {'start': 1350, 'end': 1600, 'type': 'B'},
    {'start': 1700, 'end': 1750, 'type': 'A'}
]

# Irrelevant pre-processing
processed_config = []
for c in config_settings:
    shifted = (c << 2) ^ 0b1101
    processed_config.append(shifted % 100)

# Generate meaningless hash
config_hash = sum(c * (i+1) for i, c in enumerate(processed_config)) % 97

# Real usage
system_timestamps = [1000, 1350, 1700, 2100, 2600]
threshold_values = [300, 500]  # min, max interval bounds

# Call analysis (only return value used)
load_metric = analyze_system_load(system_timestamps, threshold_values)

# Error detection based on one config value (only 21 % 7 == 0 triggers meaningful branch)
errors_detected = sum(detect_errors(c) for c in config_settings)

# Core final computation
final_diagnostic = aggregate_metrics(timing_log, errors_detected)

print(f"Target result: {final_diagnostic}")