def process_characters(text_data):
    # Initial processing - count uppercase characters
    upper_count = sum(1 for char in text_data if char.isupper())
    
    # Distractor: Process vowels but don't use in final calculation
    vowel_count = sum(1 for char in text_data.lower() if char in 'aeiou')
    vowel_ratio = vowel_count / len(text_data) if text_data else 0
    
    # Main logic - count alphanumeric characters
    alnum_chars = [char for char in text_data if char.isalnum()]
    alnum_count = len(alnum_chars)
    
    # Intermediate calculation with modular arithmetic
    mod_base = 7
    mod_result = alnum_count % mod_base
    
    # Combine counts with some operations
    combined_count = upper_count + alnum_count
    adjustment = (combined_count // 3) * 2
    
    # Final processing
    final_count = combined_count - adjustment + mod_result
    group_factor = 4
    processed_total = final_count // group_factor
    
    print(f"Result: {processed_total}")
    return processed_total

# Main execution
text_sample = "PyTh0n_Pr0gr@mming_2024!"
result = process_characters(text_sample)