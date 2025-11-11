from functools import reduce

def transform_identifier(traffic_id):
    # Convert hex to integer
    numeric_id = int(traffic_id, 16)
    
    # Apply bitwise transformations
    step1 = numeric_id ^ 0xFFFF  # XOR with mask
    step2 = (step1 >> 4) & 0x0FFF  # Right shift and mask
    
    # Create mapping dictionaries
    hex_mapping = {hex(i)[-1]: i for i in range(16)}
    transformed_mapping = {k: v*3 + 7 for k, v in hex_mapping.items()}
    merged_dict = {**hex_mapping, **transformed_mapping}
    
    # Apply logical conditions
    condition_a = (step2 & 0x0F00) != 0
    condition_b = (step2 & 0x00F0) > 0x10
    condition_c = not (step2 & 0x000F == 0)
    
    # Functional transformation
    hex_chars = [c for c in hex(step2)[2:].upper()]
    mapped_values = list(map(lambda x: merged_dict.get(x, 0), hex_chars))
    filtered_values = list(filter(lambda x: x > 10, mapped_values))
    
    # Calculate security score
    base_score = reduce(lambda x, y: x + y, filtered_values, 0) if filtered_values else 0
    
    # Apply final logical combination
    if condition_a and (condition_b or condition_c):
        final_security_score = base_score * 2 + 0x100
    else:
        final_security_score = base_score // 2 - 0x50
    
    return final_security_score

# Process the network traffic
network_identifier = '0x3A7F'
final_security_score = transform_identifier(network_identifier)
print(f"Result: {final_security_score}")