def compute_validation_score(data_stream, mask_bits):
    temp_buffer = [0] * 8
    parity_check = 0
    # Distractor: unused crypto calculation
    crypto_seed = 0x5A
    dummy_hash = crypto_seed ^ 0xFF
    
    # Relevant data processing with bitwise operations
    for i, byte_val in enumerate(data_stream):
        masked_val = byte_val & mask_bits[i % len(mask_bits)]
        temp_buffer[i % 8] ^= masked_val
        # Distractor: misleading intermediate calculation
        parity_check += (masked_val >> 2) * 3
    
    # Core computation with early return
    validation_sum = 0
    for idx, val in enumerate(temp_buffer):
        if idx % 2 == 0:
            validation_sum += (val << 1) | 0x1
        else:
            validation_sum += val ^ 0x3A
    
    # Distractor: unused alternate calculation path
    alternate_score = sum(temp_buffer) * 2 - parity_check
    
    # Final adjustment with conditional
    if validation_sum > 100:
        validation_sum = (validation_sum % 64) + 25
    else:
        validation_sum = (validation_sum | 0x10) - 8
    
    return validation_sum

# Main execution with distractor variables
encrypted_data = [0x37, 0x5A, 0x89, 0xF2, 0x1E, 0x4C, 0xB7, 0x63]
validator_mask = [0x7F, 0x3A, 0x55, 0x91]
debug_counter = 0
redundant_check = sum(encrypted_data) + len(validator_mask)

# Critical execution point
final_score = compute_validation_score(encrypted_data, validator_mask)

# Distractor: unused result processing
formatted_output = f"Debug: {final_score:04X}"
backup_score = final_score * 2 - 15

print(f"Result: {final_score}")