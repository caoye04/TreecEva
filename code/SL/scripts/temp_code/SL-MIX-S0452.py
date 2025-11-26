from collections import Counter

def calculate_weights(data_stream):
    # Primary data processing with bitwise operations
    base_mask = 0xFF
    shift_count = 2
    
    # Main computation - transform data using modular arithmetic
    transformed = [(x << shift_count) & base_mask for x in data_stream]
    
    # Distractor: unused computation that looks important
    inverse_weights = [~x & base_mask for x in data_stream]
    
    # Actual weight calculation
    weight_vector = [t % 17 for t in transformed]
    return weight_vector

def validate_pattern(pattern_data):
    # Misleading validation that appears crucial but isn't
    temp_sum = sum(pattern_data)
    validation_flag = (temp_sum & 0x0F) == 7
    
    # Dead code path that never executes
    if validation_flag and len(pattern_data) > 10:
        redundancy_check = pattern_data[-1] * 3
    else:
        redundancy_check = 0
    
    # Counter-based frequency analysis (relevant)
    freq_counter = Counter(pattern_data)
    dominant_value = freq_counter.most_common(1)[0][0] if freq_counter else 0
    return dominant_value

# Main execution with multiple data streams
primary_data = [12, 45, 78, 23, 56, 89, 34, 67]
secondary_data = [8, 29, 51, 74, 16, 39, 62, 95]

# Compute checksums with various operations
checksum_a = sum(calculate_weights(primary_data))
checksum_b = validate_pattern(secondary_data)

# Misleading intermediate calculation
auxiliary_mod = (checksum_a * 3 + checksum_b) % 256

# Critical execution point
verification_mod = 97
final_checksum = (checksum_a ^ checksum_b) % verification_mod

# Print target result
print(f"Target result: {final_checksum}")