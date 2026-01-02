def analyze_data_stream(raw_input):
    # Preprocess input: remove noise tags and split into tokens
    cleaned = raw_input.replace("<NOISE>", "").strip()
    tokens = cleaned.split(',')

    # Initialize tracking variables
    valid_count = 0
    temp_sum = 0
    rolling_avg_numerator = 0
    debug_log = []  # Unused debugging artifact (distractor)
    intermediate_results = []  # Semi-relevant, used for logging but not final result

    threshold = 42
    mask = 0xFF  # Used in final XOR-mask operation

    # Simulate signal validation with mixed conditions
    for token in tokens:
        stripped = token.strip()
        if not stripped.isdigit():
            continue

        value = int(stripped)
        is_valid = value > threshold and len(stripped) <= 3

        # Track valid entries
        if is_valid:
            valid_count += 1
            temp_sum += value
            intermediate_results.append(value * 0.95)  # Scaled for potential future use

        # Red herring: complex-looking but unused calculation
        if value % 7 == 0:
            dummy_calc = (value ** 2) + len(token)  # Dead-end computation
            debug_log.append(f"Debug: {dummy_calc}")

        # Another distractor: unrelated string processing
        reversed_chars = ''.join(reversed(token))
        if '5' in reversed_chars:
            _ = reversed_chars.count('5')  # Irrelevant count

        # Update numerator for a never-used average
        rolling_avg_numerator += value

    # Final integrity checksum using bitwise operations
    checksum = (valid_count ^ temp_sum) & mask

    # Print result as required
    print(f"Result: {checksum}")

# Input stream with mixed valid/invalid data
input_stream = "<NOISE>30,45,100,<NOISE>7,84,999,102,77<NOISE>,55"
analyze_data_stream(input_stream)