def main():
    # Simulated sensor readings and calibration data
    raw_readings = [107, 214, 153, 98, 201]
    calibration_factor = 0.89
    offset = 17

    # Apply calibration and offset (relevant)
    calibrated = [round((x * calibration_factor) + offset) for x in raw_readings]

    # Irrelevant: Diagnostic log setup (distractor)
    diagnostic_mode = True
    log_buffer_size = 2048
    debug_level = 'INFO'
    temp_diagnostic_data = {f'entry_{i}': i * 2 for i in range(10)}  # Dead code

    # Normalize data into score range 0-100 (relevant)
    max_val = max(calibrated)
    normalized = [int((x / max_val) * 100) for x in calibrated]

    # Threshold mapping using dictionary (relevant)
    thresholds = {
        'low': 30,
        'medium': 60,
        'high': 85
    }

    # Misleading secondary threshold (semi-relevant but unused)
    fallback_thresholds = {'min': 25, 'optimal': 70}
    adjustment_factor = 1.05  # Unused in logic

    # Scale data using lambda (relevant)
    scaler = lambda val, factor: int(val * factor)
    scaled_data = [scaler(val, 0.95) for val in normalized]

    # Process results based on threshold rules (key function)
    def process_results(data, limits):
        score = 0
        category_tally = {'high': 0, 'medium': 0, 'low': 0}

        for value in data:
            # Categorize each value
            if value >= limits['high']:
                category = 'high'
                increment = 15
            elif value >= limits['medium']:
                category = 'medium'
                increment = 8
            elif value >= limits['low']:
                category = 'low'
                increment = 3
            else:
                category = 'very_low'
                increment = 1

            # Update tally (semi-relevant, not used in score)
            if category in category_tally:
                category_tally[category] += 1

            # Accumulate score (critical path)
            score += increment

            # Artificial complexity: conditional expression with no impact
            status = 'active' if score > 20 else 'pending'
            _ = status  # Dummy use to avoid linter warning

        # Bonus logic: extra points if more than two 'high' values
        high_count = sum(1 for v in data if v >= limits['high'])
        if high_count > 2:
            score += 10

        return score

    # Execute key statement
    final_score = process_results(scaled_data, thresholds)

    # Irrelevant post-processing (dead code)
    report_timestamp = '2023-11-05T14:30:00Z'
    export_format = 'JSON'
    compression_enabled = False

    print(f"Result: {final_score}")

if __name__ == '__main__':
    main()