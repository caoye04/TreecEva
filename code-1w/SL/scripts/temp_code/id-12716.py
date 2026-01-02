from collections import defaultdict, Counter

# Simulated sensor data processing with diagnostic flags
def process_sensor_readings(raw_data):
    readings_log = defaultdict(list)
    diagnostics = []
    temp_buffer = []
    aggregate_score = 0
    correction_factor = 0
    entropy_counter = 0

    for idx, entry in enumerate(raw_data):
        # Parse timestamp and value
        timestamp_str, val_str, flag = entry
        numeric_value = float(val_str)
        
        # Irrelevant time-based categorization (distractor)
        hour = int(timestamp_str.split(':')[0])
        period = 'night' if hour < 6 or hour >= 18 else 'day'
        readings_log[period].append(numeric_value)

        # Core logic: detect anomalies and compute score
        if abs(numeric_value) > 50:
            diagnostics.append((idx, 'OVERFLOW'))
            correction_factor -= 3
        elif 10 <= abs(numeric_value) <= 20:
            temp_buffer.append(numeric_value)
            if len(temp_buffer) % 3 == 0:
                correction_factor += sum(temp_buffer[-3:]) / 3

        # Dead branch: never executed due to flag logic (red herring)
        if flag == 'CRITICAL_OVERRIDE':
            emergency_reset = True
            for _ in range(5):
                emergency_reset = not emergency_reset
            break

        # Accumulate only positive even-indexed values
        if idx % 2 == 0 and numeric_value > 0:
            aggregate_score += int(numeric_value)

        # Bit manipulation decoy: computes but unused result
        bit_fiddle = idx ^ 255
        if bit_fiddle & (bit_fiddle - 1) == 0:  # power of two check
            entropy_counter += 1

    # Unused statistical analysis (distractor)
    all_values = [float(x[1]) for x in raw_data]
    freq_stats = Counter(all_values)
    mode_val = freq_stats.most_common(1)[0][1]
    spread_metric = max(all_values) - min(all_values)

    # Final computation path (target)
    final_diagnostic = aggregate_score + correction_factor

    # Additional red herring: complex unused transformation
    transformed_diagnostics = [
        f"{d[1]}_CODE_{hash(d[0]) % 100}" for d in diagnostics if d[1] == 'OVERFLOW'
    ]
    summary_key = ''.join([t[5] for t in transformed_diagnostics[:2]]) if transformed_diagnostics else 'NONE'

    return final_diagnostic

# Input data (simulated sensor stream)
sensor_input = [
    ('08:15', '65.4', 'NORMAL'),
    ('08:16', '12.3', 'NORMAL'),
    ('08:17', '15.7', 'NORMAL'),
    ('08:18', '98.2', 'NORMAL'),
    ('08:19', '18.9', 'NORMAL'),
    ('08:20', '-200.1', 'NORMAL'),
    ('08:21', '45.0', 'NORMAL'),
    ('08:22', '10.5', 'NORMAL')
]

# Execute and print target result
target_result = process_sensor_readings(sensor_input)
print(f"Result: {target_result}")