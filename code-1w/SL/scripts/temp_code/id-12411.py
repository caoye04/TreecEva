from collections import defaultdict

# Simulated sensor data processing with red herrings
def process_sensor_readings(raw_data):
    readings_count = len(raw_data)
    temp_stats = defaultdict(int)
    cumulative = 0
    checksum = 0
    outlier_flags = []

    # Irrelevant statistical tracking (distractor)
    for val in raw_data:
        if val > 300:
            temp_stats['high'] += 1
        elif val < 100:
            temp_stats['low'] += 1
        else:
            temp_stats['normal'] += 1

    # Decoy transformation - unused result (dead code path)
    transformed = [((x >> 2) ^ 15) & 255 for x in raw_data]
    aggregate_score = sum(transformed) % 97

    # Real data path begins here
    filtered_data = [x for x in raw_data if 50 <= x <= 450]  # Valid range filter

    # Secondary filtering based on index parity (meaningful)
    indexed_weights = {}
    for i, value in enumerate(filtered_data):
        if i % 2 == 0:
            indexed_weights[i] = value * 1.1
        else:
            indexed_weights[i] = value * 0.9

    # Accumulate only the values, not weights
    data_sum = int(sum(filtered_data))  # Key accumulation

    # Position-based weighting using slice and index logic
    mid_point = len(filtered_data) // 2
    left_half = filtered_data[:mid_point]
    right_half = filtered_data[mid_point:]

    # Weight derived from structural property (not actual sum)
    position_weight = len(left_half) ^ len(right_half)

    # Critical statement: checksum computation
    checksum = (data_sum ^ position_weight) & 0xFFFF

    # More red herrings below
    anomaly_sequence = [a ^ b for a, b in zip(left_half, right_half[::-1])]
    security_hash = sum(anomaly_sequence) * 31 % 65537

    debug_info = {
        'raw_length': readings_count,
        'filtered_length': len(filtered_data),
        'temp_bands': dict(temp_stats),
        'security_hash': security_hash,
        'aggregate_score': aggregate_score
    }

    return checksum  # Only this matters

# Input data with subtle patterns
input_stream = [88, 105, 52, 320, 401, 44, 203, 99, 150, 451, 399, 101, 222]

# Execute
result = process_sensor_readings(input_stream)
print(f"Result: {result}")