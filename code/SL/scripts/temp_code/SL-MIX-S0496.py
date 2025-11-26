import itertools

def process_sequence(entries):
    # Irrelevant processing for distraction
    temp_values = [e * 2 + 5 for e in entries]
    misleading_sum = sum(temp_values)
    
    # Actual relevant computation
    filtered_data = [e for e in entries if e > 15]
    if not filtered_data:
        return -999  # Dead code path - never reached
    
    # Distractor operations
    redundant_calc = misleading_sum // len(entries)
    unused_var = redundant_calc * 3 - 10
    
    # Core logic
    permutations = list(itertools.permutations(filtered_data, 2))
    valid_pairs = [(x, y) for x, y in permutations if x % 2 == 0 and y % 3 == 0]
    
    # More distractions
    fake_max = max(temp_values) if temp_values else 0
    intermediate_distraction = fake_max - misleading_sum
    
    if valid_pairs:
        result_pairs = [x * y for x, y in valid_pairs]
        final_value = sum(result_pairs) // len(result_pairs)
    else:
        final_value = 0
    
    return final_value

# Main execution with distractions
data_entries = [18, 12, 24, 9, 30, 6, 21]

# Irrelevant variable manipulations
distractor_list = [n + 100 for n in data_entries]
meaningless_total = sum(distractor_list)
unused_counter = len([x for x in distractor_list if x > 115])

# Actual call
final_result = process_sequence(data_entries)

# Print final answer
print(f"Result: {final_result}")