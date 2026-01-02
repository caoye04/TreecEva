from itertools import combinations
from math import log2

# Sensor simulation data (simulated voltage readings over time)
sensor_a_readings = [1.2, 1.5, 0.9, 2.3, 1.8, 2.1, 1.6, 0.7]
sensor_b_readings = [1.4, 1.3, 1.0, 2.2, 1.9, 2.0, 1.5, 0.8]
sensor_c_readings = [1.1, 1.6, 0.8, 2.4, 1.7, 2.2, 1.4, 0.9]

# Irrelevant calibration constants (distractor)
CALIBRATION_OFFSET_A = 0.03
CALIBRATION_OFFSET_B = -0.02
CALIBRATION_OFFSET_C = 0.01
BASELINE_DRIFT = 0.005

# Apply meaningless offset adjustments (red herring - not used later)
adjusted_a = [v + CALIBRATION_OFFSET_A + BASELINE_DRIFT for v in sensor_a_readings]
adjusted_b = [v + CALIBRATION_OFFSET_B + BASELINE_DRIFT for v in sensor_b_readings]
adjusted_c = [v + CALIBRATION_OFFSET_C + BASELINE_DRIFT for v in sensor_c_readings]

# Fused signal computation (unused distractor path)
fused_signal = [sum(x) / 3 for x in zip(adjusted_a, adjusted_b, adjusted_c)]
smoothed_fused = [fused_signal[i] if i == 0 else (fused_signal[i] + fused_signal[i-1]) / 2 for i in range(len(fused_signal))]

# Real processing begins: detect anomalies above dynamic thresholds
def compute_dynamic_thresholds(readings):
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    return {'mean': avg, 'threshold': avg + variance ** 0.5}

# Compute thresholds for each sensor (only 'mean' and 'threshold' are relevant)
thresh_a = compute_dynamic_thresholds(sensor_a_readings)
thresh_b = compute_dynamic_thresholds(sensor_b_readings)
thresh_c = compute_dynamic_thresholds(sensor_c_readings)

# Decoy entropy calculation (dead code - looks important but unused)
entropy_a = sum(-p * log2(p) for p in [x/sum(sensor_a_readings) for x in sensor_a_readings if x > 0])
entropy_b = sum(-p * log2(p) for p in [x/sum(sensor_b_readings) for x in sensor_b_readings if x > 0])
entropy_c = sum(-p * log2(p) for p in [x/sum(sensor_c_readings) for x in sensor_c_readings if x > 0])

# Threshold map with only needed fields
threshold_map = {
    'A': thresh_a['threshold'],
    'B': thresh_b['threshold'],
    'C': thresh_c['threshold']
}

# Simulate packetized data with metadata (complex structure with irrelevant fields)
raw_packets = [
    {'data': a, 'meta': {'id': f'A{i}', 'seq': i, 'flag': (i % 3 == 0), 'debug': f'dbg_{i}'}, 'sensor': 'A'} for i, a in enumerate(sensor_a_readings)
] + [
    {'data': b, 'meta': {'id': f'B{i}', 'seq': i, 'flag': (i % 2 == 0), 'debug': f'trace_{i}'}, 'sensor': 'B'} for i, b in enumerate(sensor_b_readings)
] + [
    {'data': c, 'meta': {'id': f'C{i}', 'seq': i, 'flag': (i % 4 == 0), 'debug': f'log_{i}'}, 'sensor': 'C'} for i, c in enumerate(sensor_c_readings)
]

# Extract only valid entries above 1.0V and sort by data value (linear filter)
valid_entries = [p for p in raw_packets if p['data'] > 1.0]
sorted_entries = sorted(valid_entries, key=lambda x: x['data'])

# Group by sensor (dictionary accumulation)
grouped_data = {}
for entry in sorted_entries:
    sensor = entry['sensor']
    if sensor not in grouped_data:
        grouped_data[sensor] = []
    grouped_data[sensor].append(entry['data'])

# Filter readings based on dynamic thresholds (core logic)
filtered_data = {}
for sensor, readings in grouped_data.items():
    t = threshold_map[sensor]
    filtered_data[sensor] = [r for r in readings if r > t]

# Analyze filtered readings using combinatorics and set logic
def analyze_readings(data_dict, thresholds):
    result_set = set()
    total_exceedances = 0
    
    # Process each sensor's filtered data
    for sensor, values in data_dict.items():
        threshold = thresholds[sensor]
        total_exceedances += len(values)
        # Add unique pattern codes based on value combinations
        if len(values) >= 2:
            # Generate all 2-element combinations (itertools usage)
            for pair in combinations(values, 2):
                # Use bit manipulation to encode pattern (bitwise operation)
                code = int((pair[0] * 10) % 8) ^ int((pair[1] * 10) % 8)  # XOR of scaled fractional bits
                result_set.add(code)
    
    # Additional decoy transformation (not affecting final result)
    transformed_codes = [c * 2 + 1 for c in result_set]
    sorted_transformed = sorted(transformed_codes, reverse=True)
    
    # Final diagnostic computed from size of unique patterns and total exceedances
    diagnostic_weight = len(result_set) * 100
    secondary_factor = total_exceedances * 10
    
    # Only this line determines the answer
    final_diagnostic = diagnostic_weight + secondary_factor
    
    # Dead code branches (misleading)
    if len(result_set) > 10:
        final_diagnostic -= 500  # never reached
    elif sum(result_set) % 7 == 0:
        final_diagnostic += 100  # never reached
    
    return final_diagnostic

# Execute main analysis
final_diagnostic = analyze_readings(filtered_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")