import math

# Simulated sensor data from wind turbine array
turbine_data = [
    {'id': 'T1', 'output_kw': 2150, 'vibration': 0.48, 'temp_c': 67, 'rpm': 1280},
    {'id': 'T2', 'output_kw': 2300, 'vibration': 0.33, 'temp_c': 71, 'rpm': 1310},
    {'id': 'T3', 'output_kw': 1950, 'vibration': 0.62, 'temp_c': 88, 'rpm': 1190},
    {'id': 'T4', 'output_kw': 2450, 'vibration': 0.29, 'temp_c': 63, 'rpm': 1350},
    {'id': 'T5', 'output_kw': 2000, 'vibration': 0.51, 'temp_c': 77, 'rpm': 1220}
]

# Irrelevant red herring: atmospheric conditions (not used in final calculation)
atmospheric_conditions = {
    'wind_speed_ms': 12.4,
    'direction_deg': 280,
    'humidity': 68,
    'pressure_hpa': 1013
}

# Decoy function: looks important but unused
def compute_efficiency_index(data_list):
    total_eff = 0
    for item in data_list:
        if item['temp_c'] > 80:
            total_eff += item['output_kw'] * 0.85
        else:
            total_eff += item['output_kw'] * 0.95
    return total_eff / len(data_list)

# Unused transformation path (dead code)
transformed_readings = []
for idx, reading in enumerate(turbine_data):
    transformed = {
        'index': idx,
        'adjusted_rpm': reading['rpm'] * (1 + 0.01 * math.sin(idx)),
        'thermal_load': reading['temp_c'] * reading['vibration']
    }
    transformed_readings.append(transformed)

# Real processing begins here
baseline_threshold = 2100
high_perf_turbines = []
critical_vibration = []

for entry in turbine_data:
    if entry['output_kw'] >= baseline_threshold:
        high_perf_turbines.append(entry['id'])
    if entry['vibration'] > 0.5:
        critical_vibration.append(entry['id'])

# Calibration sequence with bit manipulation (critical path)
calibration_sequence = [0b1101, 0b1011, 0b1110, 0b0111, 0b1001]

# Distractor: complex-looking but unused bitwise analysis
shadow_mask = 0
for i, val in enumerate(calibration_sequence):
    shadow_mask ^= (val << (i % 3))

# Actual relevant transformation
normalized_power = []
for t in turbine_data:
    norm_value = t['output_kw'] / 100.0
    if t['temp_c'] < 75:
        norm_value *= 1.08
    normalized_power.append(norm_value)

# Linear search for specific pattern in calibration (red herring)
search_target = 0b1110
found_index = -1
for i in range(len(calibration_sequence)):
    if calibration_sequence[i] == search_target:
        found_index = i
        break

# Real aggregation logic (uses enumerate and zip as required)
def aggregate_metrics(power_nodes, calib):
    # Summation and accumulation with conditional scaling
    base_sum = sum(node['vibration'] * node['rpm'] for node in power_nodes)
    
    # Conditional combinatorics
    adjustment_factor = 1.0
    if len(high_perf_turbines) >= 3:
        adjustment_factor *= 0.92
    if len(critical_vibration) > 1:
        adjustment_factor *= 1.15
    
    # Critical use of enumerate and zip
    indexed_weights = []
    for i, (node, cval) in enumerate(zip(power_nodes, calib)):
        weight = (node['output_kw'] / 2000) * (cval / 8) * (i + 1)
        indexed_weights.append(weight)
    
    # Final computation chain
    raw_metric = base_sum * adjustment_factor
    weighted_correction = sum(indexed_weights) * 0.23
    
    # Final diagnostic value
    result = raw_metric - (weighted_correction * 150)
    
    # Additional distraction: irrelevant rounding path
    temp_store = []
    for w in indexed_weights:
        temp_store.append(round(w * 100) / 100)
    
    return int(result)  # Deterministic integer result

# Execution point of interest
final_diagnostic = aggregate_metrics(turbine_data, calibration_sequence)

# Print result as required
print(f"Target result: {final_diagnostic}")