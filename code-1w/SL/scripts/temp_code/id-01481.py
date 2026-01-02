import itertools
import math

# Simulated sensor array data from wind turbine diagnostics
turbine_data = [
    {'rpm': 1250, 'temp': 78.3, 'vibration': 0.45, 'power_output': 2.1},
    {'rpm': 1300, 'temp': 80.1, 'vibration': 0.52, 'power_output': 2.3},
    {'rpm': 1180, 'temp': 75.6, 'vibration': 0.39, 'power_output': 1.9},
    {'rpm': 1320, 'temp': 82.4, 'vibration': 0.61, 'power_output': 2.4}
]

# Irrelevant maintenance log (red herring)
maintenance_log = [
    {'action': 'lubrication', 'timestamp': '2023-05-01'},
    {'action': 'inspector_check', 'timestamp': '2023-05-08'}
]

# Decoy function that is never called
def compute_efficiency_loss(rpm, temp):
    if rpm < 1200:
        return (temp - 70) * 0.15
    else:
        return (temp - 70) * 0.08

# Unused transformation pipeline
temp_readings = list(map(lambda x: x['temp'], turbine_data))
rpm_buckets = {key: list(group) for key, group in itertools.groupby(turbine_data, key=lambda x: x['rpm'] // 100)}

# Real processing begins here
baseline_rpm = 1200
calibration_sequence = [0.98, 1.02, 0.99, 1.01]

# Misleading intermediate calculation (not used in final result)
avg_vibration = sum(s['vibration'] for s in turbine_data) / len(turbine_data)
adjusted_power_sum = 0

# Simulate signal drift correction (unused)
signal_drift = [math.sin(i * 0.1) for i in range(len(turbine_data))]

# Core logic hidden among distractors
def apply_calibration(data_point, factor):
    return {
        'calibrated_output': data_point['power_output'] * factor,
        'thermal_ratio': data_point['temp'] / (data_point['rpm'] / 100),
        'stable': data_point['vibration'] < 0.5
    }

# Another decoy — calculates entropy but unused
def shannon_entropy(values):
    total = sum(values)
    probs = [v / total for v in values]
    return -sum(p * math.log2(p) for p in probs if p > 0)

entropy_guess = shannon_entropy([d['power_output'] for d in turbine_data])

# Key transformation with distractor variables
processed_nodes = []
for idx, entry in enumerate(turbine_data):
    # Distractor: complex unpacking and irrelevant tuple usage
    (status_flag, priority) = (True, 1) if entry['temp'] > 77 else (False, 3)
    
    # Real work inside distraction
    calibrated = apply_calibration(entry, calibration_sequence[idx % len(calibration_sequence)])
    processed_nodes.append(calibrated)

    # Dead code path (never executed due to structure)
    if False:
        backup_node = {'raw': entry, 'index': idx}
        adjusted_power_sum += backup_node['raw']['power_output']

# Accumulation obscured by multiple loops
valid_nodes = [node for node in processed_nodes if node['stable']]

# Summation disguised as diagnostic metric
output_accumulator = 0
for node in valid_nodes:
    # Only calibrated_output contributes
    output_accumulator += node['calibrated_output']

# Red herring: bit manipulation on irrelevant metric
temp_flags = 0
for d in turbine_data:
    temp_flags ^= int(d['temp'])

# Final aggregation uses both real data and decoy sequence
aggregation_key = sum(calibration_sequence) * 10  # 40.0

# Real answer computation buried in noise
intermediate_metric = output_accumulator * 1000  # Scale up
noise_floor = len([d for d in turbine_data if d['vibration'] >= 0.5]) * 100  # 200

# Final diagnostic combines relevant accumulation and noise floor subtraction
final_diagnostic = int(intermediate_metric - noise_floor)

# Print required result
print(f"Result: {final_diagnostic}")