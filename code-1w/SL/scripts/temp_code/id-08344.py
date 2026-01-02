def analyze_system_state():
    # Simulate sensor readings from a distributed system
    raw_readings = [12, 15, 10, 8, 23, 14, 9, 18, 21, 11]
    
    # Irrelevant metadata (distractor)
    device_ids = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10']
    location_map = {uid: idx % 3 for idx, uid in enumerate(device_ids)}
    
    # Filter anomalies using threshold logic (relevant)
    normal_range = (10, 20)
    filtered_readings = [x for x in raw_readings if normal_range[0] <= x <= normal_range[1]]
    
    # Compute moving average to smooth data (relevant)
    smoothed = []
    window_size = 2
    for i in range(len(filtered_readings) - window_size + 1):
        window_avg = sum(filtered_readings[i:i+window_size]) / window_size
        smoothed.append(round(window_avg))
    
    # Misleading transformation on irrelevant path (distractor)
    temp_shift = [x - 5 for x in raw_readings if x > 15]
    decay_factor = 0.8
    projected_loss = sum(temp_shift) * decay_factor  # unused downstream
    
    # Adjust direction based on trend slope (relevant)
    trend_direction = []
    for i in range(1, len(smoothed)):
        if smoothed[i] > smoothed[i-1]:
            trend_direction.append(1)
        elif smoothed[i] < smoothed[i-1]:
            trend_direction.append(-1)
        else:
            trend_direction.append(0)
    
    # Apply corrective offsets for oscillations (semi-relevant)
    correction_phase = []
    for step in trend_direction:
        if step == 1:
            correction_phase.append(0.5)
        elif step == -1:
            correction_phase.append(-0.3)
        else:
            correction_phase.append(0)
    
    # Accumulate net adjustment path (relevant)
    adjusted_path = [smoothed[0]]
    for delta in correction_phase:
        adjusted_path.append(adjusted_path[-1] + delta)
    
    # Dead code path — no impact on result (distractor)
    outlier_buffer = []
    for val in raw_readings:
        if val < 9 or val > 22:
            outlier_buffer.append(val * 2)
    buffer_checksum = sum(outlier_buffer) % 17 if outlier_buffer else 0
    
    # Final integration step: compute stability score (relevant)
    fluctuation_index = sum(abs(correction_phase[i] - correction_phase[i-1]) 
                           for i in range(1, len(correction_phase)))
    base_energy = sum(smoothed)
    final_tally = int(base_energy - fluctuation_index * 10)
    
    # Key computation point
    equilibrium_score = final_tally // (len(adjusted_path) or 1)
    
    # Print result as required
    print(f"Result: {equilibrium_score}")

analyze_system_state()