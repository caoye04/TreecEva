import itertools

def analyze_sensor_array(raw_readings, threshold, mode='aggregate'):
    # Irrelevant preprocessing: string-based metadata parsing
    sensor_tag = 'SNSR-ALPHA-7'
    location_code = sensor_tag.split('-')[2]
    is_active = location_code.lower().startswith('a')

    # Distractor: unused transformation
    normalized = [x * 0.98 for x in raw_readings if x > -50]

    # Real filtering path
    valid_readings = []
    for val in raw_readings:
        if val > threshold + 5:
            valid_readings.append(val)
    
    # Dead code path (never reached due to prior filter)
    if mode == 'debug':
        return sum(valid_readings) % len(valid_readings)

    # Meaningless aggregation (red herring)
    avg_normalized = sum(normalized) / len(normalized) if normalized else 0
    spike_count = len([x for x in raw_readings if x > 90])
    
    # Actual relevant computation begins here
    calibrated_offsets = [x - 32 for x in valid_readings]
    squared_errors = [(x ** 2) * 0.1 for x in calibrated_offsets]
    
    # Bit manipulation decoy (unused result)
    bit_encoded = 0
    for x in calibrated_offsets[:3]:
        bit_encoded ^= int(x) & 0xFF
    
    # Key transformation
    filtered_data = [round(x, 3) for x in squared_errors if x < 500]
    
    # Multiple assignments with distractors
    calibration_factor, backup_factor, _ = (1.05, 0.95, 'legacy')
    
    # Unused dictionary operations (distractor)
    status_map = {k: 'valid' for k in filtered_data}
    status_map.update({0: 'null'})

    # Decoy function call (no side effects)
    def validate_integrity(data):
        return len(data) % 2 == 0
    
    validate_integrity(filtered_data)

    # Real processing function (nested logic)
    def process_readings(data, factor):
        if not data:
            return -999
        
        # Use of itertools and conditional branching
        paired = list(itertools.zip_longest(data, data[1:], fillvalue=0))
        diffs = []
        for a, b in paired:
            if a > b:
                diffs.append((a - b) * factor)
            elif b > 0:
                continue  # early skip
            else:
                diffs.append(a + b)

        # Tuple unpacking red herring
        total, count = sum(diffs), len(diffs)
        
        # Final calculation (answer depends only on this)
        rolling_adjustment = 0
        for i, d in enumerate(diffs):
            if i % 2 == 0:
                rolling_adjustment += d * 0.5
            else:
                rolling_adjustment -= d * 0.25
        
        return round(rolling_adjustment, 4)

    final_diagnostic = process_readings(filtered_data, calibration_factor)
    
    # Print required output
    print(f"Result: {final_diagnostic}")

    # Irrelevant final data structure
    report_summary = {
        'readings_processed': len(filtered_data),
        'calibration_used': calibration_factor,
        'anomaly_flag': False
    }

    return final_diagnostic

# Execution entry point
sensor_inputs = [85, 92, 76, 103, 45, 88, 110, 67, 95]
result = analyze_sensor_array(sensor_inputs, threshold=80)
