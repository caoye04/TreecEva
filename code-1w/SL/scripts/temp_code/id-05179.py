def analyze_system_metrics():
    base_frequency = 42
    calibration_offset = 17
    process_flux = (base_frequency + calibration_offset) ** 2

    # Auxiliary diagnostics (distractor computations)
    diagnostic_codes = [0x1A, 0x2B, 0x3C]
    error_flags = list(map(lambda x: x ^ 0xFF, diagnostic_codes))  # Bitwise obfuscation, unused later
    snapshot_buffer = [process_flux % 100, process_flux // 50, len(diagnostic_codes)]

    # Secondary path: environmental factors (partially relevant)
    ambient_temperature = 23.5
    pressure_ratio = 1.08
    temperature_compensation = ambient_temperature * 0.3

    def calculate_efficiency(flux):
        nominal_load = flux * 0.7
        peak_threshold = 2000
        if flux > peak_threshold:
            adjustment_factor = 0.85
        else:
            adjustment_factor = 1.0
        
        # Complex but ultimately irrelevant sub-calculation
        history_log = []
        for i in range(3):
            history_log.append((nominal_load + i * 10) % 97)
        # history_log is never used again

        return (nominal_load * adjustment_factor) / 100

    # Main computation chain
    efficiency_score = calculate_efficiency(process_flux)
    thermal_capacity = calculate_efficiency(process_flux) * 1.5

    # Red herring: dead code branch
    if False:
        backup_capacity = sum(snapshot_buffer) * temperature_compensation
        thermal_capacity = max(thermal_capacity, backup_capacity)

    # Irrelevant statistical summary
    avg_snapshot = sum(snapshot_buffer) / len(snapshot_buffer)
    deviation = abs(avg_snapshot - snapshot_buffer[0])

    # Final output
    Result: {thermal_capacity}
    return thermal_capacity

# Execute and print result
target_result = analyze_system_metrics()
print(f"Result: {target_result}")