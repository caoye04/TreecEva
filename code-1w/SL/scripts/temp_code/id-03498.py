from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation (distractor: some values are irrelevant)
sensor_nodes = ['temp_1', 'temp_2', 'pressure_a', 'pressure_b', 'flow_x', 'flow_y']
raw_readings = [
    [36.8, 37.1, 36.9, 37.0, 37.2],
    [37.5, 37.6, 37.4, 37.5, 37.7],
    [101.2, 101.5, 101.3, 101.4, 101.6],
    [102.1, 102.3, 102.0, 102.2, 102.4],
    [1.2, 1.3, 1.1, 1.25, 1.35],
    [1.8, 1.75, 1.85, 1.78, 1.82]
]

# Irrelevant preprocessing: normalizing unrelated sensor types (red herring)
normalized = []
for readings in raw_readings:
    mean_val = sum(readings) / len(readings)
    normalized.append([r / mean_val for r in readings])

# Mapping data to nodes (partially relevant)
data_map = dict(zip(sensor_nodes, raw_readings))
normalized_map = dict(zip(sensor_nodes, normalized))

# Extract only temperature-related data for health diagnostics (critical path)
temp_data = []
for key in data_map:
    if key.startswith('temp_'):
        temp_data.extend(data_map[key])

# Distractor: complex but unused pressure correlation analysis
def compute_pressure_correlation():
    p_a = data_map['pressure_a']
    p_b = data_map['pressure_b']
    cov = sum((p_a[i] - sum(p_a)/len(p_a)) * (p_b[i] - sum(p_b)/len(p_b)) for i in range(len(p_a)))
    return cov / len(p_a)

# Unused function — dead code path (distractor)
unused_result = compute_pressure_correlation()

# Threshold calibration using string patterns (semi-relevant abstraction)
def get_dynamic_thresholds(baseline, variation_factor='medium'):
    factor_map = {'low': 0.5, 'medium': 1.0, 'high': 1.5}
    factor = factor_map.get(variation_factor, 1.0)
    return {
        'high': baseline + (0.8 * factor),
        'low': baseline - (0.6 * factor)
    }

# Bitwise flag simulation for system status (distractor with misleading use)
system_status_flags = 0b1101
is_stable = system_status_flags & 0b0001
is_calibrated = (system_status_flags >> 2) & 0b0001
flag_diagnostic = is_stable ^ is_calibrated  # XOR logic, not used later

# Core diagnostic logic (relevant)
thresholds = get_dynamic_thresholds(baseline=37.0, variation_factor='medium')
abnormal_count = 0
for temp in temp_data:
    if temp > thresholds['high'] or temp < thresholds['low']:
        abnormal_count += 1

# Auxiliary metrics from flow sensors (irrelevant to final result)
flow_set = set()
for key in data_map:
    if 'flow' in key:
        flow_set.update([round(x, 1) for x in data_map[key]])

# Distractor: set operations with no impact
complement_set = {1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9}
unused_intersection = flow_set & complement_set

# Health data structure creation (key input to final function)
health_data = {
    'temperatures': temp_data,
    'abnormalities': abnormal_count,
    'source_nodes': [k for k in data_map.keys() if k.startswith('temp')]
}

# Complex processing with decoy operations inside
def process_metrics(data, limits):
    temps = data['temperatures']
    count = data['abnormalities']
    
    # Red herring: entropy calculation on temperatures (not used in output)
    freq = Counter([round(t, 1) for t in temps])
    total = len(temps)
    entropy = -sum((count/total) * math.log2(count/total) for count in freq.values())
    
    # Dummy transformation chain
    transformed = []
    for t in temps:
        shifted = t * 1.002
        adjusted = abs(shifted - 0.001)
        transformed.append(adjusted)
    
    # Mean of transformed (decoy)
    transformed_mean = sum(transformed) / len(transformed)
    
    # Critical path: use abnormal_count and apply bitwise-weighted adjustment
    # Weight based on number of source nodes (only 2: temp_1, temp_2)
    node_count = len(data['source_nodes'])
    adjustment_factor = (node_count << 2)  # left shift by 2 => multiply by 4
    
    # Final computation: count squared plus adjustment (actual answer path)
    base_score = count ** 2
    final_value = base_score + adjustment_factor
    
    # Dead code branch: never executed due to constant condition
    if entropy < 0:
        final_value -= int(transformed_mean)
    
    return int(final_value)

# Execute critical statement
final_diagnostic = process_metrics(health_data, thresholds)
print(f"Result: {final_diagnostic}")