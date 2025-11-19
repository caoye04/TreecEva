import itertools
import re

def process_packet_headers():
    # Initial packet header values
    headers = [0x1A, 0x2B, 0x3C, 0x4D, 0x5E]
    
    # Bitwise transformation matrix
    transform_matrix = [
        [0x0F, 0xF0, 0xFF],
        [0xAA, 0x55, 0xCC],
        [0x33, 0xCC, 0xAA]
    ]
    
    # Apply XOR transformations with bit shifts
    transformed = []
    for i, header in enumerate(headers):
        row = i % len(transform_matrix)
        xor_result = header
        for j, mask in enumerate(transform_matrix[row]):
            if j % 2 == 0:
                xor_result ^= (mask << (j+1))
            else:
                xor_result ^= (mask >> (j-1))
        transformed.append(xor_result)
    
    # Pattern matching to filter values
    filtered_values = []
    for val in transformed:
        binary_str = bin(val)[2:].zfill(16)
        # Match pattern: at least 3 consecutive 1s
        if re.search(r'1{3,}', binary_str):
            filtered_values.append(val)
    
    # Combinatorial aggregation
    encoded_checksum = 0
    for combo in itertools.combinations(filtered_values, 2):
        pair_xor = combo[0] ^ combo[1]
        encoded_checksum = (encoded_checksum & pair_xor) | ((encoded_checksum | pair_xor) >> 2)
    
    return encoded_checksum

# Execute the security protocol
encoded_checksum = process_packet_headers()
print(f"Result: {encoded_checksum}")