def analyze_sensor_data(raw_readings):
    processed = []
    temp_offset = 0.0
    cumulative_noise = 0
    
    for reading in raw_readings:
        stripped = reading.strip()
        if not stripped.startswith('SEN'):
            continue
            
        parts = stripped.split(':')
        if len(parts) < 3:
            continue
            
        try:
            sensor_id = parts[0]
            status_code = int(parts[1])
            value_str = parts[2]
            
            # Irrelevant parsing branch (dead logic)
            if 'CAL' in value_str:
                calibration_value = float(value_str.replace('CAL', ''))
                temp_offset += calibration_value % 0.5
                continue
            
            data_point = float(value_str)
            
            # Real processing branch
            if status_code == 200:
                if data_point > 1000:
                    data_point = 999.99  # clamp
                elif data_point < -1000:
                    data_point = -999.99
                processed.append(data_point)
                
        except (ValueError, IndexError):
            cumulative_noise += 1
            continue

    # Distractor: unused complex transformation
    reversed_data = [x for x in reversed(processed)]
    smoothed = []
    for i in range(len(reversed_data)):
        window = reversed_data[max(0, i-2):i+1]
        smoothed.append(sum(window) / len(window))

    # Actual relevant computation begins here
    base_total = sum(processed)
    sample_count = len(processed)
    
    if sample_count == 0:
        aggregate_score = 0
    else:
        aggregate_score = base_total / sample_count

    # Bit manipulation red herring
    binary_mask = 0b101010
    shift_key = (sample_count ^ binary_mask) & 0b1111
    dummy_checksum = (shift_key << 2) | (shift_key >> 2)

    # Conditional logic with decoy variables
    threshold_met = aggregate_score > 42.0
    volatility_index = 0
    for i in range(1, len(processed)):
        diff = abs(processed[i] - processed[i-1])
        if diff > 50:
            volatility_index += 1

    # Another distraction: string analysis with no impact
    debug_tag = ""
    for r in raw_readings:
        if 'ERR' in r:
            debug_tag += r[r.find('ERR'):][:4]
    tag_length = len(debug_tag)
    
    # Core logic embedded in noise
    if threshold_met and volatility_index > 2:
        anomaly_flag = 1
    elif not threshold_met:
        anomaly_flag = -1
    else:
        anomaly_flag = 0

    correction_factor = 17.3
    
    # Key statement — answer depends on this
    final_diagnostic = aggregate_score + correction_factor * anomaly_flag
    
    # Multiple print statements to distract
    print(f"Processed {sample_count} valid readings")
    print(f"Volatility events: {volatility_index}")
    print(f"Noise encounters: {cumulative_noise}")
    print(f"Checksum (unused): {dummy_checksum}")
    
    # Final output
    print(f"Result: {final_diagnostic}")
    
    return final_diagnostic

# Input data with mixed valid/invalid entries
sensor_inputs = [
    "SEN001:200:890.5",
    "LOG_ENTRY_IGNORED",
    "SEN002:404:700.0",  # invalid status
    "SEN003:200:1050",     # clamped to 999.99
    "SEN004:200:CAL0.25",
    "SEN005:200:-600.3",
    "SEN006:200:950.1",
    "SEN007:200:300.0",
    "ERR_CRITICAL",         # triggers debug_tag but ignored
    "SEN008:200:980.7",
    "SEN009:200:400.2"
]

result = analyze_sensor_data(sensor_inputs)