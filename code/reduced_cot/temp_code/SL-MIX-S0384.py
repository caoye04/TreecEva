def filter_condition(x):
    return x % 3 != 0

def transform_op(x):
    return (x << 2) | (x & 0xF)

def process_data(values, filter_func, transform_func):
    filtered = list(filter(filter_func, values))
    transformed = list(map(transform_func, filtered))
    
    # Distractor operations with bitwise manipulation
    irrelevant_mask = 0b10101010
    misleading_result = sum(x & irrelevant_mask for x in transformed)
    
    # Dead code path that looks relevant
    if misleading_result > 1000:
        unused_value = misleading_result // 4
    else:
        unused_value = misleading_result * 3
    
    # Main computation chain
    accumulator = 0
    for val in transformed:
        accumulator ^= val
        
    # More distractions
    dummy_calc = (misleading_result + accumulator) % 17
    dummy_calc = dummy_calc << 1
    
    return accumulator

# Initial data setup
mixed_values = [12, 7, 19, 25, 8, 14, 31, 42, 55, 68]

# Distractor variables and computations
irrelevant_set = {x for x in mixed_values if x > 20}
redundant_sum = sum(irrelevant_set)

# Key execution point
target_value = process_data(mixed_values, filter_condition, transform_op)

# More misleading intermediate calculations
fake_result = (target_value + redundant_sum) // 2
misleading_var = fake_result & 0xFF

print(f"Target result: {target_value}")