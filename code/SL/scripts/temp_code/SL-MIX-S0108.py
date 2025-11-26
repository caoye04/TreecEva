def compute_checksum(data_values, mask_pattern):
    # Distractor: unused bit manipulation
    bit_shift_temp = (mask_pattern << 3) & 0xFF
    redundant_xor = bit_shift_temp ^ 0xAA
    
    # Relevant processing with list comprehension
    filtered_data = [x for x in data_values if x % 2 == 0]
    
    # Misleading intermediate calculation
    fake_sum = sum(data_values) * 2
    unused_remainder = fake_sum % 7
    
    # Actual checksum logic
    checksum = 0
    for i, value in enumerate(filtered_data):
        if mask_pattern & (1 << (i % 8)):
            checksum ^= (value + i)
        else:
            checksum |= (value - i)
    
    # Dead code path that looks relevant
    if len(filtered_data) > 10:
        checksum += 1000
    else:
        checksum -= 50  # This path is never taken
    
    # Redundant string operations (unused)
    temp_str = ''.join(chr(65 + x % 26) for x in data_values[:3])
    
    return checksum

def validate_data_structure(input_list):
    # Distractor function that appears useful
    sorted_copy = sorted(input_list)
    median = sorted_copy[len(sorted_copy) // 2]
    mean = sum(input_list) / len(input_list)
    return abs(median - mean)  # Unused return value

# Main execution
primary_data = [15, 8, 23, 42, 7, 56, 31, 18, 9, 64]
secondary_mask = 0b11010101

# Distractor calculations
unrelated_total = sum(primary_data) * 3 - 100
redundant_list = [x * 2 for x in primary_data if x > 20]

# Key function call
final_output = compute_checksum(primary_data, secondary_mask)

# Print the target variable
print(f"Result: {final_output}")