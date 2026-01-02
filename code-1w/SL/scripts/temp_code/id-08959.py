import math

# Simulated system telemetry data from a distributed sensor network
technical_logs = [
    {'timestamp': 1623456780, 'sensor_id': 'S1', 'value': 127, 'status': 'OK'},
    {'timestamp': 1623456789, 'sensor_id': 'S2', 'value': 255, 'status': 'OK'},
    {'timestamp': 1623456795, 'sensor_id': 'S3', 'value': 64, 'status': 'ERROR'},
    {'timestamp': 1623456801, 'sensor_id': 'S1', 'value': 191, 'status': 'OK'},
    {'timestamp': 1623456810, 'sensor_id': 'S3', 'value': 223, 'status': 'OK'},
    {'timestamp': 1623456815, 'sensor_id': 'S4', 'value': 31, 'status': 'WARNING'}
]

# Irrelevant metadata (distractor)
system_metadata = {
    'version': '2.1.9',
    'build_date': '2023-06-15',
    'nodes': ['alpha', 'beta', 'gamma'],
    'max_log_size': 10000,
    'debug_mode': False
}

# Decoy function that looks relevant but is unused (dead code path)
def legacy_calibrate(data):
    adjusted = []
    for entry in data:
        entry['value'] = int(entry['value'] * 0.95)
        adjusted.append(entry)
    return adjusted

# Unused transformation map (red herring)
transform_map = {
    'S1': lambda x: x ^ 15,
    'S2': lambda x: x & 240,
    'S3': lambda x: x | 64,
    'S4': lambda x: x >> 2
}

# Diagnostic thresholds (some are misleading)
thresh_critical = 200
thresh_warning = 150
thresh_info = 100  # Not actually used

# System flags with multiple decoy entries
system_flags = {
    'overload_protection': True,
    'legacy_mode': False,
    'data_enhancement': True,
    'mock_flag_ignored': True,
    'checksum_enabled': False
}

# Spurious intermediate calculations (irrelevant)
total_sensors = len([log['sensor_id'] for log in technical_logs])
avg_value = sum(log['value'] for log in technical_logs) / len(technical_logs)
peak_value = max(log['value'] for log in technical_logs)

# Bit manipulation table for unused optimization (distractor)
optim_table = {}
for i in range(8):
    optim_table[i] = (i << 3) | 7

# Real processing begins here

# Extract active sensors and their latest values
current_state = {}
for log in technical_logs:
    sensor_id = log['sensor_id']
    if sensor_id not in current_state or log['timestamp'] > current_state[sensor_id]['timestamp']:
        current_state[sensor_id] = log

# Compute diagnostic hash using bitwise and arithmetic ops
hash_seed = 5437
for sensor_id, data in current_state.items():
    val = data['value']
    # Mix value into hash using prime multiplier and XOR
    hash_seed ^= (val * 31 + ord(sensor_id[-1]))
    hash_seed = (hash_seed & 0xFFFFFFFF)  # Keep within 32-bit

# Determine status levels
error_count = sum(1 for log in technical_logs if log['status'] == 'ERROR')
warning_count = sum(1 for log in technical_logs if log['status'] == 'WARNING')
ok_count = len(technical_logs) - error_count - warning_count

# Flag-based modifier
modifier = 1.0
if system_flags['overload_protection']:
    modifier *= 0.9
if system_flags['data_enhancement']:
    modifier *= 1.15

# Composite metric calculation
base_metric = hash_seed % 10000
scaled_metric = base_metric * modifier

# Apply conditional adjustment based on warning presence
if warning_count > 0:
    scaled_metric -= 250
    temp_adjust = []
    for i in range(3):
        temp_adjust.append(int(scaled_metric / (i + 1)) if i > 0 else int(scaled_metric))
    scaled_metric = sum(temp_adjust) / len(temp_adjust)

# Final aggregation logic
final_diagnostic = int(scaled_metric + error_count * 100)

# Print result as required
print(f"Result: {final_diagnostic}")