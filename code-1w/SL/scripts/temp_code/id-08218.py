def calculate_system_load():
    # Simulate a thermal regulation system with diagnostic telemetry
    base_temperature = 23.5
    target_temperature = 19.0
    temperature_delta = abs(base_temperature - target_temperature)

    # Sensor array inputs (simulated)
    sensor_readings = [23.4, 23.6, 23.5, 23.7, 23.3]
    calibrated_offsets = [round(abs(x - base_temperature)), 0.1] for x in sensor_readings]
    average_calibration = sum(calibrated_offsets) / len(calibrated_offsets)

    # Environmental interference factors (distractors)
    wind_speed_kph = 14.2
    humidity_index = 68
    pressure_mb = 1013.25
    interference_score = (wind_speed_kph * 0.3) + (humidity_index * 0.05)  # Unused beyond this

    # Primary energy computation chain
    base_energy_requirement = 1250
    delta_ratio = temperature_delta / 0.5  # Each 0.5C deviation adds 1 unit load
    dynamic_load_factor = int(delta_ratio) + 1

    # Efficiency degradation over time (modeled)
    runtime_hours = 72
    degradation_rate = 0.001
    efficiency_decay = runtime_hours * degradation_rate
    efficiency_factor = max(0.7, 1.0 - efficiency_decay)

    # Auxiliary systems draw (red herring variables)
    lighting_draw_kw = 1.2
    control_system_draw_kw = 0.35
    auxiliary_total = lighting_draw_kw + control_system_draw_kw  # Not used in thermal calc

    # Net energy flow calculation
    gross_energy_input = base_energy_requirement * dynamic_load_factor
    transmission_loss = gross_energy_input * 0.08
    net_energy_flow = gross_energy_input - transmission_loss

    # Critical assignment: compute effective thermal capacity
    thermal_capacity = net_energy_flow // efficiency_factor

    # Diagnostic checksum (unrelated to main result)
    checksum_seed = int(sum(sensor_readings))
    diagnostic_flag = checksum_seed % 2 == 1

    # Final telemetry output
    telemetry_data = {
        'status': 'OK',
        'capacity': thermal_capacity,
        'diagnostics': diagnostic_flag
    }

    print(f"Result: {thermal_capacity}")

calculate_system_load()