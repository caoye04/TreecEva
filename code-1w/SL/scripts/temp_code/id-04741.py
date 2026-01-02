def main():
    # Simulated sensor readings and calibration data
    raw_readings = [145, 203, 98, 167, 256, 73, 191]
    calibration_offsets = [5, -3, 8, 0, -12, 4, 6]
    
    # Apply calibration (relevant)
    calibrated_readings = [r + c for r, c in zip(raw_readings, calibration_offsets)]
    
    # Irrelevant preprocessing: normalize to percentage (distractor)
    max_reading = max(calibrated_readings)
    percentages = [round((val / max_reading) * 100, 2) for val in calibrated_readings]
    avg_percentage = sum(percentages) / len(percentages)

    # Secondary sensor set (semi-relevant but not used in final logic)
    secondary_sensor_data = {k: v * 1.05 for k, v in enumerate([102, 98, 150, 201, 75, 88, 110])}
    derived_metrics = []
    for idx, val in secondary_sensor_data.items():
        if val > 100:
            derived_metrics.append(val ** 0.5)

    # Core logic: filter readings above dynamic threshold
    base_threshold = 150
    fluctuation_factor = 0.1
    dynamic_floor = base_threshold * (1 - fluctuation_factor)

    # Define threshold function using lambda (required python feature)
    threshold_func = lambda x: x >= dynamic_floor

    # Process events with timestamp tracking (some state tracking)
    timestamps = [1634567800 + i*60 for i in range(len(calibrated_readings))]
    event_log = []
    for i, reading in enumerate(calibrated_readings):
        status = "ACCEPT" if threshold_func(reading) else "REJECT"
        event_log.append({'time': timestamps[i], 'value': reading, 'status': status})
    
    # Extract accepted results (relevant)
    accepted_values = [entry['value'] for entry in event_log if entry['status'] == 'ACCEPT']
    results = {
        'valid_count': len(accepted_values),
        'sum_valid': sum(accepted_values),
        'peak': max(accepted_values) if accepted_values else 0,
        'history': event_log
    }

    # Dead code path: unused diagnostic function (irrelevant)
    def debug_analysis(data):
        return {"size": len(data), "unique": len(set(data)), "range": max(data)-min(data)}
    
    # Unused transformation (distractor)
    inverted_map = tuple(abs(x - 255) for x in raw_readings)
    temp_correction = sum(inverted_map[:3]) / 3

    # Final score calculation depends only on results and threshold_func
    def calculate_final_score(report, validator):
        count_bonus = report['valid_count'] * 10
        sum_contribution = int(report['sum_valid'] // 10)
        peak_multiplier = 2 if validator(report['peak']) else 1
        return count_bonus + sum_contribution + (report['peak'] // 25) * peak_multiplier
    
    final_score = calculate_final_score(results, threshold_func)
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()