from collections import defaultdict, Counter

# Simulate sensor data stream with noise and valid readings
def process_sensor_data(raw_stream):
    stats = defaultdict(int)
    frequencies = Counter()
    temp_buffer = []
    cumulative = 0
    outlier_count = 0
    normalization_factor = 1.0
    scaling_offset = 0

    # Irrelevant pre-processing: analyze frequency distribution
    for val in raw_stream:
        frequencies[val] += 1
        if val > 95 or val < 5:
            outlier_count += 1

    # Normalize data based on outlier statistics (unused path)
    if outlier_count > len(raw_stream) * 0.1:
        normalization_factor = 0.9
        scaling_offset = 5
    else:
        normalization_factor = 1.1

    adjusted_values = []
    for val in raw_stream:
        adjusted = int(val * normalization_factor) + scaling_offset
        adjusted_values.append(adjusted)

    # Begin core checksum calculation (critical path)
    checksum = 543
    phase_key = 7
    history_log = []

    for idx, (raw, adj) in enumerate(zip(raw_stream, adjusted_values)):
        # Distraction: logging and stats update (partially irrelevant)
        stats['total'] += 1
        stats['sum_raw'] += raw
        temp_buffer.append(adj)

        # Complex conditional with red herring operations
        if idx % 3 == 0:
            shift_op = (idx // 3) % 5
            cumulative += (raw ^ phase_key) >> shift_op
n        elif idx % 3 == 1:
            # Fake transformation chain
            transformed = adj
            for _ in range(2):
                transformed = (transformed ^ 17) % 100
            stats['dummy_metric'] = transformed

        # Core logic embedded within distractions
        processed_value = (adj ^ phase_key) & 255
        if idx % 4 == 0:
            processed_value = (processed_value * 3) % 256

        # Key statement — answer is derived from this line's effect
        checksum = (checksum << 1) ^ processed_value if processed_value % 2 else (checksum >> 1) ^ processed_value

        # More distraction: history tracking that isn't used later
        history_log.append({'index': idx, 'raw': raw, 'chk': checksum})

        # Dead code branch (never executed due to data)
        if len(temp_buffer) > 1000:
            temp_buffer.clear()

    # Final irrelevant transformation
    final_count = sum(1 for x in history_log if x['chk'] > 1000)
    result_scalar = len(stats) * 0.5

    # Output the target variable
    print(f"Result: {checksum}")

# Input data: deterministic sensor stream
sensor_input = [12, 45, 67, 89, 23, 56, 78, 34, 88, 12, 67, 45, 29, 77, 55]
process_sensor_data(sensor_input)