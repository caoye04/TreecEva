def analyze_sensor_array(raw_input, config):
    # Irrelevant preprocessing: case conversion and string cleanup
    cleaned_str = raw_input.strip().lower()
    tokens = cleaned_str.split(',')
    parsed_values = [float(x) for x in tokens if x.replace('.', '').isdigit()]

    # Distractor: unused statistical summaries
    mean_val = sum(parsed_values) / len(parsed_values) if parsed_values else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in parsed_values) / len(parsed_values) if parsed_values else 0

    # Relevant: identify anomalous indices using bitwise signature
    anomaly_flags = []
    for i, val in enumerate(parsed_values):
        bit_signature = int(val) & 7  # Use lower 3 bits
        is_anomalous = (bit_signature == 5) or (val > 90)
        anomaly_flags.append((i, is_anomalous, bit_signature))

    # Distractor: dead code path - never called
    def deprecated_filter(data):
        return [x for x in data if x > 0]  # Unused

    # Relevant: filter only anomalous readings
    filtered_indices = [i for i, flag, _ in anomaly_flags if flag]
    filtered_data = [parsed_values[i] for i in filtered_indices]

    # Distractor: misleading intermediate transformation
    shifted_data = [(x * 2) ^ 3 for x in parsed_values]  # Computed but not used

    # Relevant: construct threshold map based on configuration
    base_threshold = config.get('base', 10)
    dynamic_factor = config.get('factor', 1.5)
    offset = len(filtered_data) if len(filtered_data) < 5 else 2
    threshold_map = {}
    for idx, val in enumerate(filtered_data):
        key = f"sensor_{(idx ^ 3) + 100}"
        threshold_map[key] = base_threshold * dynamic_factor + offset

    # Distractor: unused zip-based alignment
    temp_labels = [f"T{idx}" for idx in range(len(parsed_values))]
    for label, value in zip(temp_labels, parsed_values):
        if 'T7' in label and value > 100:
            break  # Unreachable due to data range

    # Relevant: core processing function (defined inline to increase nesting)
    def process_readings(data, thresholds):
        results = []
        items = list(thresholds.items())
        for i, val in enumerate(data):
            # Use enumerate with offset logic
            adj_val = val - (i % 4)
            key_name = f"sensor_{(i ^ 3) + 100}"
            thresh = thresholds.get(key_name, 15)

            # Apply compound condition: arithmetic and logical mix
            if adj_val >= thresh:
                # Complex transformation: mix of arithmetic and bitwise
                score = int((adj_val * 0.7) // 1) ^ int(thresh)
                results.append(score)
            else:
                # Alternative path contributes to final sum
                backup = (adj_val + 5) & 15
                results.append(backup)

        # Final aggregation with list comprehension
        aggregate = sum([x * (x & 1) for x in results])  # Only odd values contribute
        return aggregate + len(results)  # Include count bonus

    # Critical execution point
    final_diagnostic = process_readings(filtered_data, threshold_map)

    # Output required result
    print(f"Result: {final_diagnostic}")

# Simulate input and config
data_stream = "85.0, 12.3, 93.1, 4.5, 6.7, 25.2, 5.0, 10.8, 105.0"
config_params = {'base': 12, 'factor': 2.0}

# Execute main analysis
analyze_sensor_array(data_stream, config_params)