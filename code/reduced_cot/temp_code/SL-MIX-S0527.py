def analyze_text_fragments(text_data):
    # Distractor: unnecessary text processing
    temp_buffer = [char.upper() for char in text_data if char.isalpha()]
    distractor_count = len([c for c in temp_buffer if c in 'AEIOU'])
    
    # Relevant: extract numeric patterns and process
    numeric_chunks = []
    current_chunk = ''
    for char in text_data:
        if char.isdigit():
            current_chunk += char
        elif current_chunk:
            numeric_chunks.append(int(current_chunk))
            current_chunk = ''
    
    # Distractor: unused bitwise operation
    bit_mask = 0b1010
    unused_result = numeric_chunks[0] & bit_mask if numeric_chunks else 0
    
    # Relevant: filtering and transformation
    filtered_values = [x for x in numeric_chunks if x % 3 == 0 or x % 5 == 0]
    
    # Misleading intermediate calculation
    misleading_sum = sum(filtered_values) + distractor_count * 10
    
    # Distractor: dead code path
    if misleading_sum > 1000:
        dead_branch = misleading_sum // 2
    
    # Relevant: core processing with slicing
    if len(filtered_values) >= 4:
        middle_slice = filtered_values[1:-1]
        processed_slice = [val * 2 if val % 2 == 0 else val + 1 for val in middle_slice]
        processed_data = processed_slice
    else:
        processed_data = [x + 5 for x in filtered_values]
    
    # Add padding if needed (distractor)
    padding_size = max(0, 6 - len(processed_data))
    for _ in range(padding_size):
        processed_data.append(padding_size * 7)
    
    # Final relevant operation with slicing
    if len(processed_data) > 3:
        final_result = processed_data[-1]
    else:
        final_result = processed_data[0] if processed_data else 0
    
    print(f"Result: {final_result}")
    return final_result

# Main execution with mixed data
input_text = "abc42xyz789pqr123mno456def"
analyze_text_fragments(input_text)