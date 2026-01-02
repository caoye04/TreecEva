def analyze_thermal_profile():
    # Simulate a thermal regulation system with diagnostic metrics
    temperatures = [22.3, 24.1, 19.8, 25.6, 23.7, 20.9, 26.4]
    pressure_readings = [101.3, 102.1, 99.8, 103.4, 100.2, 98.7, 104.5]  # Unused in final calc

    # Distractor: irrelevant diagnostics
    avg_pressure = sum(pressure_readings) / len(pressure_readings)
    deviation_index = 0
    for p in pressure_readings:
        deviation_index += (p - avg_pressure) ** 2
    deviation_index = deviation_index ** 0.5

    # Relevant data processing
    filtered_temps = [t for t in temperatures if t > 20.0]  # List comprehension
    temp_summation = sum(filtered_temps)
    sample_size = len(filtered_temps)

    # Compute base physical flux using mean of filtered temps
    base_flux = temp_summation / sample_size

    # Efficiency determined by set logic on string-encoded status
    status_codes = ['OK', 'PENDING', 'OK', 'FAILED', 'OK']
    valid_statuses = set([s.lower() for s in status_codes])  # Set operation + string method
    success_count = len(valid_statuses)  # Misleading: not actual success rate

    # Actual efficiency depends only on number of 'OK' entries
    actual_successes = status_codes.count('OK')
    efficiency_factor = actual_successes / len(status_codes)

    # Key computation point
    thermal_capacity = base_flux * efficiency_factor

    # Additional red herring computations
    normalized_data = []
    for i, t in enumerate(temperatures):
        normalized_value = (t - min(temperatures)) / (max(temperatures) - min(temperatures))
        normalized_data.append(f"{normalized_value:.3f}")

    checksum = 0
    for entry in normalized_data:
        checksum += float(entry) * 1000
    checksum = int(checksum) % 100  # Irrelevant final check

    print(f"Result: {thermal_capacity}")

analyze_thermal_profile()