import itertools

# Irrelevant helper function (decoy)
def dummy_transform(x):
    return (x * 37 + 123) % 10007

def compute_checksum(sequence):
    # Real but misleading intermediate computation
    checksum = 0
    for i, val in enumerate(sequence):
        checksum += val * (i + 1)
    return checksum % 97

def bitwise_scramble(n):
    # Distractor operation with no real impact
    n = ((n << 3) & 0xFF) | ((n >> 5) & 0xFF)
    n ^= 0b10101010
    return n

def generate_sequence(seed, length):
    # Generates a sequence using recursion and bit manipulation
    if length == 0:
        return []
    if length == 1:
        return [seed]
    prev = generate_sequence(seed, length - 1)
    next_val = (prev[-1] + seed // 2) ^ (seed & 7)
    return prev + [next_val]

def filter_relevant_data(stream, threshold=150):
    # Uses itertools to group data, but only one branch matters
    filtered = []
    for key, group in itertools.groupby(stream, lambda x: x > threshold):
        if key:  # Only this block matters
            filtered.extend(list(group)[:3])  # Take first 3 above threshold
    return filtered

def decode_payload(units):
    # Core transformation logic buried among distractions
    adjusted = [u - 100 for u in units if u > 100]
    base = sum(adjusted)
    multiplier = len(adjusted) or 1
    temp_result = base * multiplier

    # Red herring: complex-looking but unused calculation
    decoy_accum = 0
    for i in range(len(adjusted)):
        decoy_accum += adjusted[i] * (i + 1) ** 2
        decoy_accum %= 100000

    return temp_result  # This is actually used later

def process_pipeline(data_stream):
    # Step 1: Generate side data (distractor)
    noise_sequence = generate_sequence(13, 10)
    fake_checksum = compute_checksum(noise_sequence)

    # Step 2: Filter real data
    important_units = filter_relevant_data(data_stream, threshold=150)

    # Step 3: Decode payload (core logic)
    decoded_value = decode_payload(important_units)

    # Step 4: Apply scrambling (irrelevant for final result)
    scrambled = bitwise_scramble(decoded_value % 1000)

    # Step 5: Final adjustment (only part that uses decoded_value)
    scaling_factor = 7
    offset = 42
    final_output = decoded_value * scaling_factor - offset

    # Dead code path - never reached
    if final_output < 0:
        final_output = dummy_transform(final_output)

    return final_output

# Main execution
if __name__ == '__main__':
    # Input data stream
    raw_input = [88, 95, 102, 167, 173, 151, 200, 77, 130, 158, 144]
    
    # Decoy operations
    _ = [bitwise_scramble(x) for x in raw_input[::2]]
    _ = compute_checksum(raw_input)
    
    # Key execution point
    final_output = process_pipeline(raw_input)
    
    # Output result
    print(f"Result: {final_output}")