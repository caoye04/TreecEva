import math

# Simulated sensor fusion system for environmental monitoring
base_threshold = 72.5
noise_floor = 4.3
calibration_factor = 1.08

# Raw data from multiple sensors (simulated)
sensor_a = [68, 71, 75, 79, 85, 83, 77]
sensor_b = [70, 73, 74, 80, 86, 82, 76]
sensor_c = [69, 70, 76, 78, 88, 81, 75]

# Irrelevant auxiliary arrays (distractor)
aux_data_1 = [1, 1, 2, 3, 5, 8, 13]
aux_data_2 = ['x', 'y', 'z']
accumulated_bias = 0.0

# Misleading pre-processing (dead path)
def legacy_filter(data):
    return [x * 0.95 for x in data if x > 70]  # Unused function

# Signal conditioning with noise correction
def apply_calibration(raw_values):
    calibrated = []
    for val in raw_values:
        adjusted = (val + noise_floor) * calibration_factor
        if adjusted > base_threshold:
            calibrated.append(adjusted)
    return calibrated

# Fusion logic with set operations and filtering
processed_signals = []
for i in range(len(sensor_a)):
    avg_raw = (sensor_a[i] + sensor_b[i] + sensor_c[i]) / 3
    if avg_raw >= base_threshold - 5:
        processed_signals.append(avg_raw)

# Apply calibration to fused signals
processed_signals = apply_calibration(processed_signals)

# Introduce irrelevant transformation chain (red herring)
shadow_copy = [x * 0.99 for x in processed_signals]
decay_correction = sum([math.exp(-x/100) for x in shadow_copy])

# Critical diagnostic analysis using recursion and set logic
def recursive_anomaly_score(data, index=0, depth=0):
    if depth >= 3 or index >= len(data) - 1:
        return int(abs(data[index] - base_threshold)) if index < len(data) else 0
    jump = int(data[index + 1] - data[index])
    sub_score = recursive_anomaly_score(data, index + 1, depth + 1)
    return (jump ** 2) + (sub_score // 2)

# Secondary analysis with list comprehension and set ops (partial distractor)
outlier_bounds = {min(processed_signals) - 5, max(processed_signals) + 5}
filtered_diagnostics = [
    x for x in processed_signals 
    if not (x < min(outlier_bounds) or x > max(outlier_bounds))
]

# Compute safety margin (misleading intermediate)
safety_margin = (max(processed_signals) - min(processed_signals)) / 2
adjustment_log = []
for _ in range(3):
    adjustment_log.append(safety_margin * 0.1)
    safety_margin *= 0.9  # Decoy evolution

# Real computation path begins here
aggregated_diagnostic = sum(
    [int(x) % 10 for x in processed_signals]
) + len(processed_signals)

# Final analysis combining multiple concepts
def analyze_readings(readings):
    # Use of set to deduplicate rounded values
    unique_bases = list(set([int(r) for r in readings]))
    
    # List comprehension with conditional logic
    scores = [recursive_anomaly_score(readings, i) for i in range(0, len(readings), 2)]
    
    # Irrelevant sorting (distractor)
    sorted_bases = sorted(unique_bases, reverse=True)
    temp_weight = sum(sorted_bases[:2]) if len(sorted_bases) > 1 else sorted_bases[0]
    
    # Actual contributing factor
    base_score = sum(scores)
    penalty = 0
    for s in readings:
        if s > base_threshold + 10:
            penalty += 5
    
    # Core result formation
    final_component = base_score - penalty + temp_weight // 10
    return final_component

# Execution point of interest
final_diagnostic = analyze_readings(processed_signals)

# Output required format
print(f"Result: {final_diagnostic}")