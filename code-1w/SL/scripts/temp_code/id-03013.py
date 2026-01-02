def analyze_sensor_network():
    # Simulated sensor IDs and raw data streams
    sensor_ids = ['S101', 'S102', 'S103', 'S104', 'S105']
    base_readings = [23.4, 19.8, 45.1, 36.7, 28.3]
    status_flags = [True, False, True, True, False]
    calibration_offsets = [0.5, -0.3, 1.2, 0.0, -0.8]

    # Irrelevant auxiliary mapping (distractor)
    location_zones = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
    zone_temps = {k: v * 9 / 5 + 32 for k, v in location_zones.items()}  # Unused

    # Apply calibration (relevant)
    calibrated_readings = [base_readings[i] + calibration_offsets[i] for i in range(len(base_readings))]

    # Generate metadata index (partially relevant)
    sensor_index = {}
    for idx, sid in enumerate(sensor_ids):
        sensor_index[sid] = {
            'index': idx,
            'active': status_flags[idx],
            'calibrated': calibrated_readings[idx]
        }

    # Filter active sensors (relevant)
    active_sensors = [sid for sid in sensor_ids if sensor_index[sid]['active']]
    filtered_data = [sensor_index[sid]['calibrated'] for sid in active_sensors]

    # Decoy transformation chain (dead path)
    def transform_legacy(data):
        return [round(x ** 0.5, 2) for x in data if x > 20]  # Never called

    legacy_output = transform_legacy(calibrated_readings)  # Dead assignment

    # Threshold logic with red herring conditions
    temp_categories = {}
    for val in calibrated_readings:
        if val < 20:
            temp_categories[val] = 'LOW'
        elif val < 30:
            temp_categories[val] = 'NORMAL'
        elif val < 40:
            temp_categories[val] = 'ELEVATED'
        else:
            temp_categories[val] = 'HIGH'  # Only one HIGH entry

    # Misleading statistical summary (irrelevant)
    avg_reading = sum(calibrated_readings) / len(calibrated_readings)
    variance_proxy = sum((x - avg_reading) ** 2 for x in calibrated_readings)
    stability_score = 100 - variance_proxy  # Looks important, unused

    # Real threshold map construction (critical)
    threshold_map = {}
    for i, val in enumerate(calibrated_readings):
        category = temp_categories[val]
        penalty = 5 if category == 'HIGH' else (2 if category == 'ELEVATED' else 0)
        threshold_map[sensor_ids[i]] = 30 + penalty

    # Secondary decoy structure (unused)
    alert_registry = []
    for sid, val in zip(sensor_ids, calibrated_readings):
        if val > 40:
            alert_registry.append((sid, 'CRITICAL'))
        elif val > 35:
            alert_registry.append((sid, 'WARNING'))  # S103 would trigger, but not used

    # Core processing function (nested relevance)
    def process_readings(readings, thresholds):
        total_impact = 0
        adjustment_factor = 1.75

        # Enumerate over active sensor calibrated values
        for idx, val in enumerate(readings):
            sensor = active_sensors[idx]
            threshold = thresholds[sensor]

            # Primary impact calculation
            if val > threshold:
                excess = val - threshold
                total_impact += excess * adjustment_factor

        # Complex post-processing with dummy branches
        if total_impact > 10:
            total_impact *= 0.9
        elif total_impact > 5:
            total_impact *= 1.1
        else:
            total_impact += 2.5  # This will be triggered

        # Spurious bit manipulation (distractor)
        binary_tag = len(active_sensors) << 2 | 7  # Unused
        checksum = 0
        for c in ''.join(active_sensors):
            checksum ^= ord(c)

        return int(total_impact * 100) / 100.0  # Normalize to 2 decimals

    # Execute key computation
    final_diagnostic = process_readings(filtered_data, threshold_map)

    # Final red herring: alternate aggregation path (not taken)
    consolidated_report = []
    for s, r in zip(sensor_ids, base_readings):
        consolidated_report.append(f'{s}:{r:.1f}')
    report_hash = hash('|'.join(consolidated_report)) % 1000  # Computed but unused

    print(f'Result: {final_diagnostic}')

analyze_sensor_network()