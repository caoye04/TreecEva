def calculate_quality_scores(data_points):
    base_scores = [85, 92, 78, 96, 88, 74, 91, 83]
    irrelevant_metric = sum(data_points) * 2.5  # Misleading calculation
    adjustment_factor = len(base_scores) // 2
    
    # Distractor operations
    temp_array = base_scores[:4] + base_scores[-2:]
    dead_code_value = temp_array[1] * temp_array[3]  # Never used
    
    quality_sum = 0
    for i, score in enumerate(base_scores):
        if i % 2 == 0:
            quality_sum += score * (i + 1)
        else:
            quality_sum += score // 2
    
    return quality_sum

def compute_final_result(input_data):
    # Multiple irrelevant variables and misleading calculations
    initial_value = 42
    offset_correction = 17
    bogus_calculation = (initial_value * offset_correction) % 23
    
    # Slicing operations (as required)
    data_slice = input_data[2:6]
    reversed_segment = data_slice[::-1]
    
    # Core logic with distractor
    if len(reversed_segment) > 2:
        core_component = sum(reversed_segment) - min(reversed_segment)
    else:
        core_component = 0  # Dead code path
    
    # More distractions
    unused_intermediate = core_component * 3.14159
    red_herring = [x + 10 for x in input_data]
    
    quality_result = calculate_quality_scores(input_data)
    final_value = (quality_result + core_component) // len(input_data)
    
    # Final distraction that looks important but isn't
    if final_value > 100:
        final_adjustment = final_value - 50  # Never executed
    
    return final_value

# Main execution
performance_data = [15, 28, 42, 56, 31, 49, 23, 67, 38, 52]
final_score = compute_final_result(performance_data)
print(f"Result: {final_score}")