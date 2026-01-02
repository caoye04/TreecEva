def sensor_diagnostic():
    # Real system parameters
    raw_readings = [145, 278, 93, 412, 88, 301, 176, 223]
    calibration_offset = 17
    sampling_rate = 4  # Hz
    temperature_compensation = 0.98

    # Irrelevant telemetry (distractor variables)
    battery_level = 87
    signal_strength = -67
    last_maintenance = '2023-11-05'
    device_id = 'SEN-TRX-9000'
    firmware_version = '2.1.7'

    # Preprocessing with red herring operations
    adjusted_readings = []
    cumulative_noise = 0
    spike_count = 0
    for i, val in enumerate(raw_readings):
        adjusted = (val + calibration_offset) * temperature_compensation
        adjusted_readings.append(int(adjusted))
        
        # Distractor logic: noise tracking (not used in final result)
        if i > 0 and abs(adjusted - adjusted_readings[i-1]) > 100:
            cumulative_noise += 15
            spike_count += 1

    # Decoy transformation function (never called)
    def legacy_process(x):
        return [v >> 2 for v in x]

    # Real processing path begins
    filtered_data = [v for v in adjusted_readings if v > 100]  # Remove low values

    # Bit manipulation red herring
    checksum = 0
    for v in raw_readings:
        checksum ^= v
        checksum &= 0xFFFF

    # String-based distractor: encode status (irrelevant)
    status_msg = f"Device {device_id} OK @ {sampling_rate}Hz"
    encoded_status = status_msg.upper().replace(' ', '_').strip()
    error_flag = len(encoded_status) % 2 == 0

    # Actual data transformation
    processed_data = []
    for v in filtered_data:
        # Apply non-linear correction
        corrected = int(v ** 0.5) * 3
        processed_data.append(corrected)
    
    # Hidden logic: count how many original readings had even digits sum
    even_digit_sum_count = 0
    for val in raw_readings:
        digit_sum = sum(int(d) for d in str(val))
        if digit_sum % 2 == 0:
            even_digit_sum_count += 1

    # Threshold determined by irrelevant computation (but looks important)
    pseudo_entropy = (len(device_id) * battery_level) % 19
    threshold = 42 + (spike_count * 2)  # Depends on earlier distractor

    # Core analysis function (looks complex, but deterministic)
    def analyze_readings(data, thresh):
        count_above = 0
        running_product = 1
        position_weight = 0
        
        for idx, x in enumerate(data):
            # Multiple layers of distraction
            if x > thresh:
                count_above += 1
                
            # Fake entropy calculation
            running_product = (running_product * (x + idx)) % 997
            
            # Weighted contribution that cancels out
            position_weight += (idx + 1) * x - x * (idx + 1)
        
        # The real answer depends only on count_above and even_digit_sum_count
        stability_factor = 7
        if count_above >= 3:
            stability_factor += 4
        
        # Final diagnostic is deterministic but obscured
        result = (count_above * 100) + (even_digit_sum_count * 10) + stability_factor
        return result

    # Execution point of interest
    final_diagnostic = analyze_readings(processed_data, threshold)
    print(f"Result: {final_diagnostic}")

sensor_diagnostic()