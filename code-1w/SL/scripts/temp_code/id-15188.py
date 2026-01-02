import math

# Simulated sensor array data (real and decoy)
sensor_readings = [14.2, 18.7, 13.5, 21.0, 9.8, 16.3, 12.1, 19.4]
dummy_sensors = [0.0] * 8  # Unused dummy array as red herring

# Calibration parameters (some irrelevant)
baseline_offset = 3.1
scaling_factor = 0.95
temperature_compensation = lambda t: t * 1.02 if t > 15 else t * 0.98

# Irrelevant transformation chain
calibrated = []
for val in sensor_readings:
    temp_adj = temperature_compensation(val)
    adjusted = (temp_adj + baseline_offset) * scaling_factor
    calibrated.append(round(adjusted, 2))

# Signal processing pipeline
noise_floor = 12.5
signal_mask = [1 if x > noise_floor else 0 for x in calibrated]

# Decoy bit manipulation (unused)
masked_int = 0
for bit in signal_mask:
    masked_int = (masked_int << 1) | bit
inverted_mask = ~masked_int & 0xFF

# Real processing begins here
filtered_data = [sensor_readings[i] for i in range(len(calibrated)) if signal_mask[i]]

# Statistical summary (only mean is used later)
data_mean = sum(filtered_data) / len(filtered_data)
data_variance = sum((x - data_mean) ** 2 for x in filtered_data) / len(filtered_data)
data_median = sorted(filtered_data)[len(filtered_data)//2]

# Dictionary-based threshold system (core logic)
threshold_map = {
    'low': 13.0,
    'medium': 16.0,
    'high': 18.5
}

# Set operation to determine active bands (partial use)
active_bands = {k for k, v in threshold_map.items() if data_mean > v}
band_priority = {'high', 'medium'}  # Decoy set for distraction
conflict_zones = active_bands & band_priority  # Misleading intermediate

# Conditional data transformation
processed_data = []
for x in filtered_data:
    if data_mean > threshold_map['medium']:
        processed_data.append(x * 1.1 if x > threshold_map['low'] else x * 0.9)
    else:
        processed_data.append(x * 1.05)

# Core analysis function with red herrings
def analyze_signal(signal, thresholds):
    
    # Dead code path (never executed due to prior filtering)
    if len(signal) == 0:
        return -999.0  
    
    # Irrelevant local variables
    peak = max(signal)
    trough = min(signal)
    dynamic_range = peak - trough
    normalized = [x / peak for x in signal]
    
    # Decoy dictionary accumulation
    stats_log = {}
    for i, val in enumerate(normalized):
        if val > 0.7:
            stats_log[f'peak_{i}'] = val
    
    # Actual computation path
    mean_sig = sum(signal) / len(signal)
    adjustment_factor = 1.0
    
    # Complex conditional expression (used)
    adjustment_factor = 0.85 if 'high' in {k for k, v in thresholds.items() if mean_sig > v * 1.05} else 1.15
    
    # Final diagnostic calculation (this is the real answer)
    raw_diagnostic = mean_sig * adjustment_factor
    
    # Extra obfuscation layer
    final_weight = len([x for x in signal if x > thresholds['medium']])
    weighted_diagnostic = raw_diagnostic + (final_weight * 0.5)
    
    return round(weighted_diagnostic, 4)

# Execute main logic
dummy_result = sum(dummy_sensors)  # Red herring operation
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Output result
print(f"Result: {final_diagnostic}")