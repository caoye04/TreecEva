def analyze_filtration_process(raw_data: str) -> float:
    # Parse sensor readings from embedded string format (timestamp|value)
    entries = raw_data.split(',')
    timestamps = []
    pressure_readings = []
    
    for entry in entries:
        if '|' in entry:
            ts, val = entry.split('|')
            timestamps.append(int(ts))
            pressure_readings.append(float(val))

    # Derived metrics: rate of change and baseline thresholds
    delta_pressures = [pressure_readings[i+1] - pressure_readings[i] for i in range(len(pressure_readings)-1)]
    avg_pressure = sum(pressure_readings) / len(pressure_readings)
    high_threshold = avg_pressure * 1.3
    low_threshold = avg_pressure * 0.7

    # Simulate calibration offset (irrelevant to final result but adds cognitive load)
    calibration_sequence = [0.1, -0.2, 0.15, -0.05]
    adjusted_offsets = [x + 0.01 for x in calibration_sequence if x < 0.15]  # dead branch: not used later

    # Extract purity levels from pressure deviations (fictional physical model)
    purities = []
    for p in pressure_readings:
        if p > high_threshold:
            purities.append(0.85)
        elif p < low_threshold:
            purities.append(0.65)
        else:
            purities.append(0.92)

    # Filter only stable-phase readings (middle third of data) — key logic
    mid_start = len(purities) // 3
    mid_end = 2 * len(purities) // 3
    filtered_purities = purities[mid_start:mid_end]

    # Efficiency factor based on string length pattern (red herring computation)
    tag_suffix = raw_data[-3:]
    suffix_sum = sum([ord(c) - 96 for c in tag_suffix if c.isalpha()])  # uses ASCII, not meaningful
    efficiency_factor = 0.9 if suffix_sum % 2 == 0 else 0.95

    # Critical assignment point
    filtration_yield = sum(filtered_purities) * efficiency_factor

    # Extraneous post-processing (no effect on answer)
    report_lines = [f"Yield: {filtration_yield:.2f}"]
    formatted_report = "\n".join(report_lines).strip()

    print(f"Result: {filtration_yield}")
    return filtration_yield

# Simulated sensor input with embedded structure
sensor_input = "100|12.4,105|15.1,110|11.8,115|16.3,120|12.9,125|14.0,130|10.7,135|15.2,140|13.6"
analyze_filtration_process(sensor_input)