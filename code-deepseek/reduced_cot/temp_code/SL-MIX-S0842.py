def process_text_data(text_input):
    # Initial processing steps
    word_count = len(text_input.split())
    char_count = len(text_input)
    vowel_count = sum(1 for char in text_input.lower() if char in 'aeiou')
    
    # Intermediate calculations (some not directly used)
    consonant_ratio = (char_count - vowel_count) / char_count if char_count > 0 else 0
    avg_word_length = char_count / word_count if word_count > 0 else 0
    
    # Core processing
    text_upper = text_input.upper()
    processed_chars = ''.join(char for char in text_upper if char.isalpha())
    char_frequency = len(processed_chars)
    
    # Additional operations that don't affect final result
    temp_buffer = char_frequency * 2
    dummy_operation = temp_buffer // 3
    
    # Key calculation path
    base_value = char_frequency + vowel_count
    adjustment_factor = word_count % 5
    offset_correction = 7
    
    # Final computation
    processed_value = base_value * 3
    final_operation = processed_value * adjustment_factor - offset_correction
    
    print(f"Result: {processed_value}")
    return processed_value

# Execute the function
sample_text = "The quick brown fox jumps"
result = process_text_data(sample_text)