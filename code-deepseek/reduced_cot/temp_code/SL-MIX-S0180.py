def process_text_analysis(text_data):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    processed_chars = set()
    temp_counter = 0
    
    for char in text_data.lower():
        if char.isalpha():
            processed_chars.add(char)
            temp_counter += ord(char)
    
    # Distractor operations that don't affect the final result
    intermediate_sum = sum(ord(c) for c in text_data)
    char_frequency = len(text_data) - len(set(text_data))
    
    unique_vowels = vowels.intersection(processed_chars)
    result_set = unique_vowels.intersection(processed_chars)
    final_output = len(result_set)
    
    # Additional irrelevant computation
    redundant_calc = len(text_data) * 2 - temp_counter // 10
    
    print(f"Target result: {final_output}")

# Main execution
text_sample = "Programming Language Analysis"
process_text_analysis(text_sample)