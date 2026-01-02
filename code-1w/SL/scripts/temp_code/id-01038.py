def analyze_data_stream():
    # Simulated sensor readings (temperature in tenths of degrees)
    raw_readings = [234, 189, 256, 178, 201, 222, 198, 245, 267, 188, 205]

    # Thresholds for anomaly detection
    lower_bound = 190
    upper_bound = 250

    # Derived metrics (some are red herrings)
    average_temp = sum(raw_readings) / len(raw_readings)
    temp_variance = sum((x - average_temp) ** 2 for x in raw_readings) / len(raw_readings)
    normalized_readings = [(x - min(raw_readings)) / (max(raw_readings) - min(raw_readings)) for x in raw_readings]

    # Flag suspicious patterns (unused flags act as distractors)
    has_spike = any(abs(raw_readings[i] - raw_readings[i-1]) > 30 for i in range(1, len(raw_readings)))
    is_stable = not has_spike and temp_variance < 500
    system_status = 'STABLE' if is_stable else 'WARNING'

    # Historical baselines (irrelevant to final computation)
    historical_avg = 210
    drift_compensation = (average_temp - historical_avg) * 0.1

    # Signal filtering: extract readings within normal operating range
    valid_readings = [temp for temp in raw_readings if lower_bound <= temp <= upper_bound]

    # Generate product codes for traceability (mostly irrelevant)
    base_codes = ['PX2', 'QY9', 'RZ3', 'SA7', 'TB1']
    extended_codes = [c + str(i % 3) for i, c in enumerate(base_codes)]
    code_mapping = {i: extended_codes[i % len(extended_codes)] for i in range(len(valid_readings))}

    # Compute derived diagnostic values (distractor computations)
    squared_norms = [round(n**2 * 100) for n in normalized_readings]
    checksum = sum(squared_norms[i] * (i + 1) for i in range(len(squared_norms))) % 97

    # Critical data transformation path
    adjusted_values = [v - int(drift_compensation) for v in valid_readings]

    # Identify potential harmonic interference (dead logic branch)
    harmonic_risk = False
    for i in range(2, len(adjusted_values)):
        if adjusted_values[i] == adjusted_values[i-1] == adjusted_values[i-2]:
            harmonic_risk = True
            break  # Never triggers with this dataset

    # Map to frequency bins (decoy structure)
    bins = {i: [] for i in range(5)}
    for val in adjusted_values:
        bin_key = (val // 10) % 5
        bins[bin_key].append(val)

    # Core calculation: cross-correlation of adjacent valid pairs
    paired_deltas = [adjusted_values[i+1] - adjusted_values[i] for i in range(len(adjusted_values)-1)]
    
    # Product of delta and original value for entropy estimation (distraction)
    pseudo_entropy = sum(abs(d * adjusted_values[i]) for i, d in enumerate(paired_deltas))

    # Real signal: compute products of consecutive adjusted values
    relevant_products = []
    for i in range(len(adjusted_values) - 1):
        prod = adjusted_values[i] * adjusted_values[i + 1]
        if prod % 2 == 1:  # Only odd products are relevant (non-obvious condition)
            relevant_products.append(prod)

    filtered_sum = sum(relevant_products)

    # Final system diagnostics (irrelevant output)
    report_id = ''.join([chr(97 + (checksum >> i) % 26) for i in range(0, 18, 3)])
    timestamp_correlation = (checksum * 17) & 0xFFFF

    # Output target result
    print(f"Result: {filtered_sum}")

analyze_data_stream()