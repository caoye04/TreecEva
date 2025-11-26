import itertools

def transform_coordinates(point_list):
    # Distractor: unused lambda function
    coord_mapper = lambda x: (x[0] ** 2, x[1] ** 3)
    
    # Irrelevant intermediate calculations
    temp_sum = sum(x[0] + x[1] for x in point_list) * 2
    avg_coord = temp_sum / (len(point_list) * 2) if point_list else 0
    
    # Actual transformation with bitwise operations
    processed = [(x[0] & 15, x[1] | 7) for x in point_list]
    
    # Misleading intermediate result
    fake_result = sum(a * b for a, b in processed) + 100
    
    # Real processing with itertools
    result = list(itertools.chain.from_iterable(processed))
    
    # Dead code path
    if fake_result > 1000:
        redundant_var = fake_result // 2
    else:
        redundant_var = fake_result * 3
    
    return result

def process_data(data_sequence):
    # More distractions
    sequence_length = len(data_sequence)
    dummy_multiplier = sequence_length * 3 - 5
    
    # Irrelevant tuple operations
    coord_pairs = [(data_sequence[i], data_sequence[i+1]) for i in range(0, len(data_sequence)-1, 2)]
    dummy_sum = sum(a + b for a, b in coord_pairs) if coord_pairs else 0
    
    # Actual core logic with conditional expressions
    filtered_data = [x for x in data_sequence if x % 2 == 0]
    
    # Multiple misleading computations
    temp_product = 1
    for num in filtered_data[:3]:
        temp_product *= (num + 1)
    
    # Final calculation with nested conditionals
    if len(filtered_data) > 2:
        result = sum(filtered_data) - (filtered_data[0] ^ filtered_data[1])
    else:
        result = sum(filtered_data) * 2 + (dummy_sum % 10)
    
    # More dead code
    unused_var = temp_product + dummy_multiplier
    
    return result

# Main execution
coords = [(12, 8), (7, 15), (10, 3), (5, 11)]

# Irrelevant variable tracking
coords_count = len(coords)
dummy_tracker = coords_count * 10 - 5

# Key execution point
final_output = process_data(transform_coordinates(coords))

# Final output
print(f"Result: {final_output}")