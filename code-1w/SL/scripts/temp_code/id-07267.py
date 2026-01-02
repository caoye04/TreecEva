import math

# Simulated sensor data preprocessing for environmental monitoring system
data_stream = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
offset_calibration = 0.87
scaling_factor = 1.04

# Irrelevant baseline constants for other sensors (distractors)
pressure_baseline = 1013.25
humidity_floor = 40
voltage_cap = 3.3
thermal_buffer = [0.1, 0.4, 0.7]

# Real-time filtering with moving window (unused path - dead code)
def apply_noise_filter(signal):
    return [signal[i] for i in range(1, len(signal)-1) if i % 2 == 1]

# Data transformation pipeline
raw_offsets = list(map(lambda x: x * scaling_factor + offset_calibration, data_stream))

# Bit manipulation for error checking (red herring - not used in final result)
checksum = 0
for val in data_stream:
    shifted = (val << 2) ^ 0b1010
    checksum += shifted & 0b1111

# Slice critical subset for analysis
trimmed_data = raw_offsets[2:7]

# Secondary transformation using list comprehension with conditional logic
doubled_filtered = [round(x * 2) for x in trimmed_data if x > 8.5]

# Simulate threshold detection (misleading intermediate metric)
exceedance_count = 0
for reading in doubled_filtered:
    if reading > 20:
        exceedance_count += 1

# Decoy function that looks important but is never called
def compute_robustness_index(seq, tolerance=0.95):
    return sum([abs(seq[i] - seq[i+1]) for i in range(len(seq)-1)]) * tolerance

# Define thresholds for diagnostic classification (used later)
thresh_config = {
    'low_risk': 15,
    'moderate_risk': 25,
    'high_risk': 35
}

# Transform data using exponential smoothing (actual relevant path)
smoothed_data = []
smoothing_constant = 0.3
if len(doubled_filtered) > 0:
    smoothed_data.append(doubled_filtered[0])
    for i in range(1, len(doubled_filtered)):
        new_val = smoothing_constant * doubled_filtered[i] + (1 - smoothing_constant) * smoothed_data[-1]
        smoothed_data.append(round(new_val, 2))

# Aggregate metrics function combining multiple concepts
def aggregate_metrics(series, limits):
    if not series:
        return -1
    
    # Summation and accumulation
    total = sum(series)
    count = len(series)
    
    # Boolean logic and comparisons
    high_alerts = sum(1 for x in series if x > limits['high_risk'])
    medium_alerts = sum(1 for x in series if x > limits['moderate_risk'])
    
    # Complex conditional with nested logic
    if high_alerts > 0:
        base_score = total * 1.5
    elif medium_alerts > 1:
        base_score = total * 1.2
    else:
        base_score = total * 0.8
    
    # Final adjustment using arithmetic and rounding
    adjusted_score = math.floor(base_score / count)
    
    # Apply bit-based mask as final obfuscation (effect is minimal)
    mask = 0b11111111
    result = adjusted_score & mask
    
    return result

# Unused alternate aggregation method (dead path)
calculate_resilience = lambda seq: sum([x**0.5 for x in seq]) / len(seq) if seq else 0

# Critical execution point
transformed_data = smoothed_data
final_diagnostic = aggregate_metrics(transformed_data, thresh_config)

# Print target result
print(f"Target result: {final_diagnostic}")