def analyze_water_treatment():
    # Simulate a water purification process with multiple sensors and validation steps

    # Core process parameters
    base_flow_rate = 250.0
    contaminant_load = 142.5
    temperature_celsius = 22.3
    pressure_psi = 58.7

    # Sensor readings (some may be faulty)
    sensor_a_reading = 94.8
    sensor_b_reading = 96.1
    sensor_c_reading = 88.4  # Slightly out of range
    calibration_offset = -1.2

    # Derived metrics
    adjusted_sensor_a = sensor_a_reading + calibration_offset
    adjusted_sensor_b = sensor_b_reading + calibration_offset
    adjusted_sensor_c = sensor_c_reading + calibration_offset

    # Purity estimation from averaged sensors
    raw_purity_estimate = (adjusted_sensor_a + adjusted_sensor_b + adjusted_sensor_c) / 3

    # Environmental adjustments
    temp_factor = 1.0 if 20 <= temperature_celsius <= 25 else 0.85
    pressure_factor = pressure_psi / 60.0

    # Efficiency model
    base_efficiency = 0.91
    load_adjustment = max(0.7, 1 - (contaminant_load / 1000))
    efficiency_factor = base_efficiency * load_adjustment * temp_factor * pressure_factor

    # Flow validity checks (complex conditional)
    high_flow = base_flow_rate > 200
    stable_pressure = abs(pressure_psi - 60) < 5
    valid_temp_range = 18 <= temperature_celsius <= 30

    inflow_conditions = {
        'flow': high_flow,
        'pressure': stable_pressure,
        'temperature': valid_temp_range,
        'contaminants': contaminant_load < 200
    }

    # Determine overall inflow validity using conditional expression
    inflow_valid = all(inflow_conditions.values()) and raw_purity_estimate > 90

    # Critical computation: yield depends on purity and system efficiency
    net_purity = raw_purity_estimate * 0.98  # Final calibration
    filtration_yield = net_purity * efficiency_factor if inflow_valid else 0

    # Irrelevant diagnostic computations (distractors)
    diagnostic_codes = []
    if sensor_a_reading < 90:
        diagnostic_codes.append('A1')
    if sensor_b_reading < 90:
        diagnostic_codes.append('B1')
    if pressure_psi > 70:
        diagnostic_codes.append('P_HIGH')
    if len(diagnostic_codes) == 0:
        diagnostic_codes.append('NORMAL')

    avg_diagnostic_code_value = sum([hash(code) % 100 for code in diagnostic_codes]) / len(diagnostic_codes)

    # Unused transformation chains (dead logic path)
    def transform_flow(rate):
        if rate < 100:
            return rate * 1.5
        elif rate < 300:
            return rate * 1.2
        else:
            return rate * 0.95

    projected_flow = transform_flow(base_flow_rate)  # Not used in yield

    # Spurious intermediate variables (red herrings)
    stability_index = (adjusted_sensor_b - adjusted_sensor_c) / adjusted_sensor_a
    redundancy_check = (sensor_a_reading + sensor_b_reading) / 2
    final_quality_flag = 'PASS' if net_purity > 90 else 'FAIL'

    # Output the target result
    print(f"Result: {filtration_yield}")

analyze_water_treatment()