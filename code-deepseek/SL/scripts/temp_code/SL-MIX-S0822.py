import itertools

def process_data(text_input):
    # Process text data through multiple transformations
    words = text_input.split('_')
    processed_chunks = []
    
    # Intermediate processing that doesn't affect final result
    temp_count = sum(len(word) for word in words)  # Redundant calculation
    
    for word in words:
        # Apply case conversion and filtering
        upper_word = word.upper()
        if len(upper_word) > 3:
            processed_chunks.append(upper_word)
    
    # Generate combinations (distractor operation)
    combinations = list(itertools.combinations(processed_chunks, 2))
    combo_count = len(combinations)  # Unused variable
    
    # Core logic with string operations and comparisons
    joined_result = '-'.join(processed_chunks)
    final_length = len(joined_result)
    
    # Boolean logic with comparisons
    length_check = (final_length > 15) and (final_length < 30)
    adjust_value = 5 if length_check else 2
    
    # Final computation
    result_value = final_length * adjust_value
    
    # Additional distractor operations
    dummy_operation = result_value + temp_count - combo_count
    
    return result_value

input_string = "data_processing_test_case_example"
result = process_data(input_string)
final_output = result
print(f"Target result: {final_output}")