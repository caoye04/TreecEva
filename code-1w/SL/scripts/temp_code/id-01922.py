from collections import defaultdict, Counter

# Simulated sensor network data processing with diagnostic analysis
def collect_diagnostics():
    raw_readings = [145, 178, 201, 145, 190, 201, 178, 145, 210, 190, 145, 201]
    calibration_offset = 12
    scaling_factor = 1.05
    max_acceptable = 200
    min_acceptable = 150

    # Irrelevant pre-processing: normalized readings (not used in final path)
    normalized = [(x - min(raw_readings)) / (max(raw_readings) - min(raw_readings)) for x in raw_readings]

    # Distractor: unused transformation
    transformed_data = [round((x + calibration_offset) * scaling_factor) for x in raw_readings]

    # Actual relevant processing begins here
    adjusted_readings = [x + calibration_offset for x in raw_readings]

    # Count frequency of adjusted values
    freq_count = Counter(adjusted_readings)

    # Extract only those values that exceed the max_acceptable threshold
    outliers = [val for val, count in freq_count.items() if val > max_acceptable]

    # Distractor: unrelated statistical computation
    mean_val = sum(adjusted_readings) / len(adjusted_readings)
    variance = sum((x - mean_val) ** 2 for x in adjusted_readings) / len(adjusted_readings)
    std_dev = variance ** 0.5

    # Build severity map based on outlier magnitude
    severity_map = {val: (val - max_acceptable) ** 2 for val in outliers}

    # Unused decoy function
    def compute_entropy(counts):
        from math import log
        total = sum(counts.values())
        entropy = 0
        for count in counts.values():
            p = count / total
            entropy -= p * log(p)
        return entropy

    # Dead code path — never executed
    legacy_mode = False
    if legacy_mode:
        fallback_result = sum(severity_map.values()) * 0.5

    # Processed data structure used in final analysis
    processed_data = defaultdict(list)
    for val in adjusted_readings:
        bucket = 'high' if val > max_acceptable else 'normal' if min_acceptable <= val <= max_acceptable else 'low'
        processed_data[bucket].append(val)

    # Threshold configuration for diagnostic engine
    threshold_map = {
        'critical': max_acceptable + 10,
        'warning': max_acceptable + 5
    }

    # Decoy intermediate variable with misleading name
    preliminary_score = len([x for x in processed_data['high'] if x > threshold_map['warning']])

    # Another red herring: historical baseline comparison (not used)
    historical_avg = 172.3
    drift = mean_val - historical_avg

    # Core diagnostic logic
    def analyze_readings(data, thresholds):
        high_values = data['high']
        critical_level = thresholds['critical']
        warning_level = thresholds['warning']

        # Compute weighted impact: count above critical, otherwise sum excess over warning
        if any(v > critical_level for v in high_values):
            impact = len([v for v in high_values if v > critical_level]) * 100
        else:
            impact = sum(v - warning_level for v in high_values if v > warning_level)

        # Additional factor: diversity of high readings
        unique_high = len(set(high_values))
        stability_penalty = 5 * (len(high_values) - unique_high)  # penalty for repeated values

        # Final diagnostic score
        result = impact + stability_penalty

        # Dead branch: never taken due to data
        if min(high_values) < 150:
            result += 1000  # unreachable

        return int(result)

    # Key execution point
    final_diagnostic = analyze_readings(processed_data, threshold_map)

    # Print result as required
    print(f"Target result: {final_diagnostic}")

    # Return nothing; only side effect is printing
    return None

# Execute the function
collect_diagnostics()