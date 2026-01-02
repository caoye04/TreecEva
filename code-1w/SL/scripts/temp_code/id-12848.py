def process_segments(buffer, size):
    temp_storage = []
    checksum = 0
    overflow_flag = False

    for i in range(0, len(buffer), size):
        segment = buffer[i:i + size]
        segment_sum = sum(segment)
        segment_len = len(segment)

        # Irrelevant string processing (distractor)
        label = f"chunk_{i//size}".upper().replace('_', '')
        label_value = sum(ord(c) for c in label) % 100

        # Dummy logic that doesn't affect final result
        if segment_sum > 100:
            temp_storage.append(segment_sum * 0.95)
        else:
            temp_storage.append(segment_sum)

        # Actual contribution to checksum
        normalized = segment_sum // (segment_len if segment_len != 0 else 1)
        checksum ^= (normalized * 37) % 97

        # Dead code path (never executed due to flag never being set)
        if overflow_flag and len(temp_storage) > 10:
            reset_counter = 0
            while reset_counter < 5:
                reset_counter += 1
            checksum = checksum % 50

    # More irrelevant computation
    average_temp = sum(temp_storage) / len(temp_storage) if temp_storage else 0
    stability_score = (average_temp * 100) // (checksum + 1)

    # Final transformation
    final_hash = 0
    for c in f"{checksum}":
        final_hash = (final_hash * 31 + ord(c)) % 10000

    return final_hash

# Initialization data
raw_data = list(range(15, 98, 3))
noise_floor = [x % 7 for x in raw_data]
data_buffer = [(x + y) % 43 for x, y in zip(raw_data, noise_floor)]
window_size = 5

# Additional unused variables (distractors)
padding_length = 16
dummy_matrix = [[i*j for j in range(4)] for i in range(4)]
lookup_table = {i: (i**2) % 59 for i in range(20)}

# Key execution point
final_checksum = process_segments(data_buffer, window_size)
print(f"Result: {final_checksum}")