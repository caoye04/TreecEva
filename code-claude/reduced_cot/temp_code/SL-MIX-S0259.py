def calculate_hash(data):
    base_value = 17
    multiplier = 31
    
    # This is just for debugging purposes
    debug_values = []
    
    hash_value = 0
    for item in data:
        # Apply bitwise XOR with the ASCII value
        hash_value = (hash_value * multiplier) ^ ord(item)
        debug_values.append(hash_value)
    
    # Apply a final transformation that doesn't affect the result
    transformed = hash_value + 0
    
    # Additional operations for verification (not used in final result)
    verification_sum = sum([ord(c) for c in data])
    alternative_hash = verification_sum % 1000
    
    return hash_value

# Input data processing
raw_data = "security_hash_algorithm"
input_data = raw_data + "_v2"

# Apply some filtering
filter_chars = ['a', 'e', 'i', 'o', 'u']
decoy_data = ''.join([c for c in input_data if c not in 'xyz'])

# This is our actual filtering operation
filtered_data = ''.join([c for c in input_data if c not in filter_chars])

# Perform some analysis (not directly used in final result)
char_counts = {}
for char in filtered_data:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1

# Calculate metrics that won't be used
max_count = max(char_counts.values()) if char_counts else 0
unique_chars = len(char_counts)

# Calculate the hash value
final_hash = calculate_hash(filtered_data)

# Try an alternative approach (not used)
alternative_result = sum([ord(c) * (i+1) for i, c in enumerate(filtered_data)]) % 10000

print(f"Result: {final_hash}")