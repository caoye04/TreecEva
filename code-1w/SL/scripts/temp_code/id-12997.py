def process_data(data_chunk, key):
    # Irrelevant transformation (distractor)
    shadow_map = list(map(lambda x: (x * 2) ^ 3, data_chunk))
    
    # Semi-relevant pre-processing
    filtered = [x for x in data_chunk if x & key > 0]
    
    # Dummy accumulator with misleading purpose
    temp_accum = sum([x ** 0.5 for x in shadow_map if x % 2 == 0])

    # Core logic hidden among distractions
    base_shift = 0
    for val in filtered:
        if val % 2 == 1:
            base_shift ^= val
        else:
            base_shift += val >> 1

    # Secondary distractor: complex but unused calculation
    checksum = 0
    for i in range(len(data_chunk)):
        checksum = (checksum + data_chunk[i] * (i + 1)) % 97
    alt_stream = tuple((x | key) - 1 for x in data_chunk)
    
    # Actual result derivation using mixed operations
    weighted = sum(val * (index + 1) for index, val in enumerate(filtered))
    final_shift = base_shift + (weighted % 100)
    
    # Key computation involving lambda and tuple destructuring
    transform = lambda a, b: (a + b) * 2
    a, b = (final_shift, len(filtered))
    final_output = transform(a, b)
    
    # Print required at end
    return final_output

# Setup inputs
stream_buffer = [12, 7, 3, 18, 5]
activation_key = 7
intermediate_flag = False
buffer_size = len(stream_buffer) * 2 + 5  # Red herring

# Unused helper to increase cognitive load
def validate_integrity(buf):
    return all(x > 0 for x in buf)

# Execution point of interest
final_output = process_data(stream_buffer, activation_key)
print(f"Result: {final_output}")