def process_text_analysis(text):
    # Initialize counters and processing variables
    total_chars = len(text)
    vowel_counter = lambda s: sum(1 for c in s.lower() if c in 'aeiou')
    consonant_counter = lambda s: sum(1 for c in s.lower() if c.isalpha() and c not in 'aeiou')
    
    # Main processing chain with some distractor operations
    vowel_count = vowel_counter(text)
    consonant_count = consonant_counter(text)
    
    # Distractor calculations that don't affect final result
    temp_ratio = vowel_count / consonant_count if consonant_count > 0 else 0
    char_product = total_chars * vowel_count
    
    # Intermediate processing with lambda functions
    adjust_vowels = lambda x: (x * 3) % 7
    processed_vowels = adjust_vowels(vowel_count)
    
    # More distractors - these operations are irrelevant
    dummy_sum = processed_vowels + consonant_count
    offset_value = (dummy_sum - 5) * 2
    
    # Key logic: vowel count modulo consonant count (avoiding division by zero)
    if consonant_count > 0:
        final_count = vowel_count % consonant_count
    else:
        final_count = vowel_count
    
    # Final assignment
    result = final_count
    print(f"Result: {result}")

# Execute with sample text
sample_text = "programming evaluation benchmark"
process_text_analysis(sample_text)