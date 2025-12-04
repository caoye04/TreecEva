def transform_data(input_str):
    return sum(ord(c) for c in input_str if c.isalpha())

def xor_operation(a, b):
    return a ^ b

def process_crypto_blocks(data_sequence):
    # Irrelevant preprocessing step
    temp_buffer = [x * 2 for x in range(len(data_sequence))]
    
    # Main processing with bitwise operations
    accumulator = 0
    for i, val in enumerate(data_sequence):
        if i % 2 == 0:
            accumulator = xor_operation(accumulator, val)
        else:
            accumulator = accumulator | (val << 2)
    
    # Misleading intermediate calculation
    dummy_checksum = sum(data_sequence) % 256
    
    # Dead code path - never executed
    if dummy_checksum > 1000:
        backup_hash = dummy_checksum * 3
    
    return accumulator

# Main execution
input_string = "CryptoChain2024"

# Distractor computations
string_length = len(input_string)
vowel_count = len([c for c in input_string.lower() if c in 'aeiou'])
consonant_ratio = vowel_count / string_length

# Irrelevant set operations
character_set = set(input_string)
unique_chars = len(character_set)

# Main data processing
numeric_data = [transform_data(input_string[i:i+3]) if i+3 <= len(input_string) else 0 
                for i in range(0, len(input_string), 2)]

# Misleading variable assignments
intermediate_result = sum(numeric_data) % 128
dummy_accumulator = intermediate_result * 3 + 17

encrypted_data = [x ^ 0xAB for x in numeric_data]

# Critical execution point
final_processing = process_crypto_blocks(encrypted_data)

# Final answer variable
crypto_hash = final_processing & 0xFFF

print(f"Target result: {crypto_hash}")