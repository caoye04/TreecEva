from functools import reduce
import itertools

def custom_checksum(data_sequence):
    processed_values = []
    for idx, val in enumerate(data_sequence):
        if idx % 3 == 0:
            transformed = (val ^ 0xF0) & 0xFF
        elif idx % 3 == 1:
            transformed = (val << 2) & 0xFF
        else:
            transformed = (val >> 1) & 0x7F
        processed_values.append(transformed)
    
    # Apply modular sum with alternating sign
    checksum = 0
    for i, v in enumerate(processed_values):
        if i % 2 == 0:
            checksum = (checksum + v) % 256
        else:
            checksum = (checksum - v) % 256
    
    return checksum

data_packets = [0x12, 0x34, 0x56, 0x78, 0x9A, 0xBC]
intermediate_result = custom_checksum(data_packets)

# Generate all 3-element combinations of processed data
processed_for_combinations = [(x ^ 0xAA) & 0xFF for x in data_packets]
combinations_list = list(itertools.combinations(processed_for_combinations, 3))

# Calculate XOR of each combination's elements
combination_xor_results = list(map(lambda combo: reduce(lambda a, b: a ^ b, combo), combinations_list))

# Filter results greater than 0x80 and compute their product modulo 179
filtered_results = list(filter(lambda x: x > 0x80, combination_xor_results))
product_mod = 1
for num in filtered_results:
    product_mod = (product_mod * num) % 179

# Final verification flag combines checksum and combinatorial product
verification_flag = ((intermediate_result & 0xFF) | (product_mod << 2)) % 251
print(f"Result: {verification_flag}")