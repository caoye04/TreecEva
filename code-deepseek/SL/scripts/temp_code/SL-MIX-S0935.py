import itertools

def compute_checksum(items):
    # Distractor function - never actually called in main flow
    temp_sum = sum(x ** 2 for x in items if x % 3 == 0)
    checksum = temp_sum & 0xFF
    return checksum + len(items)

def transform_data(values):
    # Misleading transformation that looks relevant
    transformed = [v * 2 + 7 for v in values]
    filtered = list(filter(lambda x: x > 15, transformed))
    return sum(filtered) - len(filtered) * 3

def process_results(sequence):
    # Main logic with multiple red herrings
    counter = 0
    running_total = 0
    
    # Irrelevant string operations that don't affect final result
    test_string = "debug_info_123"
    string_length = len(test_string.replace("_", "X"))
    
    # Dead code path
    if string_length > 20:
        dummy_var = string_length * 2
    else:
        dummy_var = string_length // 2
    
    # Actual relevant computation
    for i, val in enumerate(sequence):
        if i % 2 == 0:
            running_total += val * 3
            counter += val % 7
        else:
            running_total -= val
            counter -= (val // 2) % 5
    
    # More distractor operations
    unused_list = [x for x in range(10, 20)]
    unused_sum = sum(unused_list) + transform_data([1, 2, 3])
    
    # Final combination with irrelevant elements
    intermediate = running_total * 2 - counter
    final_value = intermediate // 4 + (string_length % 3)
    
    return final_value

# Main execution
initial_data = [8, 12, 5, 19, 3, 14, 7]
backup_data = [x + 2 for x in initial_data]  # Unused backup

# Red herring - never used
validation_hash = hash(tuple(initial_data)) % 1000

# Critical execution point
final_tally = process_results(initial_data)

# Print result
print(f"Target result: {final_tally}")