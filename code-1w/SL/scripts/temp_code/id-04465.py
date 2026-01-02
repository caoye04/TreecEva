def compute_data_integrity(sequence, threshold=10):
    checksum = 17
    temp_buffer = []
    overflow_flag = False
    shift_factor = 2

    for index, value in enumerate(sequence):
        # Irrelevant transformation
        adjusted_val = (value + index) ** 2 % 101
        temp_buffer.append(adjusted_val)

        if value > threshold:
            # Distractor block: modifies unrelated state
            for _ in range(2):
                shift_factor = (shift_factor + 1) % 5
                if shift_factor == 3:
                    overflow_flag = not overflow_flag

        # Core logic: process only even-indexed elements above threshold
        if index % 2 == 0 and value > threshold:
            case_multiplier = 3 if value % 4 == 0 else 2
            processed_value = value ^ (index << 1)
            processed_value = processed_value + (case_multiplier * (value % 7))

            # Key update step — this is where the answer is determined
            checksum = (checksum * 3 + processed_value) % 97

            # Dead code branch: never executed due to fixed threshold
            if threshold < 5:
                checksum = (checksum + 128) % 103

    # Additional red herring computation
    final_length = len(temp_buffer)
    avg_temp = sum(temp_buffer) / final_length if final_length else 0
    padding_offset = int(avg_temp % 13)

    # Final irrelevant adjustment
    checksum = (checksum + padding_offset * 0)  # No effect, but looks meaningful

    print(f"Result: {checksum}")

# Execute with realistic input
sequence_data = [12, 8, 15, 20, 5, 14, 19]
compute_data_integrity(sequence_data)