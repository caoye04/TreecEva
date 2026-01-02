import itertools

# Simulated sensor array data (real signal embedded in noise)
sensor_readings = [18, 21, 17, 23, 19, 25, 16, 20, 22, 18]

# Irrelevant backup calibration constants (distractor)
calibration_refs = [0.98, 1.02, 0.99, 1.01, 0.97]
offset_adjustment = sum(calibration_refs) * 0.1  # Unused in logic

# Noise filter threshold initialized (red herring variable)
temp_thresholds = [x > 20 for x in sensor_readings]

def smooth_signal(data, window=3):
    """Apply moving average to reduce noise."""
    smoothed = []
    for i in range(len(data)):
        start = max(0, i - window // 2)
        end = min(len(data), i + window // 2 + 1)
        smoothed.append(sum(data[start:end]) / (end - start))
    return smoothed

# Apply smoothing (relevant)
smoothed_signal = smooth_signal(sensor_readings)

# Frequency domain transformation attempt (mostly irrelevant)
fft_magnitude_estimate = [abs(x - 20) ** 0.5 for x in sensor_readings]  # Distractor

# Baseline normalization using conditional expression (relevant)
baseline = 20 if len(smoothed_signal) > 5 else 18
normalized_signal = [x - baseline + 1 for x in smoothed_signal]

# Generate phase-shifted duplicates for redundancy analysis (mixed relevance)
shifted_a = [normalized_signal[i-1] for i in range(len(normalized_signal))]
shifted_b = [normalized_signal[i-2] for i in range(len(normalized_signal))]

# Combine signals using XOR-based fusion (core relevant operation)
fused_signal = []
for a, b, c in zip(normalized_signal, shifted_a, shifted_b):
    fused_value = int(a) ^ int(b) | int(c)  # Bit manipulation
    fused_signal.append(fused_value)

# Create diagnostic map with false positives (distractor structure)
diagnostic_flags = {f'node_{i}': fused_signal[i] > 15 for i in range(len(fused_signal))}

# Build threshold map using itertools and conditional logic (relevant)
indices = list(range(len(fused_signal)))
threshold_map = dict(itertools.zip_longest(indices, [8, 6, 7], fillvalue=5))

# Decoy statistical summary (dead code path)
stats_summary = {
    'mean_fused': sum(fused_signal) / len(fused_signal),
    'peak_count': len([x for x in fused_signal if x > 10]),
    'valid_ratio': len([x for x, t in zip(fused_signal, threshold_map.values()) if x > t]) / len(fused_signal)
}  # Never used

# Secondary processing: isolate anomalies
anomalies = []
for i, val in enumerate(fused_signal):
    if val > threshold_map.get(i, 7):
        anomalies.append((i, val))

# Mock classification of anomaly types (irrelevant)
anomaly_classes = []
for idx, v in anomalies:
    cls = 'A' if v < 10 else 'B' if v < 15 else 'C'
    anomaly_classes.append(cls)

# Processed data container (key intermediate)
processed_data = {
    'sequence': fused_signal,
    'meta': {'origin': 'sensor_array_7', 'version': 0.9},
    'flags': diagnostic_flags  # Included but not fully used
}

# Redundant checksum verification (distractor function)
def validate_integrity(data_seq):
    xor_checksum = 0
    for x in data_seq:
        xor_checksum ^= int(x)
    return xor_checksum % 100

# Unused validation call (dead code)
integrity_score = validate_integrity(normalized_signal)

# Core analysis function with mixed logic paths
def analyze_signal(signal_dict, thresholds):
    raw_seq = signal_dict['sequence']
    total_power = 0
    event_count = 0
    
    for j, power_level in enumerate(raw_seq):
        # Conditional expression determining activation
        modifier = 1.5 if j % 3 == 0 else 0.8
        adjusted_power = power_level * modifier
        
        # Critical comparison
        if adjusted_power > thresholds.get(j, 6.0):
            total_power += adjusted_power
            event_count += 1
    
    # Final diagnostic score calculation (depends on prior state)
    if event_count == 0:
        return 0
    avg_power = total_power / event_count
    
    # Spurious secondary adjustment (misleading)
    if avg_power > 10:
        avg_power = avg_power * 0.9 + 2  # Artificial boost
    
    # Final mapping via bitwise interaction with count
    final_score = int(avg_power) ^ event_count | int(avg_power / 2)
    
    return final_score

# Execute critical statement
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")