def analyze_sensor_data(raw_readings, thresholds):
    # Irrelevant preprocessing block (dead path)
    temp_buffer = [0] * len(raw_readings)
    for i in range(len(raw_readings)):
        if raw_readings[i] < -50:  # Rare condition never met
            temp_buffer[i] = abs(raw_readings[i]) >> 2

    # Distractor: complex but unused transformation
    transformed = []
    for val in raw_readings:
        base = val & 0xFF
        shift_op = (base << 3) ^ 0xAA
        transformed.append(shift_op % 17)

    # Real computation begins: filter valid readings
    valid_readings = []
    outlier_count = 0
    for reading in raw_readings:
        if thresholds[0] <= reading <= thresholds[1]:
            valid_readings.append(reading)
        else:
            outlier_count += 1

    # Secondary distractor: character counting in debug mode (never activated)
    debug_mode = False
    diagnostic_log = "Sensor analysis v3.2"
    char_count = sum(1 for c in diagnostic_log if c.isalpha()) if debug_mode else 0

    # Core logic hidden among noise
    baseline = sum(valid_readings) / len(valid_readings) if valid_readings else 0
    variance_pool = [(x - baseline) ** 2 for x in valid_readings]
    avg_variance = sum(variance_pool) / len(variance_pool) if variance_pool else 0

    # Bit manipulation red herring
    magic_seed = 0xDEADBEEF
    masked = magic_seed & 0xFFFF
    hashed = (masked ^ 0xCAFEBABE) & 0xFFFFFFFF

    # Actual signal chain
    signal_strength = 0
    for idx, val in enumerate(valid_readings):
        if idx % 2 == 0:
            signal_strength += val * 3
        else:
            signal_strength -= val

    # Data fusion using zip and slicing
    segment_a = valid_readings[:len(valid_readings)//2]
    segment_b = valid_readings[len(valid_readings)//2:]
    coherence_pairs = list(zip(segment_a, segment_b[::-1]))  # Reverse second half
    coherence_score = sum(a & b for a, b in coherence_pairs)  # Bitwise AND across pairs

    # Final aggregation with multiple distractors
    aggregate_result = signal_strength + coherence_score
    correction_factor = max(1, outlier_count - char_count)  # char_count=0, so no effect

    # Critical statement
    filtration_score = aggregate_result // correction_factor

    # Unused decoy function call
    def compute_entropy(data): return 0
    entropy = compute_entropy(raw_readings)

    # Output target result
    print(f"Result: {filtration_score}")

# Execute with realistic sensor data
sensor_input = [120, 145, 98, 167, 134, 112, 156, 101, 177, 129]
thresh_bounds = (90, 180)
analyze_sensor_data(sensor_input, thresh_bounds)