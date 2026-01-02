from collections import defaultdict, Counter

# Simulated sensor network data processing with diagnostic analysis
def collect_diagnostics():
    raw_readings = [104, 95, 110, 90, 130, 120, 115, 105, 98, 140, 138, 128, 118, 108, 99]
    base_threshold = 100
    sensitivity_factor = 0.15
    temp_cache = []
    outlier_flags = []

    # Irrelevant temperature conversion cache (distractor)
    for val in raw_readings:
        celsius = (val - 32) * 5 / 9
        temp_cache.append(round(celsius, 2))

    # Real filtering logic: detect values above dynamic threshold
    dynamic_limit = base_threshold * (1 + sensitivity_factor)
    filtered_data = [x for x in raw_readings if x > dynamic_limit]

    # Decoy statistical computation (dead path)
    mean_val = sum(raw_readings) / len(raw_readings)
    variance = sum((x - mean_val) ** 2 for x in raw_readings) / len(raw_readings)
    std_dev = variance ** 0.5
    z_scores = [(x - mean_val) / std_dev for x in raw_readings]

    # Unused anomaly detection based on z-score (red herring)
    for z in z_scores:
        if abs(z) > 2.0:
            outlier_flags.append(True)
        else:
            outlier_flags.append(False)

    # Build threshold map using defaultdict (relevant)
    threshold_map = defaultdict(int)
    for i, val in enumerate(filtered_data):
        key = f"sensor_{i % 3}"
        threshold_map[key] += val // 10

    # Spurious string manipulation (irrelevant)
    status_tags = ['OK', 'WARN', 'CRIT']
    tag_sequence = ''.join([t * (i + 1) for i, t in enumerate(status_tags)])
    reversed_tags = tag_sequence[::-1]

    # Dummy recursive function that's never called (decoy)
    def recursive_checksum(data, n):
        if n <= 0:
            return 0
        return data[n % len(data)] + recursive_checksum(data, n - 1)

    # Real analysis function (called later)
    def analyze_readings(readings, thresholds):
        total_impact = 0
        contributions = []

        # Process each reading with conditional weighting
        for val in readings:
            if val < 120:
                weight = 1.1
            elif val < 135:
                weight = 1.3
            else:
                weight = 1.6

            impact = val * weight
            contributions.append(impact)

            # Early break condition (not triggered here)
            if impact > 200:
                break

        # Aggregate using Counter on digit frequency (set operation distractor)
        digit_counter = Counter()
        for num in readings:
            for digit in str(num):
                digit_counter[digit] += 1

        common_digits = set(digit_counter.keys())
        rare_contribution = 0
        if '9' in common_digits:
            rare_contribution += 5

        total_impact = int(sum(contributions) + rare_contribution)

        # Dead code: unused transformation
        squared_sums = [x ** 2 for x in readings]
        avg_square = sum(squared_sums) / len(squared_sums)

        return total_impact

    # Critical assignment point
    final_diagnostic = analyze_readings(filtered_data, threshold_map)

    # Unused nested structure (distractor)
    metadata_log = {
        'version': '2.1.0',
        'nodes': [
            {'id': 1, 'active': True, 'payload': [1, 1, 2]},
            {'id': 2, 'active': False, 'payload': [3, 5, 8]},
            {'id': 3, 'active': True, 'payload': [13, 21]}
        ]
    }

    # Final result output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execute and capture result
collect_diagnostics()