import itertools

def compute_parity_mask(bits):
    irrelevant_mask = 0b11011010  # Distractor variable
    temp_sum = sum((bits >> i) & 1 for i in range(8))
    return temp_sum % 2

def calculate_data_offset(values):
    offset_accumulator = 0
    for i, val in enumerate(values):
        offset_accumulator ^= (val << (i % 4))  # Misleading computation
    return offset_accumulator % 16

def process_checksum(data_sequence):
    # Main processing logic with multiple intermediate steps
    prime_filter = lambda x: x % 2 != 0 and x % 3 != 0  # Relevant lambda
    filtered_primes = list(filter(prime_filter, data_sequence))
    
    # Distractor operations
    redundant_set = set(data_sequence) | {255, 128, 64}
    unused_combo = list(itertools.combinations(redundant_set, 2))  # Unused itertools
    
    # Core computation chain
    parity_results = [compute_parity_mask(x) for x in filtered_primes]
    offset_value = calculate_data_offset(filtered_primes)
    
    # Misleading intermediate result
    misleading_sum = sum(parity_results) * 2 + offset_value
    
    # Final computation (actual answer path)
    checksum_base = sum(filtered_primes) & 0xFF
    final_checksum = (checksum_base ^ offset_value) | (misleading_sum & 0x0F)
    
    # Dead code path
    if misleading_sum > 100:
        dead_result = final_checksum + 50  # Never executed
    else:
        dead_result = final_checksum - 25  # Never executed
    
    return final_checksum

# Main execution
initial_data = [17, 23, 29, 31, 37, 41, 43, 47, 53]
additional_data = [61, 67, 71]  # Distractor data
combined_stream = initial_data + additional_data

# Multiple irrelevant variables
temp_buffer = [x * 2 for x in combined_stream]
unused_counter = len([x for x in temp_buffer if x > 80])

final_result = process_checksum(initial_data)
print(f"Result: {final_result}")