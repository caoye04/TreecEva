def process_transmission(data, mask):
    intermediate = 0
    checksum = 0
    temp_result = []

    # Misleading pre-processing (distractor)
    for i in range(len(data)):
        if data[i] % 2 == 0:
            checksum += data[i] * 3
        else:
            checksum -= data[i] * 2

    # Actual signal processing logic (core path)
    transform = lambda x: (x ^ mask) + 1
    for val in data:
        transformed = transform(val)
        if transformed % 4 == 0:
            intermediate += transformed // 4
        else:
            intermediate += transformed % 4

    # Red herring: unused computation on a copy
    backup_data = [x + 1 for x in data]
    for x in backup_data:
        if x > 10:
            temp_result.append(x * 2)  # Dead code path (not used)

    # Final adjustment based on intermediate state
    if intermediate > 50:
        intermediate = intermediate // 3
    else:
        intermediate = (intermediate + 7) * 2

    return intermediate

# Simulate sensor data sequence and transmission key
data_sequence = [12, 7, 3, 19, 4, 8, 11]
key_mask = 5
noise_floor = sum([x**2 for x in data_sequence]) // 100  # Irrelevant metric
baseline_offset = len(data_sequence) * 2  # Unused offset

encoded_sequence = [x + noise_floor for x in data_sequence]

# Key execution point
final_signal = process_transmission(encoded_sequence, key_mask)

print(f"Result: {final_signal}")