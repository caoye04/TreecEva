def analyze_data_stream(raw_input):
    # Irrelevant preprocessing: reverse and slice
    reversed_data = raw_input[::-1]
    offset_view = reversed_data[2:9:2]

    # Distractor variables with misleading calculations
    temp_factor = sum([i * 2 for i in range(7)])  # = 42, unused later
    dummy_mask = 0xFF
    padding_length = len(raw_input) % 8

    # Real processing begins: extract digits and filter
    digit_chars = [c for c in raw_input if c.isdigit()]
    numeric_values = [int(d) for d in digit_chars]

    # Decoy transformation using enumerate and string methods
    indexed_map = []
    for idx, val in enumerate(numeric_values):
        shifted = (val + idx) % 10
        str_rep = str(shifted).zfill(2)
        indexed_map.append(int(str_rep))  # Red herring list

    # Another decoy: zip-based pairing with no impact
    paired_data = list(zip(numeric_values, numeric_values[1:]))
    edge_score = 0
    for a, b in paired_data:
        edge_score += (a ^ b) & 0x0F  # Computed but unused

    # Actual logic path starts here — hidden among noise
    base_sequence = [v for i, v in enumerate(numeric_values) if v % 2 == i % 2]
    extended_sequence = base_sequence + [base_sequence[0] ^ base_sequence[-1]]

    # Critical data structure: valid_sequence derived from complex rules
    valid_sequence = []
    for num in extended_sequence:
        if num > 0:
            transformed = (num ** 2) // 3
            if transformed % 2 == 0:
                valid_sequence.append(transformed | 1)
            else:
                valid_sequence.append(transformed)

    # Running total initialization — key starting point
    running_total = 0
    for ch in raw_input:
        if ch.isalpha():
            running_total += ord(ch.lower()) - ord('a')

    # Final loop with critical statement embedded
    checksum = 0
    for i in range(len(valid_sequence)):
        if i % 2 == 1:
            # Key update point — this line determines final answer
            checksum = (valid_sequence[i] << 1) ^ running_total
        else:
            # Dead-end branch: modifies local var only
            temp_checksum = checksum ^ valid_sequence[i]
            temp_checksum += 5

    # Output required result
    print(f"Result: {checksum}")

# Input with mixed alphanumeric content
input_str = "A7B3C9X2M8K1N4"
analyze_data_stream(input_str)