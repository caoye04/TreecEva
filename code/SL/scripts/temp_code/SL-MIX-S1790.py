from collections import defaultdict

def rotate_left(value, bits, width=16):
    bits %= width
    return ((value << bits) | (value >> (width - bits))) & ((1 << width) - 1)

def process_encryption_sequence(input_val):
    # Transformation map (simulating a 4-bit S-box)
    transform_map = {
        0x0: 0xE, 0x1: 0x4, 0x2: 0xD, 0x3: 0x1,
        0x4: 0x2, 0x5: 0xF, 0x6: 0xB, 0x7: 0x8,
        0x8: 0x3, 0x9: 0xA, 0xA: 0x6, 0xB: 0xC,
        0xC: 0x5, 0xD: 0x9, 0xE: 0x0, 0xF: 0x7
    }
    
    # Dynamic mask for XOR operation
    dynamic_mask = 0x1F3C
    
    # Step 1: XOR with dynamic mask
    xor_result = input_val ^ dynamic_mask
    
    # Step 2: Left rotate by 3 bits
    rotated_val = rotate_left(xor_result, 3)
    
    # Step 3: Process each 4-bit chunk through transform_map
    encrypted_output = 0
    for i in range(4):
        chunk = (rotated_val >> (i * 4)) & 0xF
        if chunk in transform_map:
            transformed_chunk = transform_map[chunk]
            encrypted_output |= (transformed_chunk << (i * 4))
        else:
            encrypted_output |= (chunk << (i * 4))
    
    return encrypted_output

# Initial 16-bit input in hexadecimal
initial_input = 0xB4A3

# Process the encryption sequence
encrypted_output = process_encryption_sequence(initial_input)
print(f"Result: {encrypted_output}")