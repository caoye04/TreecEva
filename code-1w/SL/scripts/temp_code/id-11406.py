import math

# Irrelevant helper function (decoy)
def useless_transform(x):
    return [val ** 2 + 3 for val in x if val % 2 == 0]

# Another decoy function with misleading intermediate computation
def compute_checksum(data):
    checksum = 0
    for i, val in enumerate(data):
        checksum += val * (i + 1) ^ 7
    return checksum % 1000  # Dead-end result

# Real transformation: applies bit manipulation and filtering
def preprocess_sequence(seq):
    filtered = [x for x in seq if x > 0 and (x & (x - 1)) == 0]  # Keep powers of two
    rotated = filtered[2:] + filtered[:2]  # Slice rotation
    return [rotated[i] ^ i for i in range(len(rotated))]  # XOR with index

# Secondary transform: applies combinatorial scaling
def generate_pairs(values):
    pairs = []
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            pairs.append((values[i], values[j]))
    return pairs  # Not used directly but distracts

# Entropy calculation based on frequency distribution
def calculate_entropy(data):
    if not data:
        return 0.0
    freq_map = {}
    total = 0
    for val in data:
        freq_map[val] = freq_map.get(val, 0) + 1
        total += 1
    
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

# Main execution flow
initial_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 16]

# Distractor: multiple unused transformations
shadow_copy = initial_data[::-1]  # Reversed, unused
scaled_data = [x * 3 - 1 for x in initial_data if x % 3 != 0]
dummy_checksum = compute_checksum(scaled_data)

# Real processing path begins
filtered_power_of_two = [x for x in initial_data if x > 0 and (x & (x - 1)) == 0]
shifted_slice = filtered_power_of_two[1:] + [filtered_power_of_two[0]]  # Rotate left by 1
processed_shift = [v ^ 5 for v in shifted_slice]  # Bitwise obfuscation

expanded_data = []
for val in processed_shift:
    expanded_data.extend([val, val + 1])  # Duplicate pattern

trimmed_data = expanded_data[1:-1]  # Remove first and last

# Apply actual key transformation
transformed_data = preprocess_sequence(trimmed_data)

# Introduce another red herring: string-based distraction
temp_string = ''.join([chr(97 + (x % 26)) for x in trimmed_data[:10]])
anagram_list = [temp_string[i:] + temp_string[:i] for i in range(len(temp_string))]

# Final and correct entropy computation
final_entropy = calculate_entropy(transformed_data)

print(f"Result: {final_entropy}")