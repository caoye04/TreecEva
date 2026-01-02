def analyze_sensor_data():
    raw_readings = [107, 214, 153, 98, 241]
    threshold = 100
    spike_count = 0
    normalized = []
    
    for val in raw_readings:
        if val > threshold:
            spike_count += 1
        normalized.append((val + 5) // 10 * 2)

    # Misleading transformation (not used in final result)
    transformed = [x ^ 7 for x in normalized if x % 3 == 0]
    artifact_score = sum(transformed) % 19

    base_flux = 0
    for i in range(len(normalized)):
        base_flux += normalized[i] << 1
    
    # Simulate calibration set using set operations
    default_calibrations = {1, 2, 4, 8, 16, 32}
    environmental_shifts = {2, 8, 16, 64}
    calibration_set = default_calibrations & environmental_shifts  # Intersection
    calibration_set.add(256)  # External correction factor

    def adjust_flux(flux, calib):
        temp = flux
        for factor in sorted(calib):
            if factor > 100:
                temp += factor // 4
            else:
                temp -= factor % 7
        return temp ^ 15  # Final obfuscation via XOR

    intermediate_diagnostic = (base_flux * 2 + len(calibration_set)) / 3.5
    debug_flag = intermediate_diagnostic < 100

    final_flux = adjust_flux(base_flux, calibration_set)
    
    # Dead code branch - misleading control flow
    if debug_flag and False:
        final_flux = -1
        backup_log = [base_flux, artifact_score]
    
    print(f"Result: {final_flux}")

analyze_sensor_data()