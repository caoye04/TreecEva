def analyze_sensor_coverage():
    # Define required and detected signal segments in a monitoring zone
    required_signals = {f'sensor_{i}' for i in range(1, 19)}  # 18 expected sensors

    # Simulate active sensor readings from field data
    raw_readings = ['sensor_2', 'sensor_4', 'sensor_5', 'sensor_7', 'sensor_8',
                   'sensor_9', 'sensor_11', 'sensor_13', 'sensor_14', 'sensor_15',
                   'sensor_16', 'sensor_17', 'sensor_18']
    active_segments = set(raw_readings)

    # Identify missing coverage points
    coverage_gaps = required_signals - active_segments

    # Secondary metric: count of redundant detections (appearing more than once)
    detection_log = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9]
    seen, duplicates = set(), set()
    for reading in detection_log:
        if reading in seen:
            duplicates.add(reading)
        else:
            seen.add(reading)

    # Final output for primary analysis
    print(f"Result: {len(coverage_gaps)}")

analyze_sensor_coverage()