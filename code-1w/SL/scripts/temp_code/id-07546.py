def analyze_sensor_network():
    # Simulated environmental sensor readings (temperature in Celsius)
    raw_readings = [23.5, 19.0, 25.3, 18.7, 30.1, 27.4, 22.0, 19.8, 24.6, 26.2]

    # Auxiliary metadata (distractor: not directly used in final result)
    sensor_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010']
    locations = ['North', 'South', 'East', 'West', 'Center', 'Roof', 'Basement', 'Lab', 'Hall', 'Tower']
    deployment_dates = [20210315, 20210316, 20210317, 20210318, 20210319, 20210320, 20210321, 20210322, 20210323, 20210324]

    # Irrelevant transformation (distractor)
    date_map = {sid: dt for sid, dt in zip(sensor_ids, deployment_dates)}
    location_index = {loc: i for i, loc in enumerate(locations)}

    # Data quality flags (partially relevant but misleading)
    quality_flags = [True, True, False, True, True, True, False, True, True, False]
    flagged_readings = [temp for temp, flag in zip(raw_readings, quality_flags) if flag]

    # Outlier detection threshold (red herring: not actually applied)
    mean_temp = sum(raw_readings) / len(raw_readings)
    std_dev = (sum((t - mean_temp) ** 2 for t in raw_readings) / len(raw_readings)) ** 0.5
    outlier_lower = mean_temp - 2 * std_dev
    outlier_upper = mean_temp + 2 * std_dev

    # Primary filtering logic (actually used)
    valid_range = lambda x: 18.5 <= x <= 26.5
    filtered_data = [temp for temp in raw_readings if valid_range(temp)]

    # Decoy function that looks important but isn't called
    def compute_thermal_index(data):
        return sum(t ** 1.1 for t in data if t > 20) / (len(data) + 1)

    # Unused alternative filtering path (dead code)
    if False:
        filtered_data = [t for t in raw_readings if t > mean_temp]

    # Calibration system (mixed relevance)
    base_calibration = 1.05
    temperature_drift = 0.02
    calibration_factor = base_calibration - temperature_drift * 1.5  # Evaluated to 1.02

    # Complex processing pipeline
    def process_readings(readings, calib):
        # Apply calibration
        calibrated = [round(r * calib, 3) for r in readings]
        
        # Secondary filter post-calibration (uses logical operations and comparisons)
        acceptable = [c for c in calibrated if c >= 20.0 and (c % 2 != 0 or c < 25.0)]
        
        # Bit manipulation red herring
        magic_seed = 0b1010
        mask = (magic_seed << 2) ^ 0b1101
        masked_sum = sum(len(bin(round(c * 10))) for c in acceptable)  # Irrelevant complexity
        
        # Real computation path
        exponent_weights = [1.1, 1.05, 1.03, 1.02, 1.01, 1.0, 0.99, 0.98]  # Weight decay pattern
        weighted_sum = 0.0
        for i, val in enumerate(acceptable):
            weight = exponent_weights[min(i, len(exponent_weights) - 1)]
            weighted_sum += val ** weight
        
        # Final aggregation with rounding
        diagnostic_score = round(weighted_sum * 0.87, 4)
        return int(diagnostic_score) if diagnostic_score > 100 else round(diagnostic_score, 2)

    # Ancillary data structure transformation (distractor)
    sensor_data_map = {
        sid: {'value': val, 'loc': loc, 'valid': valid_range(val)}
        for sid, val, loc in zip(sensor_ids, raw_readings, locations)
    }

    # Another decoy operation (tuple unpacking and enumeration)
    summary_stats = []
    for idx, (val, flag) in enumerate(zip(raw_readings, quality_flags)):
        if idx % 3 == 0:
            shifted = val + 0.5
n            status = 'OK' if shifted > 20 else 'LOW'
            summary_stats.append((idx, shifted, status))

    # Critical execution point
    final_diagnostic = process_readings(filtered_data, calibration_factor)

    # Output requirement
    print(f"Result: {final_diagnostic}")

analyze_sensor_network()