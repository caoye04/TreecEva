def process_data(stream, depth):
    temp_filter = lambda x: x % 2 == 0
    redundant_calc = lambda y: y * 2 - 1
    
    filtered_stream = list(filter(temp_filter, stream))
    processed_values = []
    
    for i in range(len(filtered_stream)):
        current = filtered_stream[i]
        # Distractor: this calculation is not used in final result
        unused_transform = redundant_calc(current) + depth
        
        if i % 2 == 0:
            processed_values.append(current * 3)
        else:
            processed_values.append(current + 7)
    
    # Another distractor: intermediate calculation
    intermediate_sum = sum(processed_values[:2]) if len(processed_values) >= 2 else 0
    
    final_output = sum(processed_values) ^ 15
    
    # Final verification step (distractor)
    verification = final_output & 255
    
    print(f"Result: {final_output}")
    return final_output

data_stream = [8, 3, 12, 5, 7, 18, 2, 9]
final_output = process_data(data_stream, 3)