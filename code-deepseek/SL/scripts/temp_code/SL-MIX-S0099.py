import itertools

def analyze_data_sequences(data_points):
    # Distractor operations that don't affect final result
    temp_buffer = sum([x * 2 for x in data_points if x % 3 == 0])
    sequence_analysis = len([pair for pair in itertools.combinations(data_points, 2) if sum(pair) > 15])
    
    # Relevant computation chain
    filtered_data = [x for x in data_points if x % 2 == 0]
    base_sum = sum(filtered_data)
    
    # Intermediate step that's not directly used
    processed_sum = base_sum // 2 + 5
    
    # More distractor calculations
    alternative_metric = max(data_points) - min(data_points)
    
    # Key computation path
    adjustment_factor = len(filtered_data) * 2
    offset_value = processed_sum % 7
    
    # Final result calculation
    final_processing_result = processed_sum * adjustment_factor - offset_value
    
    print(f"Result: {final_processing_result}")
    return final_processing_result

# Main execution
sample_data = [4, 7, 12, 3, 8, 15, 6, 9]
analyze_data_sequences(sample_data)