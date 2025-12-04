from collections import Counter

def decode_sequence(sequence, mask):
    # Irrelevant initialization - never used
    temp_buffer = [i * 2 for i in range(20)]
    offset_calc = sum(x & 0xF for x in temp_buffer)
    
    # Actual decoding logic
    decoded = []
    for i, val in enumerate(sequence):
        if i % 2 == 0:
            masked_val = (val ^ mask[0]) & 0xFF
        else:
            masked_val = (val | mask[1]) & 0xFF
        decoded.append(masked_val)
    
    # Misleading intermediate calculation
    fake_sum = sum(decoded) * 3 - 150
    
    # Actual checksum calculation
    freq = Counter(decoded)
    cipher_checksum = sum(k * v for k, v in freq.items()) % 256
    
    # Dead code path
    if fake_sum > 1000:
        cipher_checksum = fake_sum % 100
    
    return cipher_checksum

# Main execution
mask_pattern = (0x5A, 0x3C)
data_stream = [120, 45, 200, 89, 156, 33, 178, 67]

# Distractor computations
redundant_calc = (data_stream[0] << 2) | (data_stream[1] >> 1)
placeholder_var = [x + 10 for x in data_stream if x > 100]

result = decode_sequence(data_stream, mask_pattern)
print(f"Result: {result}")