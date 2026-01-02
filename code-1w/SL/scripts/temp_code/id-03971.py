def analyze_sensor_data(log_entries):
    # Simulate processing of sensor readings with metadata
    timestamps = [entry[0] for entry in log_entries]
    readings = [entry[1] for entry in log_entries]
    modes = [entry[2] for entry in log_entries]

    # Irrelevant transformation: normalize timestamps (not used later)
    base_time = timestamps[0]
    normalized_times = [(t - base_time) / 1000 for t in timestamps]

    # Distractor: count mode transitions (semi-relevant but unused)
    mode_changes = 0
    for i in range(1, len(modes)):
        if modes[i] != modes[i-1]:
            mode_changes += 1

    # Key data slicing: focus on active phase (middle 60%)
    slice_start = len(readings) * 2 // 5
    slice_end = len(readings) * 4 // 5
    active_readings = readings[slice_start:slice_end]

    # Track multiple accumulators (only one is used in final result)
    accumulation = 0
    squared_sum = 0
    weighted_sum = 0

    for idx, (i, value) in enumerate(zip(range(len(active_readings)), active_readings)):
        accumulation += value * (i + 1)
        squared_sum += value ** 2
        weighted_sum += value * (idx % 4 + 1)

    # Secondary computation: peak detection (unused red herring)
    peaks = []
    for i in range(1, len(active_readings)-1):
        if active_readings[i] > active_readings[i-1] and active_readings[i] > active_readings[i+1]:
            peaks.append(i)

    # Generate obfuscated key using bitwise manipulation
    raw_key = 0
    for val in readings[::3]:  # every third reading
        raw_key ^= int(val) << 1
    
    refined_key = raw_key & 0xFFFF
    final_key = refined_key ^ (refined_key >> 8)

    # Critical statement
    checksum = final_key ^ accumulation

    # Dead code: format diagnostic report (never called in execution path)
    def generate_diagnostic():
        return f'Readings: {len(readings)}, Peaks: {len(peaks)}'

    return checksum

# Input data: sensor log (timestamp, reading, mode)
logs = [
    (1678886400000, 17, 'A'), (1678886401000, 23, 'A'), (1678886402000, 19, 'B'),
    (1678886403000, 28, 'B'), (1678886404000, 31, 'B'), (1678886405000, 14, 'C'),
    (1678886406000, 22, 'C'), (1678886407000, 25, 'C'), (1678886408000, 18, 'A'),
    (1678886409000, 20, 'A')
]

result = analyze_sensor_data(logs)
print(f"Result: {result}")