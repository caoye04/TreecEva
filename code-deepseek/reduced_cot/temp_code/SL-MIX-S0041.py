import itertools

def calculate_weighted_sum(values, weights):
    # Irrelevant helper function - never called
    return sum(v * w for v, w in zip(values, weights))

def filter_and_transform(data_sequence):
    # Distractor variable that looks important but isn't
    processing_factor = 2.5
    misleading_temp = [x * processing_factor for x in data_sequence if x % 3 == 0]
    
    # Actual processing logic
    filtered_data = [x for x in data_sequence if x > 10 and x % 2 != 0]
    
    # Dead code path that looks relevant
    unused_calculation = sum(x ** 2 for x in data_sequence) // len(data_sequence)
    
    # Key transformation using itertools
    grouped_data = itertools.groupby(sorted(filtered_data), key=lambda x: x % 5)
    transformed = []
    for key, group in grouped_data:
        group_list = list(group)
        # Misleading intermediate operation
        fake_avg = sum(group_list) / len(group_list) if group_list else 0
        # Actual transformation - bitwise operation
        transformed.append(sum(group_list) ^ (key * 7))
    
    return transformed

def compute_final_result(processed_values):
    # More distractions
    temp_buffer = [x * 0.8 for x in processed_values]
    irrelevant_counter = len([x for x in processed_values if x < 50])
    
    # Core computation with multiple steps
    step1 = sum(processed_values)
    step2 = step1 & 0xFF  # Bitwise AND
    step3 = step2 * 3 - 17
    
    # Final adjustment
    final_value = step3 // 2 + (step2 % 11)
    return final_value

# Main execution
raw_data = [8, 15, 23, 12, 31, 19, 27, 14, 33, 21]

# Misleading variable that seems important
preliminary_analysis = [x + 5 for x in raw_data if x < 20]

# Key function call
processed_data = filter_and_transform(raw_data)

# More irrelevant computations
secondary_calc = sum(x ** 0.5 for x in raw_data) * 2
misleading_flag = len([x for x in processed_data if x > 30])

# Final computation
final_score = compute_final_result(processed_data)

# Dead code that looks relevant but never affects result
if misleading_flag > 2:
    potential_adjustment = final_score + 10
else:
    potential_adjustment = final_score - 5

print(f"Result: {final_score}")