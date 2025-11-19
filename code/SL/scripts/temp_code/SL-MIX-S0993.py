import re

def decode_hex_sequence(hex_string):
    # Convert hex string to bytes then to integer
    return int.from_bytes(bytes.fromhex(hex_string), 'big')

def apply_bitwise_mask(value, mask_pattern):
    # Apply XOR mask followed by AND operation
    masked = value ^ mask_pattern
    return masked & 0xFF

def transform_with_modular_arithmetic(value, modulus_base):
    # Apply modular exponentiation
    return pow(value, 3, modulus_base)

def extract_numeric_patterns(text_input):
    # Extract all numeric sequences and sum them
    patterns = re.findall(r'\d+', text_input)
    return sum(int(p) for p in patterns)

# Main cipher processing pipeline
hex_encoded_data = "4a6f686e446f65"
bitwise_key = 0b10110101
modulus_parameter = 251
text_metadata = "Version_2023_Release_45_Build_12"

# Step 1: Decode hexadecimal data
raw_data = decode_hex_sequence(hex_encoded_data)

# Step 2: Extract numeric metadata
metadata_sum = extract_numeric_patterns(text_metadata)

# Step 3: Process each byte through bitwise transformation
byte_values = [raw_data >> i*8 & 0xFF for i in range(len(hex_encoded_data)//2)]
transformed_bytes = [apply_bitwise_mask(b, bitwise_key) for b in byte_values]

# Step 4: Apply modular arithmetic to transformed values
modular_results = [transform_with_modular_arithmetic(tb, modulus_parameter) for tb in transformed_bytes]

# Step 5: Combine with metadata using set operations
total_unique_values = len(set(modular_results + [metadata_sum % modulus_parameter]))

# Step 6: Final cipher computation using generator expression and bitwise shifts
cipher_output = sum((val << (i % 4)) for i, val in enumerate(modular_results)) % modulus_parameter
cipher_output ^= total_unique_values

print(f"Result: {cipher_output}")