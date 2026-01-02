from itertools import cycle

# Simulate sensor readings with noise and periodic calibration
def generate_sensor_readings(count=5):
    return [105 + i * 3 - (i % 4) * 2 for i in range(count)]

def apply_filter(raw_readings):
    filtered = []
    for val in raw_readings:
        adjusted = val * 0.95 + 5
        if adjusted > 100:
            adjusted -= 3.5
        filtered.append(round(adjusted, 2))
    return filtered

def compute_trend(data):
    diffs = [data[i+1] - data[i] for i in range(len(data)-1)]
    avg_change = sum(diffs) / len(diffs)
    trend_category = 'rising' if avg_change > 0 else 'falling' if avg_change < 0 else 'stable'
    return avg_change, trend_category

def build_calibration_map(keys, values):
    # Irrelevant mapping construction (distractor)
    return {k: v % 17 for k, v in zip(keys, values)}

def adjust_pressure(base, log_entry):
    temp_offset = 0
    for entry in log_entry['history']:
        if entry['type'] == 'thermal_drift':
            temp_offset += entry['value'] * 0.75
    calibrated = base * 0.88 - abs(temp_offset)
    if calibrated < 0:
        calibrated = 0.5
    return round(calibrated, 2)

# Main execution flow
sensor_data = generate_sensor_readings(5)
filtered_data = apply_filter(sensor_data)
change_rate, direction = compute_trend(filtered_data)

# Dummy structures for distraction
timestamps = ['t0', 't1', 't2', 't3', 't4']
dummy_values = [110, 115, 108, 120, 113]
irrelevant_map = build_calibration_map(timestamps, dummy_values)

# Real processing begins
base_pressure = sum(filtered_data) / len(filtered_data)

# Simulated calibration log with red herring entries
log_series = [
    {'type': 'noise_spike', 'value': 4.2},
    {'type': 'thermal_drift', 'value': 2.8},
    {'type': 'vibration', 'value': 1.1},
    {'type': 'thermal_drift', 'value': 1.5},
]
calibration_log = {
    'version': '2.1',
    'history': log_series,
    'checksum': sum(v['value'] for v in log_series)  # unused field
}

# Key statement
final_pressure = adjust_pressure(base_pressure, calibration_log)

# Extraneous post-processing (dead code path)
if final_pressure > 50:
    status_flag = "NORMAL"
else:
    status_flag = "CALIBRATE"
    backup_system = [x * 1.1 for x in filtered_data if x > 40]

# Output result
print(f"Result: {final_pressure}")