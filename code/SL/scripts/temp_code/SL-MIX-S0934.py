import re

def process_packet_sequence(seq_num):
    # Initial key derivation using bit manipulation
    base_key = (seq_num & 0xFF) ^ ((seq_num >> 8) & 0xFF)
    
    # Generate rotated keys using list comprehension
    rotation_keys = [(base_key << i) & 0xFF | (base_key >> (8 - i)) for i in range(1, 5)]
    
    # Apply arithmetic transformations
    transformed_values = [((k * 17) + 42) % 256 for k in rotation_keys]
    
    # Convert to hex strings and concatenate
    hex_chain = ''.join([f'{v:02x}' for v in transformed_values])
    
    # Pattern matching to find specific sequences
    pattern_matches = len(re.findall(r'([a-f]{2})\1', hex_chain))
    
    # Final verification code calculation
    verification_code = (sum(transformed_values) ^ (pattern_matches << 4)) & 0xFF
    return verification_code

# Process packet #2023
packet_sequence_number = 2023
verification_code = process_packet_sequence(packet_sequence_number)
print(f'Result: {verification_code}')