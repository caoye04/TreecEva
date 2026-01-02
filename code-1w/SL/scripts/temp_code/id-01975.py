import itertools

# System health monitoring simulation with diagnostic interference

def monitor_subsystem(sensor_data, threshold=75):
    return list(filter(lambda x: x > threshold, sensor_data))

# Irrelevant helper (distractor)
def calculate_entropy(data):
    from math import log2
    total = sum(data)
    if total == 0:
        return 0
    probabilities = [x / total for x in data]
    return -sum(p * log2(p) for p in probabilities if p > 0)

# Unused function (dead code path)
def legacy_compatibility_mode():
    return {f'node_{i}': False for i in range(10)}

# Data preprocessing with red herring transformation
def preprocess_signal(raw_signal):
    shifted = [(x << 2) & 255 for x in raw_signal]  # Bit manipulation distraction
    smoothed = [sum(shifted[i:i+3]) / 3 for i in range(len(shifted) - 2)]
    return smoothed

# Core logic buried in noise
def validate_timing_consistency(log_entries):
    intervals = [log_entries[i+1] - log_entries[i] for i in range(len(log_entries) - 1)]
    tolerance = 0.1
    expected_interval = 1.0
    deviations = [abs(x - expected_interval) for x in intervals]
    return all(d < tolerance for d in deviations)

# Misleading diagnostic (decoy)
def assess_stability_index(telemetry):
    base_score = sum(telemetry) / len(telemetry)
    fluctuation_penalty = max(telemetry) - min(telemetry)
    return base_score - fluctuation_penalty * 0.3

# Key function - computes final diagnostic
def aggregate_metrics(timing_log, system_flags):
    valid_timing = validate_timing_consistency(timing_log)
    flag_count = sum(bool(f) for f in system_flags.values())
    
    # Real computation mixed with irrelevant transforms
    temp_buffer = [x * 1.05 for x in timing_log if x > 0.5]
    compressed = list(itertools.accumulate(temp_buffer, lambda a, b: a * 0.9 + b))
    
    # Actual decision logic (non-obvious)
    if valid_timing and flag_count < 3:
        return int(compressed[-1] * 1000) % 8971
    else:
        backup_ref = [1, 1]
        for i in range(2, 10):
            backup_ref.append(backup_ref[i-1] + backup_ref[i-2])  # Fibonacci decoy
        return (len(compressed) * 123) % 8971

# Simulated system data with embedded distractions
timing_log = [1.0, 2.0, 3.0, 4.0, 5.0]  # Perfect intervals

# Extraneous large data structure (distractor)
sensor_grid = [[i*j + 2 for j in range(8)] for i in range(8)]

# System flags - only 'overclock_detected' and 'fan_failure' matter indirectly
system_flags = {
    'overclock_detected': False,
    'fan_failure': True,
    'legacy_mode': True,
    'secure_boot': False,
    'thermal_throttle': False,
    'gpu_boost': True,
    'eco_mode': True
}

# Unused signal data (red herring)
raw_emg_signal = [12, 45, 67, 89, 23, 56, 78, 91, 14, 37]
processed_emg = preprocess_signal(raw_emg_signal)

# Fake diagnostic call (misleading)
stability = assess_stability_index([4.5, 4.7, 4.6, 4.8, 4.4])

# Critical execution point
final_diagnostic = aggregate_metrics(timing_log, system_flags)

# Print result as required
print(f"Result: {final_diagnostic}")