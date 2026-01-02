def analyze_sensor_array(raw_readings, threshold=0.75):
    # Irrelevant preprocessing: normalize using unused method
    normalized = [x / max(raw_readings) for x in raw_readings]
    above_threshold = [i for i, x in enumerate(raw_readings) if x > threshold]

    # Distractor: complex-looking but unused transformation
    transformed = []
    for idx, val in enumerate(normalized):
        if idx % 2 == 0:
            transformed.append(val ** 2 * (idx + 1))
        else:
            transformed.append(val ** 0.5 / (idx + 1))

    # Real filtering path
    valid_indices = [i for i in range(len(raw_readings)) if raw_readings[i] > 0.1]
    filtered_data = [raw_readings[i] for i in valid_indices if i % 3 != 2]

    # Decoy statistical analysis (never used)
    mean_val = sum(transformed) / len(transformed) if transformed else 0
    variance = sum((x - mean_val) ** 2 for x in transformed) / len(transformed) if transformed else 0
    peak_noise_ratio = mean_val / (variance + 1e-5)

    # Unused recursive helper (red herring)
    def recursive_denoise(data, depth=0):
        if depth >= 3 or len(data) < 2:
            return data
        return recursive_denoise([0.5 * (data[i] + data[i+1]) for i in range(len(data)-1)], depth + 1)

    # Real calibration factor computed through non-obvious chain
    shape_factor = len(raw_readings) // (len(valid_indices) + 1)
    adjustment = 0
    for i, val in zip(valid_indices, [x for x in filtered_data]):
        adjustment += (i * val) % 4
    
    # Key computation buried in middle
    calibration_factor = (adjustment / (shape_factor + 1)) + 0.5

    # Another decoy: builds structure but not used
    diagnostic_map = {}
    for i, val in enumerate(zip(normalized, transformed)):
        diag_key = f"node_{i}_status"
        status_code = int((val[0] + val[1]) * 100)
        diagnostic_map[diag_key] = status_code

    # Critical function that produces answer
    def process_readings(data, factor):
        accumulation = 0
        for index, reading in enumerate(data):
            if index % 2 == 0:
                accumulation += reading * factor * 10
            else:
                accumulation -= reading * factor * 2
        return int(accumulation) if accumulation >= 0 else -int(abs(accumulation))

    # Final result assignment
    final_diagnostic = process_readings(filtered_data, calibration_factor)
    
    # Dead code path: looks important but never reached
    if final_diagnostic < 0:
        backup_repair = [x * 1.1 for x in filtered_data]
        final_diagnostic = sum(backup_repair) // 2

    # Output result
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execution entry point with fixed input
sensor_input = [0.12, 0.81, 0.05, 0.93, 0.22, 0.68, 0.01, 0.77]
analyze_sensor_array(sensor_input)