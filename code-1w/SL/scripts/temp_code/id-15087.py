import itertools

# Simulated sensor network diagnostic system
def analyze_sensor_network():
    # Core data streams
    raw_readings = [14, 28, 19, 35, 22, 47, 13, 31, 24, 39]
    calibration_offsets = [3, -1, 2, 0, -2, 1, 4, -3, 0, 2]
    device_statuses = ['active', 'standby', 'active', 'fault', 'active', 'active', 'standby', 'active', 'fault', 'active']

    # Irrelevant auxiliary data (distractor)
    maintenance_log_ids = [1001, 1005, 1007, 1010, 1012, 1015, 1018, 1020, 1023, 1025]
    location_grid = [(0,0), (0,1), (1,0), (1,1), (2,0), (2,1), (3,0), (3,1), (4,0), (4,1)]

    # Apply calibration (relevant)
    calibrated_readings = [raw_readings[i] + calibration_offsets[i] for i in range(len(raw_readings))]

    # Masked status filtering with decoy logic
    active_mask = [status == 'active' for status in device_statuses]
    fault_mask = [status == 'fault' for status in device_statuses]  # unused path (red herring)

    # Decoy transformation chain
    def transform_sequence(seq):
        return [x * 2 + 1 for x in seq if x % 2 == 0]  # irrelevant logic

    encrypted_ticks = transform_sequence(maintenance_log_ids)  # dead end

    # Real processing begins: filter only active devices
    filtered_data = [calibrated_readings[i] for i in range(len(calibrated_readings)) if active_mask[i]]

    # Complex threshold map construction with set operations
    base_thresholds = {x for x in range(20, 45, 3)}  # {20, 23, 26, 29, 32, 35, 38, 41, 44}
    sensitivity_adjustments = {x for x in range(25, 50, 7)}  # {25, 32, 39, 46}

    # Intersection used for actual thresholds (critical)
    operational_core = base_thresholds & sensitivity_adjustments  # {32}

    # Unused symmetric difference (distractor)
    anomaly_boundaries = base_thresholds ^ sensitivity_adjustments  # decoy set

    # Build threshold map using itertools.cycle for rotation simulation
    cycle_pattern = list(itertools.cycle([1, -1, 2]))[:len(operational_core)]
    threshold_map = {}
    for idx, val in enumerate(operational_core):
        threshold_map[f'zone_{val}'] = val + cycle_pattern[idx]

    # Diagnostic processor with multiple branches
    def process_readings(readings, thresholds):
        # Secondary filtering (redundant but plausible)
        valid_range = [x for x in readings if 10 <= x <= 50]

        # Historical baseline (irrelevant)
        historical_peaks = {28: '2023-04-01', 33: '2023-04-05', 41: '2023-04-09'}

        # Real computation: count how many exceed ANY dynamic threshold
        threshold_values = list(thresholds.values())
        if not threshold_values:
            return len(readings) % 7 * -1

        # Primary logic: sum of readings above threshold, modulated by count
        total_excess = sum(x - t for x in valid_range for t in threshold_values if x > t)
        compliant_count = sum(1 for x in valid_range if all(x <= t for t in threshold_values))

        # Complex aggregation formula (key step)
        stability_index = (total_excess * len(threshold_values))
        penalty_factor = compliant_count ** 1.5 if compliant_count > 2 else 0.0

        # Final diagnostic calculation
        result = stability_index - int(penalty_factor)

        # Dead code branch (misleading)
        if result < 0:
            backup_system = [x ^ 7 for x in encrypted_ticks]  # never reached
            return sum(backup_system) % 100

        return result

    # Critical execution point
    final_diagnostic = process_readings(filtered_data, threshold_map)

    # Output requirement
    print(f"Result: {final_diagnostic}")

    # Auxiliary reporting (distractor)
    report_summary = {
        'device_count': len(raw_readings),
        'active_ratio': sum(active_mask) / len(active_mask),
        'grid_coverage': len(set(location_grid)) // 2
    }

    return final_diagnostic

# Execute
analyze_sensor_network()