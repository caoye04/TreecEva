import itertools

def analyze_sensor_network():
    # Simulated sensor IDs and raw readings
    sensor_ids = ['S1', 'S2', 'S3', 'S4', 'S5']
    base_readings = [23.4, 19.8, 27.1, 22.0, 30.5]
    calibration_offsets = [0.5, -0.3, 0.8, -0.6, 1.0]

    # Apply calibration (relevant)
    calibrated_readings = [base_readings[i] + calibration_offsets[i] for i in range(len(base_readings))]

    # Irrelevant: Timestamp generation (distractor)
    timestamps = ["2023-09-{}T10:0{}:00Z".format(i+1, i) for i in range(5)]

    # Compute derived metrics – some relevant, some not
    averages = sum(calibrated_readings) / len(calibrated_readings)  # Used later
    variance_proxy = sum((x - averages)**2 for x in calibrated_readings) / len(calibrated_readings)
    std_dev = variance_proxy ** 0.5

    # Irrelevant: String transformations on sensor IDs (red herring)
    encoded_labels = [s.lower().replace('s', 'x') for s in sensor_ids]
    reversed_labels = [s[::-1] for s in encoded_labels]

    # Distractor function: never called
    def decrypt_signal(data):
        return [d ^ 255 for d in data]  # Bitwise XOR red herring

    # Real processing begins: filter sensors above average + 0.5 * std_dev
    dynamic_threshold = averages + 0.5 * std_dev
    status_flags = [reading > dynamic_threshold for reading in calibrated_readings]

    # Map statuses with enumerate (python idiom)
    critical_sensors = [i for i, flag in enumerate(status_flags) if flag]

    # Extract filtered data using list comprehension and zip (relevant)
    raw_with_id = list(zip(sensor_ids, calibrated_readings))
    filtered_data = [reading for sid, reading in raw_with_id if sid in [sensor_ids[i] for i in critical_sensors]]

    # Decoy variables (misleading intermediate)
    temp_aggregate = sum([int(r) for r in calibrated_readings])  # Truncated ints, unused
    checksum = 0
    for val in calibrated_readings:
        checksum ^= int(val * 10)  # Bit manipulation distractor

    # Auxiliary transformation: case conversion chain (irrelevant)
    upper_ids = [sid.upper() for sid in sensor_ids]
    flipped_case = [c.swapcase() for c in upper_ids]

    # Core logic: process only filtered data above threshold
    def process_readings(data, thresh):
        if not data:
            return -999.0
        # Apply non-linear correction
        adjusted = [abs(d - thresh) * 1.5 for d in data]
        # Use itertools to pair consecutive elements
        paired = list(itertools.zip_longest(adjusted, adjusted[1:], fillvalue=0))
        scores = []
        for a, b in paired:
            if a > b:  # Introduce control flow
                scores.append(a - b * 0.3)
            else:
                scores.append(b + a * 0.2)
        # Final aggregation
        return round(sum(scores) / len(scores), 4) if scores else 0.0

    # Threshold used in processing (derived earlier)
    threshold = dynamic_threshold

    # Critical assignment: this is the target execution point
    final_diagnostic = process_readings(filtered_data, threshold)

    # Dead code path: never executed
    if False:
        fallback = [x for x in filtered_data if x < 0]
        final_diagnostic -= sum(fallback)

    # Output result as required
    print(f"Result: {final_diagnostic}")

analyze_sensor_network()