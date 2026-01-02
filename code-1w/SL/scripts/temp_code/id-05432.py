def compute_integrity_score(input_str):
    # Irrelevant preprocessing: counts vowels but never used
    vowel_count = sum(1 for c in input_str.lower() if c in 'aeiou')
    reversed_chunks = [input_str[i:i+3][::-1] for i in range(0, len(input_str), 3)]
    
    # Distractor variables: plausible but unused in final calculation
    entropy_approx = 0.0
    for i, char in enumerate(input_str):
        entropy_approx += (i + 1) * ord(char) % 7
    entropy_approx = round(entropy_approx / len(input_str), 3) if input_str else 0

    # Dead code path: looks important but not called
    def validate_hierarchy(nodes):
        return sorted(nodes, key=lambda x: (len(x), x))

    # Actual data pipeline begins
    tokens = input_str.split(',')
    raw_values = []
    for token in tokens:
        stripped = token.strip().upper()
        if stripped.startswith('X'):
            continue  # filter out X-prefixed entries
        # Use string method and conditional expression
        numeric_part = int(stripped[1:]) if len(stripped) > 1 and stripped[1:].isdigit() else 0
        direction_flag = -1 if stripped.endswith('R') else 1
        adjusted_value = direction_flag * (numeric_part or ord(stripped[0]))
        raw_values.append(adjusted_value)
    
    # Intermediate transformation with red herring
    filtered_data = [v for v in raw_values if v > -100]
    offset_basis = sum(ord(c) for c in input_str[:5]) % 8 if len(input_str) >= 5 else 0
    
    # Core computation chain
    data_sum = sum(abs(x) for x in filtered_data) + offset_basis
    
    # Multiple distractors introduced earlier are ignored here
    temp_flags = [1 if x & 1 else -1 for x in filtered_data]
    parity_mask = sum(temp_flags) & 15
    
    # Key statement embedded in logic
    correction_factor = (parity_mask ^ 5) + 2
    modulus = 90001
    checksum = (data_sum * correction_factor) % modulus
    
    # Unused post-processing that looks relevant
    normalized_score = checksum / 90000.0
    confidence = 0.85 if normalized_score > 0.5 else 0.6
    
    # Output required variable
    print(f"Result: {checksum}")

# Simulate input
input_sequence = "A12,B34R,C56,D78,X99,E2F"
compute_integrity_score(input_sequence)