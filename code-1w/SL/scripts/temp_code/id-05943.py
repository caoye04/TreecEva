def compute_integrity_code(sequence, threshold=10):
    # Simulate data packet integrity computation with noise filtering
    filtered_stream = []
    temp_accumulator = 0
    noise_counter = 0

    for item in sequence:
        # String-based type tagging and filtering
        tag = str(type(item).__name__)
        if 'int' in tag.lower() and item > 0:
            temp_accumulator += item ** 0.5
            if item % 3 == 0:
                noise_counter += 1  # Track multiples of 3 as 'noise'
            else:
                filtered_stream.append(int(item / 2))
        elif isinstance(item, str) and item.isdigit():
            # Misleading string handling branch
            temp_accumulator -= len(item)

    # Secondary processing: only even-indexed values matter
    relevant_data = []
    for i in range(len(filtered_stream)):
        if i % 2 == 0:
            relevant_data.append(filtered_stream[i])
        else:
            # Dead code path - collected but unused
            _ = filtered_stream[i] * 2  

    # Core checksum calculation with bitwise manipulation
    checksum = 17
    base_shift = 2
    mask = 255
    history_log = []  # Logged but not used in final result

    for val in relevant_data:
        processed_value = val % 19
        if processed_value < threshold:
            # Key update step
            checksum = (checksum << 1) ^ processed_value ^ mask
            history_log.append(f"Step_{val}: {checksum}")
        else:
            checksum += 1  # Rarely triggered due to threshold

    # Final red herring: floating-point transformation
    final_ratio = temp_accumulator / (checksum + 1e-5)
    scaled_result = round(final_ratio * 100, 4)

    print(f"Result: {checksum}")

# Execute with test input
data_sequence = [24, '15', 36, 18, 'abc', 21, 48, 12]
compute_integrity_code(data_sequence)