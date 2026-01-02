def analyze_data_sequence(raw_input):
    # Preprocess: convert to uppercase and reverse for inspection
    processed_str = ''.join([c.upper() for c in raw_input]).strip()[::-1]
    
    # Extract numeric characters and their positions
    numeric_chars = []
    position_map = {}
    temp_sum = 0
    
    for idx, char in enumerate(processed_str):
        if char.isdigit():
            digit_val = int(char)
            numeric_chars.append(digit_val)
            position_map[idx] = digit_val * 2  # Red herring: not used later
            temp_sum += digit_val ** 2  # Irrelevant computation

    # Create shifted pairs (non-impacting)
    shifted_pairs = [(numeric_chars[i], numeric_chars[(i+1)%len(numeric_chars)]) 
                     for i in range(len(numeric_chars))] if numeric_chars else []
    
    # Compute moving average of window size 2 (unused)
    moving_averages = []
    for i in range(len(numeric_chars) - 1):
        avg_val = (numeric_chars[i] + numeric_chars[i+1]) / 2.0
        moving_averages.append(round(avg_val, 2))

    # Actual logic: filter digits at even indices in original numeric list
    filtered_digits = [v for i, v in enumerate(numeric_chars) if i % 2 == 0]
    
    # Transform via modulo pattern (real computation path)
    transformed = []
    for x in filtered_digits:
        if x > 0:
            transformed.append((x ** 3) % 7)
        else:
            transformed.append(0)
    
    # Final accumulation
    adjustment_factor = len(moving_averages) % 5 if moving_averages else 3
    base_accum = sum(transformed)
    
    # Distractor: complex-looking but unused expression
    phantom_calc = (temp_sum * len(shifted_pairs)) - (len(position_map) ** 2) if position_map else 0
    
    # Key assignment
    filtered_sum = sum(transformed) + adjustment_factor
    
    # Output result
    print(f"Result: {filtered_sum}")

    return filtered_sum

# Input with mixed alphanumeric and case variation
data_stream = "AbC3xL9mP2qR8nZ1"
result = analyze_data_sequence(data_stream)