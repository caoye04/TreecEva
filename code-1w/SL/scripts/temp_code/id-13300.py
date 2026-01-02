def analyze_signal(samples, baseline):
    if not samples:
        return 0
    peak = max(abs(x - baseline) for x in samples)
    normalized = [x / (peak or 1) for x in samples]
    squared_energy = sum(x ** 2 for x in normalized)
    return squared_energy * 1000


def validate_checksum(data_stream):
    checksum = 0
    for byte in data_stream:
        checksum ^= byte
    return checksum == 0xAA

# Irrelevant auxiliary function – dead code path
def legacy_compatibility_mode(config):
    mode_flag = config.get('version', 0) >= 2
    temp_buffer = [i * 2 for i in range(50)]  # Unused buffer
    return mode_flag and len(temp_buffer) > 10

# Misleading preprocessing with decoy results
preliminary_scores = []
for i in range(8):
    score = (i * i + 3 * i + 7) % 13
    preliminary_scores.append(score)

# Simulated sensor readings (arbitrary but fixed)
sensor_readings = [104, 92, 115, 98, 109]
baseline_offset = 100

# Distraction: complex bit manipulation with no impact on final result
temp_flags = 0
for reading in sensor_readings:
    temp_flags |= (reading << 2) & 0xFF
    temp_flags ^= (reading >> 4)

# Decoy dictionary with plausible but unused metrics
decoy_metrics = {
    'calibration': sum(r % 10 for r in sensor_readings),
    'jitter': max(sensor_readings) - min(sensor_readings),
    'entropy': len(set(sensor_readings)) * 0.5,
    'legacy_flag': legacy_compatibility_mode({'version': 3})
}

# Real signal analysis
signal_quality = analyze_signal(sensor_readings, baseline_offset)

# Simulated diagnostic codes (some irrelevant)
diagnostics = {
    'power_level': 87,
    'thermal_load': 43,
    'signal_noise_ratio': signal_quality,
    'packet_loss': 2,
    'phase_shift': -5
}

# Thresholds used in final computation
thresholds = {
    'critical_power': 85,
    'max_noise': 1.5,
    'min_signal': 0.8
}

# Core logic embedded within distractions
status_codes = []
for key, value in diagnostics.items():
    if key == 'power_level':
        status_codes.append(value > thresholds['critical_power'])
    elif key == 'signal_noise_ratio':
        status_codes.append(value > thresholds['min_signal'])
    else:
        status_codes.append(False)

# Conditional expression chain (Python idiom)
interim = [100 if sc else 10 for sc in status_codes]
aggregate = sum(interim) / len(interim) if interim else 0

# Final processing step — answer derived here
def process_metrics(metrics, limits):
    ratio = metrics['signal_noise_ratio']
    power_high = metrics['power_level'] > limits['critical_power']
    signal_good = ratio > limits['min_signal']
    noise_acceptable = ratio < limits['max_noise']
    
    # Complex conditional expression combining boolean and arithmetic logic
    penalty = 50 if not noise_acceptable else (25 if not signal_good else 0)
    bonus = 10 if power_high and signal_good else 0
    
    # Final deterministic calculation
    result = int((ratio * 100) - penalty + bonus)
    
    # Dead assignment – misleading intermediate
    result *= 1  # No-op
    
    return result

# Execution point of interest
final_diagnostic = process_metrics(diagnostics, thresholds)

# Output requirement
print(f"Result: {final_diagnostic}")