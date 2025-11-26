def calculate_text_offsets():
    text_data = "programming_evaluation_benchmark"
    # Process the text data
    processed_data = text_data.replace('_', '').upper()
    
    # Calculate initial offset (distractor - not used in final calculation)
    initial_offset = len(text_data) * 2
    
    # Get substring positions
    substr_start = text_data.find('eval')
    substr_end = text_data.rfind('mark')
    
    # Calculate offset adjustment using slicing
    relevant_slice = text_data[substr_start:substr_end + 4]
    offset_adjustment = len(relevant_slice) // 2
    
    # Additional unused computation (interference)
    temp_calc = (initial_offset - substr_start) * 3
    unused_result = temp_calc % 7
    
    # Final calculation
    final_offset = offset_adjustment + len(processed_data)
    print(f"Target result: {final_offset}")

calculate_text_offsets()