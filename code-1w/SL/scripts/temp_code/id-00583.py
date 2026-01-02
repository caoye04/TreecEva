def analyze_pattern_sequence(data_stream):
    pattern_count = 0
    temp_buffer = []
    for char in data_stream:
        if char.isupper():
            temp_buffer.append(char.lower())
        elif char.isdigit():
            temp_buffer.append(str(int(char) * 2))
    processed = ''.join(temp_buffer)
    return len(processed)


def calculate_entropy(signal):
    # Irrelevant entropy calculation (not used in final result)
    from collections import Counter
    counts = Counter(signal)
    total = len(signal)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Simulated pseudo-entropy
    return round(entropy, 4)


def calculate_performance_rating():
    raw_input = "AbC1dE2fG3hI"
    offset_value = 7
    scaling_factor = 3
    
    # Step 1: Use string methods and list comprehension to filter and transform
    filtered_chars = [c for c in raw_input if c.isalpha()]
    
    # Step 2: Count uppercase letters (relevant)
    uppercase_count = sum(1 for c in filtered_chars if c.isupper())
    
    # Step 3: Apply transformation using bitwise XOR on ASCII values
    transformed_values = []
    for i, c in enumerate(filtered_chars):
        shifted = ord(c) ^ (i % 5)  # Bitwise interference
        transformed_values.append(shifted)
    
    # Step 4: Compute average of transformed ASCII values
    avg_transformed = sum(transformed_values) // len(transformed_values)
    
    # Step 5: Analyze pattern sequence (invokes side computation)
    dummy_signal = "XyZ9"
    dummy_analysis_result = analyze_pattern_sequence(dummy_signal)
    
    # Step 6: Calculate base score using modular arithmetic
    base_score = (avg_transformed + uppercase_count) % 100
    
    # Step 7: Scale and adjust with irrelevant intermediate
    noise_correction = calculate_entropy(raw_input)  # Computed but not used
    final_score = (base_score * scaling_factor) - offset_value
    
    # Final assignment point
    final_score = final_score + len(filtered_chars)  # Add length adjustment
    
    print(f"Result: {final_score}")
    return final_score

# Execute function
calculate_performance_rating()