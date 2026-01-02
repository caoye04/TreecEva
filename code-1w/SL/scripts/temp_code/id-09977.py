def analyze_sensor_data(raw_readings):
    # Irrelevant preprocessing: Normalize values (unused in final result)
    normalized = [round((x - min(raw_readings)) / (max(raw_readings) - min(raw_readings)) * 100, 2) for x in raw_readings]
    
    # Distractor: Frequency analysis of digits (never used)
    digit_freq = {}
    for val in raw_readings:
        for digit in str(abs(val)):
            digit_freq[int(digit)] = digit_freq.get(int(digit), 0) + 1
    
    # Key data transformation: Filter anomalies above threshold
    filtered_readings = [x for x in raw_readings if x < 750]
    
    # Dead code path: Simulate backup system (unreachable due to condition)
    backup_mode = False
    if sum(filtered_readings) < 0:
        redundant_total = 0
        for i in range(len(filtered_readings)):
            redundant_total += filtered_readings[i] * (i % 7)
        backup_mode = True

    # Compute moving average (distractor - not used in answer)
    window_size = 3
    moving_averages = []
    for i in range(len(filtered_readings) - window_size + 1):
        window_avg = sum(filtered_readings[i:i+window_size]) / window_size
        moving_averages.append(round(window_avg, 3))
    
    # Core logic begins here
    base_energy = sum(x ** 0.5 for x in filtered_readings if x > 0)  # Only positive readings contribute
    spike_count = len([x for x in raw_readings if x > 800])  # Count extreme values pre-filter
    
    # Conditional branching based on environmental mode
    environment_mode = 'storm'  # Simulated sensor context
    if environment_mode == 'calm':
        sensitivity_factor = 1.2
    elif environment_mode == 'windy':
        sensitivity_factor = 1.5
    else:
        sensitivity_factor = 1.8  # Default during storm
    
    # Intermediate calculation with red herring variables
    temp_buffer = []
    for idx, val in enumerate(filtered_readings):
        if idx % 2 == 0:
            temp_buffer.append(val * 0.9)
        else:
            temp_buffer.append(val * 1.1)
    buffered_sum = sum(temp_buffer)

    # Unused diagnostic chain
    diagnostic_chain = [{'step': i, 'status': 'ok'} for i in range(5)]
    for entry in diagnostic_chain:
        if entry['step'] > 3:
            entry['status'] = 'review'

    # Actual relevant calculations
    aggregate_score = int(base_energy * sensitivity_factor)  # Integer score from energy and conditions
    anomaly_penalty = spike_count ** 2
    
    # Correction factor derived from character count in synthetic ID
    device_id = "SEN-TRX9000"
    char_count = len([c for c in device_id if c.isalpha()])  # Count letters only
    digit_sum = sum(int(c) for c in device_id if c.isdigit())
    correction_factor = (char_count - digit_sum) or 1  # Avoid zero
    
    # Critical assignment point
    final_diagnostic = aggregate_score + anomaly_penalty * correction_factor
    
    # Decoy output variable (misleading)
    secondary_index = (buffered_sum // 100) + len(digit_freq)
    
    # Print required result
    print(f"Result: {final_diagnostic}")

# Input data
readings = [144, 867, 400, 902, 324, 780, 529, 888, 169]
analyze_sensor_data(readings)