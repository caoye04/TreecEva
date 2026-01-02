def process_sensor_data(raw_readings):
    # Irrelevant preprocessing: normalize values (not used in final result)
    normalized = [round(x * 0.98 + 0.5, 2) for x in raw_readings if x > 0]
    temp_offsets = list(map(lambda x: abs(x - 50), raw_readings))
    threshold = sum(temp_offsets) / len(temp_offsets) if temp_offsets else 0

    # Real data path: filter and transform
    valid_mask = [i for i in range(len(raw_readings)) if i % 2 == 1]  # Only odd indices
    filtered_data = [raw_readings[i] for i in valid_mask if raw_readings[i] % 4 == 0]

    # Dead code branch: looks important but unused
    if len(normalized) > 5:
        moving_avg = [sum(normalized[i:i+3]) / 3 for i in range(len(normalized) - 2)]
        spike_count = len([x for x in moving_avg if x > threshold])

    # Core transformation chain
    shift_op = lambda x: x ^ 0b1010  # Bitwise red herring
    transformed = [((x >> 2) + (x << 1)) % 100 for x in filtered_data]  # Arithmetic mangling

    # Decoy accumulation (never used)
    cumulative = []
    acc = 0
    for val in transformed:
        acc += val * 1.5
        cumulative.append(int(acc % 1000))

    # Actual computation path
    def reduce_sequence(seq):
        result = 0
        for i, v in enumerate(seq):
            result += v * (i + 1)  # Weighted sum
        return result

    def finalize(value):
        # Mix of operations, only one path matters
        a = value * 3
        b = a + 17
        c = b ** 0.5
        return int(c) if c > 10 else int(a % 19)  # Deterministic path

    # Critical assignment point
    checksum = finalize(reduce_sequence(transformed))

    # More distractions: unused diagnostics
    diagnostics = {
        'raw_count': len(raw_readings),
        'filtered_ratio': len(filtered_data) / len(raw_readings),
        'max_shift': max([shift_op(x) for x in filtered_data]) if filtered_data else 0
    }

    # Final output
    print(f"Result: {checksum}")

# Simulate sensor input (deterministic)
data_stream = [16, 24, 7, 32, 45, 48, 13, 40, 55, 64]
process_sensor_data(data_stream)