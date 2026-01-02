def analyze_system_performance(raw_logs, config_params):
    total_entries = len(raw_logs)
    valid_records = []
    error_count = 0
    temp_buffer = []
    normalization_factor = config_params.get('norm_factor', 1.0)
    threshold = config_params.get('threshold', 0.75)

    for log in raw_logs:
        if not log or 'corrupted' in log:
            error_count += 1
            continue

        try:
            severity = float(log.split(',')[1])
            category = log.split(',')[0]
        except (IndexError, ValueError):
            error_count += 1
            continue

        if severity < 0.1:
            temp_buffer.append(severity * normalization_factor)
            continue

        normalized_severity = severity / normalization_factor if normalization_factor else severity
        if normalized_severity > threshold:
            flagged = True if category == 'CRITICAL' else False
            entry = {
                'cat': category,
                'severity': normalized_severity,
                'flagged': flagged
            }
            valid_records.append(entry)

    filtered_data = [r for r in valid_records if r['severity'] >= threshold]
    processed_data = {r['cat']: [r['severity']] for r in filtered_data}

    for r in valid_records:
        if r['cat'] in processed_data and r['severity'] >= threshold:
            processed_data[r['cat']].append(r['severity'])

    aggregate = sum([sum(v) for v in processed_data.values()])
    record_count = sum([len(v) for v in processed_data.values()])

    avg_magnitude = aggregate / record_count if record_count else 0

    def calculate_efficiency(data, thresh):
        if not data:
            return 0.0
        max_val = max([max(vals) for vals in data.values()])
        min_val = min([min(vals) for vals in data.values()])
        range_spread = max_val - min_val
        efficiency = (avg_magnitude * (1 + threshold)) / (range_spread + 1) if range_spread else avg_magnitude
        return efficiency

    # Extraneous computation - irrelevant to final result
    outlier_detection = []
    for values in processed_data.values():
        for v in values:
            if v > 2 * avg_magnitude:
                outlier_detection.append(v)

    # Dead code path - misleading but syntactically present
    debug_snapshot = [
        {'timestamp': i, 'value': val} 
        for i, val in enumerate(temp_buffer)
        if i % 2 == 0
    ]

    efficiency_score = calculate_efficiency(processed_data, threshold)
    return efficiency_score

# Input data
logs = [
    "CRITICAL,0.91", "WARNING,0.65", "CRITICAL,0.87",
    "INFO,0.05", "", "CORRUPTED_ENTRY", 
    "CRITICAL,0.93", "WARNING,0.76", "CRITICAL,0.88",
    "DEBUG,0.02", "CRITICAL,0.90"
]

params = {'norm_factor': 1.1, 'threshold': 0.7}

result = analyze_system_performance(logs, params)
print(f"Result: {result}")