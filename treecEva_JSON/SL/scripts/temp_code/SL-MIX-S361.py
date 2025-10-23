from collections import defaultdict

def process_packet_headers(headers):
    # Initialize verification accumulator
    verification_code = 0
    
    # Process each header component with bitwise transformations
    for i, header_val in enumerate(headers):
        # Apply XOR with position-based mask
        masked_val = header_val ^ (i + 1)
        
        # Rotate left by 3 bits (assuming 32-bit integers)
        rotated_val = ((masked_val << 3) | (masked_val >> 29)) & 0xFFFFFFFF
        
        # Combine with verification code using OR
        verification_code |= rotated_val
    
    return verification_code

def calculate_security_hash(base_value, modifier_sequence):
    # Apply floating point transformations
    transformed = float(base_value)
    for mod in modifier_sequence:
        if mod > 0:
            transformed = transformed * 1.7 + mod
        else:
            transformed = transformed / 2.3 + mod
    
    # Convert back to integer with truncation
    return int(transformed)

# Packet header data
packet_headers = [0x1A2B3C4D, 0x5E6F7890, 0xABCD1234]

# Security modifier sequence
modifiers = [-3.5, 7.2, -1.8, 4.6]

# Step 1: Process headers through bitwise pipeline
processed_headers_checksum = process_packet_headers(packet_headers)

# Step 2: Calculate base security hash
base_security_hash = calculate_security_hash(12345, modifiers)

# Step 3: Combine results with additional transformations
combined_result = (processed_headers_checksum & 0xFFFF) << 16
combined_result |= (base_security_hash & 0xFFFF)

# Step 4: Final verification using XOR and ternary logic
final_verification = combined_result ^ 0xDEADBEEF
final_verification = final_verification if final_verification > 0 else (final_verification * -1) & 0xFFFFFFFF

# The target variable whose value we need
security_verification_code = final_verification

print(f"Result: {security_verification_code}")