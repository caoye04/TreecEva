def analyze_text_pattern(text_sample):
    # Process character data
    char_codes = [ord(c) for c in text_sample]
    
    # Calculate various metrics (some are distractors)
    avg_code = sum(char_codes) // len(char_codes)
    max_code = max(char_codes)
    min_code = min(char_codes)
    
    # Perform slicing operations
    first_half = char_codes[:len(char_codes)//2]
    second_half = char_codes[len(char_codes)//2:]
    
    # Apply bitwise operations
    encoded_chars = []
    for code in char_codes:
        # XOR with position-based key
        encoded = code ^ (len(text_sample) % 8)
        encoded_chars.append(encoded)
    
    # Process second half with different operations (distractor)
    processed_data = []
    for val in second_half:
        processed = (val & 0x0F) | ((val >> 4) & 0x0F)
        processed_data.append(processed)
    
    # Calculate final result using specific positions
    intermediate = encoded_chars[1] & processed_data[0]  # Distractor operation
    final_score = encoded_chars[2] ^ processed_data[-1]  # Key operation
    
    # Print result for verification
    print(f"Result: {final_score}")
    return final_score

# Execute the analysis
text_data = "PyThOn3"
result = analyze_text_pattern(text_data)