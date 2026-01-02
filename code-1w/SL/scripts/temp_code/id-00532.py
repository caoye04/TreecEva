def analyze_performance(rpm_sequence, threshold=85):
    stability_index = 0
    fluctuation_count = 0
    for i, rpm in enumerate(rpm_sequence):
        if rpm > 100:
            adjusted_rpm = rpm * 0.9
        else:
            adjusted_rpm = rpm * 1.05

        if abs(adjusted_rpm - rpm) > 10:
            fluctuation_count += 1

        stability_index += adjusted_rpm / (i + 1) if i % 2 == 0 else 0

    performance_score = stability_index - fluctuation_count * 2
    return performance_score


def calculate_thermal_output(log_data):
    base_temperature = 25.0
    cumulative_heat = 0
    decay_factor = 0.92

    for entry in log_data:
        if 'temp' in entry:
            raw_temp = entry['temp']
            adjusted_temp = raw_temp * (1 + entry.get('overhead', 0.05))
            cumulative_heat += adjusted_temp * decay_factor
            decay_factor *= 0.98

    final_output = cumulative_heat * 1.45
    return final_output


# Simulated sensor readings over time
sensor_readings = [
    {'time': '00:01', 'temp': 68, 'status': 'OK'},
    {'time': '00:02', 'temp': 72, 'status': 'OK'},
    {'time': '00:03', 'temp': 75, 'status': 'WARN'},
    {'time': '00:04', 'temp': 80, 'status': 'WARN'},
    {'time': '00:05', 'temp': 88, 'overhead': 0.12, 'status': 'ALERT'}
]

# Engine RPM data across cycles
engine_cycles = [78, 92, 88, 76, 95, 101, 87]

# Auxiliary diagnostic string processing (distractor)
diagnostic_codes = ['ERR01', 'OK22', 'WARN7', 'INFO5', 'ALERT3']
valid_codes = [code for code in diagnostic_codes if code.endswith('2') or 'OK' in code]
code_lengths = [len(c) for c in valid_codes]

# Performance analysis with intermediate distraction variables
system_stability = analyze_performance(engine_cycles)
baseline_offset = 3.14159
reference_checksum = sum(code_lengths) * baseline_offset

# Prepare efficiency log from sensor data using zip and enumerate (required features)
efficiency_metrics = []
time_labels = [entry['time'] for entry in sensor_readings]
temp_values = [entry['temp'] for entry in sensor_readings]

for idx, (label, temp) in enumerate(zip(time_labels, temp_values)):
    normalized = temp / 100.0
    metric_entry = {
        'seq': idx,
        'label': label.strip(':').replace('00:', ''),
        'efficiency': round(1 - (normalized * 0.3), 3)
    }
    efficiency_metrics.append(metric_entry)

# Add overhead factors using string-based conditionals (distractor)
for entry in efficiency_metrics:
    time_digit = entry['label'][-1]
    if time_digit in '02468':
        entry['overhead'] = 0.08
    else:
        entry['overhead'] = 0.05

# Introduce irrelevant list comprehension with string method (intervention)
digit_flags = [ch.isdigit() for ch in ''.join(time_labels)]
alert_triggers = [entry for entry in sensor_readings if entry['status'].startswith('A')]

# Critical computation path
thermal_capacity = calculate_thermal_output(sensor_readings)

# Print result as required
print(f"Result: {thermal_capacity}")