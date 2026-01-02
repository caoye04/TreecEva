def analyze_sensor_stream(raw_samples, calibration_key):
    # Irrelevant preprocessing: character frequency analysis (distractor)
    char_count = {}
    for sample in raw_samples:
        label = str(sample[0])
        for c in label:
            char_count[c] = char_count.get(c, 0) + 1

    # Misleading transformation: base conversion with no use (red herring)
    temp_encoded = 0
    for i, (tag, val) in enumerate(raw_samples):
        if isinstance(tag, str) and tag.isdigit():
            temp_encoded += int(tag) * (16 ** i % 7)

    # Actual relevant data filtering
    readings = [entry for entry in raw_samples if isinstance(entry[1], (int, float))]
    
    # Distractor: unused recursive function (dead code path)
    def calculate_entropy(data, acc=1.0):
        if len(data) <= 1:
            return acc
        mid = len(data) // 2
        return calculate_entropy(data[:mid], acc * 0.9) + calculate_entropy(data[mid:], acc * 0.1)

    # Relevant mapping: extract critical indices
    indexed_readings = list(enumerate([r[1] for r in readings]))

    # Decoy statistical computation (irrelevant)
    mean_val = sum(r[1] for r in readings) / len(readings) if readings else 0
    variance_proxy = sum((r[1] - mean_val) ** 2 for r in readings) / len(readings) if readings else 0

    # Real logic: filter based on dynamic condition
    threshold_map = {i: 10 + (i % 4) * 3 for i in range(len(indexed_readings))}
    filtered_pairs = []
    for idx, value in indexed_readings:
        if value > threshold_map[idx]:
            filtered_pairs.append((idx, value))
    
    # Distractor: zip used in meaningless context
    labels = [f'Sensor_{i}' for i in range(len(readings))]
    metadata = [f'Loc_X{i}Y{i+1}' for i in range(len(readings))]
    decoy_dataset = list(zip(labels, metadata, readings))

    # Unused bitwise manipulation (misleading intermediate)
    bit_signature = 0
    for idx, val in indexed_readings:
        bit_signature ^= (idx << 2) & 0xFF
        bit_signature ^= int(val) & 0x0F

    # Key transformation function (used later)
    def process_readings(pairs, thresholds):
        aggregate = 0
        for pos, (index, reading) in enumerate(pairs):
            weight = 1 + (reading // 10) % 4
            # Use of enumerate in meaningful calculation
            adjustment = (pos + 1) * weight
            aggregate += int(reading // 2) ^ adjustment  # Bitwise mix with position
        return aggregate + len(thresholds) // 2

    # Final computation depends only on this
    final_diagnostic = process_readings(filtered_pairs, threshold_map)

    # Redundant string operation (distractor)
    status_tag = "DIAGNOSTIC_{}".format("PASSED" if final_diagnostic > 50 else "FAILED")
    tokens = status_tag.lower().split('_')
    token_lengths = [len(t) for t in tokens]

    # Print required output
    print(f"Result: {final_diagnostic}")

# Simulate input
input_samples = [
    ('A7', 15), ('B3', 8), ('C9', 23), ('D2', 12), ('E5', 5), 
    ('F1', 18), ('G4', 9), ('H8', 27), ('I6', 4), ('J0', 11)
]

# Execute main logic
analyze_sensor_stream(input_samples, calibration_key=0x5A)