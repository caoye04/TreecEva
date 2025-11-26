def compute_checksum(data, mask):
    # Initialize tracking variables
    temp_sum = 0
    irrelevant_counter = 42
    misleading_buffer = []
    
    # Process data with mask using enumerate
    for idx, (d_val, m_val) in enumerate(zip(data, mask)):
        # Conditional expression for processing
        processed = (d_val & m_val) if idx % 2 == 0 else (d_val | m_val)
        temp_sum += processed
        
        # Distractor operations
        misleading_buffer.append(processed * 2)  # Never used
        irrelevant_counter = (irrelevant_counter ^ processed) - 5
        
        # Dead code path
        if idx > len(data) * 2:
            temp_sum = temp_sum * 3  # Never reached
    
    # More distraction
    fake_validation = temp_sum % 1000
    decoy_set = {x for x in misleading_buffer if x > 50}
    
    # Final computation with slicing
    data_slice = data[2:5]
    mask_slice = mask[-3:]
    
    core_result = sum(x ^ y for x, y in zip(data_slice, mask_slice))
    final_checksum = (temp_sum + core_result) % 256
    
    # Return statement with final computation
    return final_checksum

# Main execution
mask_sequence = (0x0F, 0x3C, 0x55, 0xAA, 0xF0, 0xFF)
data_stream = [0x12, 0x34, 0x56, 0x78, 0x9A, 0xBC]

# Irrelevant intermediate computations
dummy_calc = sum(data_stream) * 2
decoy_tuple = tuple(x & 0x0F for x in data_stream)

# Key execution
final_result = compute_checksum(data_stream, mask_sequence)

print(f"Result: {final_result}")