def analyze_pattern(sequence):
    count = 0
    for s in sequence:
        if len(s) > 3 and 'x' in s:
            count += 1
    return count

# Simulate sensor data stream
data_stream = ['ax1', 'bx2', 'txt', 'xyz9', 'nope']
pattern_count = analyze_pattern(data_stream)

# System calibration parameters (some are red herrings)
calib_a = 1.5
calib_b = -0.7
offset_x = pattern_count * calib_a
offset_y = offset_x * calib_b  # Unused downstream

# Base performance metrics from subsystems
base_metrics = {
    'response_time': 42,
    'throughput': 87,
    'error_rate': 0.05
}

# Bonus logic based on string-derived flags
diagnostic_codes = ['ERR_X', 'OK_Z', 'WARN_Y', 'OK_Q']
bonus_flags = [code for code in diagnostic_codes if code.startswith('OK')]
bonus_multiplier = len(bonus_flags) * 2 if bonus_flags else 1

# Irrelevant aggregation (distractor)
temp_aggr = sum(len(code) for code in diagnostic_codes) // len(diagnostic_codes)

# Core scoring logic
raw_score = (base_metrics['response_time'] + 
             base_metrics['throughput']) * (1 - base_metrics['error_rate'])

# Additional noise variables
dummy_shift = temp_aggr << 2
flag_hash = hash(tuple(bonus_flags)) % 100  # Not used

# Final adjustment using bonus flags
def calculate_performance(flags, metrics):
    base = raw_score  # Capture outer scope variable
    adjustment = 0
    for flag in flags:
        if 'Z' in flag:
            adjustment += 5
        elif 'Q' in flag:
            adjustment += 3
    return int(base + adjustment * bonus_multiplier)

# Execution point of interest
final_score = calculate_performance(bonus_flags, base_metrics)

print(f"Result: {final_score}")