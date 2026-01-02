def main():
    # Sensor data from environmental monitoring array
    raw_readings = [32, 18, 47, 25, 39, 21, 44, 36]
    
    # Calibration thresholds
    lower_bound = 20
    upper_bound = 45

    # Irrelevant transformation - red herring
    scaled_readings = list(map(lambda x: (x * 1.8) + 32, raw_readings))  # Fahrenheit conversion (unused)

    # Filter valid sensor readings within operational range
    filtered_readings = [v for v in raw_readings if lower_bound <= v <= upper_bound]

    # Simulate checksum validation with bitwise verification
    checksum = 0
    for val in filtered_readings:
        checksum ^= val  # XOR accumulation
    
    # Secondary validation chain
    is_stable = len(filtered_readings) > 5
    variance = sum((x - sum(filtered_readings)/len(filtered_readings))**2 for x in filtered_readings) / len(filtered_readings) if filtered_readings else 0
    
    # Dead code path - misleading
    if variance > 100:
        adjusted_variance = variance * 0.9  # Never reached in this case

    # Process data through calibration validator
    processed_data = {
        'readings': filtered_readings,
        'checksum_valid': checksum % 2 == 0,
        'system_flag': is_stable,
        'timestamp': 1712345678  # Irrelevant metadata
    }

    # Dummy computation to increase cognitive load
    temporal_weight = (processed_data['timestamp'] % 100) * 0.1
    
    # Core logic: validation function with lambda
    validate_calibration = lambda data: 100 if data['checksum_valid'] and data['system_flag'] else 50

    # Key execution point
    filtration_score = validate_calibration(processed_data)

    # Additional irrelevant post-processing
    normalized_score = filtration_score / 100.0
    confidence_interval = (normalized_score * 0.95) if normalized_score > 0.7 else (normalized_score * 0.8)

    print(f"Result: {filtration_score}")

if __name__ == "__main__":
    main()