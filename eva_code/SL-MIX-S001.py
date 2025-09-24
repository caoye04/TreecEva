import hashlib
import itertools
from functools import reduce

# Constants and initial data structures
BASE_MULTIPLIER = 17
MOD_VALUE = 1000007
SECRET_KEY = 0xABCDEF
data_matrix = [
    [3, 7, 11, 15],
    [19, 23, 27, 31], 
    [35, 39, 43, 47],
    [51, 55, 59, 63]
]
weight_vector = [0.25, 0.35, 0.15, 0.25]
configuration = {
    'active': True,
    'threshold': 42.5,
    'iterations': 8,
    'precision': 3
}

# String processing and hash calculations
input_string = "DataProcessing2024"
hash_object = hashlib.md5(input_string.encode())
hex_hash = hash_object.hexdigest()
hash_numeric = int(hex_hash[:8], 16)
reduced_hash = hash_numeric % 10000

# Matrix operations with conditional logic
flattened_data = [item for row in data_matrix for item in row]
filtered_data = [x for x in flattened_data if x % 4 == 3]
sorted_filtered = sorted(filtered_data, reverse=True)

# Weighted calculations
weighted_sum = sum(w * sorted_filtered[i] for i, w in enumerate(weight_vector) if i < len(sorted_filtered))
normalized_weight = weighted_sum / sum(weight_vector)

# Bitwise operations sequence
bit_pattern = SECRET_KEY
for i in range(4):
    bit_pattern ^= (sorted_filtered[i] << (i * 2))
    bit_pattern &= 0xFFFFFF
    bit_pattern |= (1 << (7 + i))

# Recursive-style calculation using reduce
recursive_product = reduce(lambda x, y: (x * y) % MOD_VALUE, sorted_filtered[:4], 1)
power_result = pow(recursive_product, 3, MOD_VALUE)

# String manipulation and encoding
reversed_string = input_string[::-1]
char_codes = [ord(c) for c in reversed_string[:8]]
char_sum = sum(char_codes)
encoded_value = char_sum ^ reduced_hash

# Complex conditional assignments
is_threshold_met = normalized_weight > configuration['threshold']
is_pattern_valid = (bit_pattern & 0xFF) > 128
is_power_significant = power_result > 50000

# Multi-level calculations
if is_threshold_met and is_pattern_valid:
    level_1 = encoded_value * BASE_MULTIPLIER
elif is_power_significant:
    level_1 = encoded_value + power_result
else:
    level_1 = encoded_value // 2

# Nested list comprehension with filtering
nested_result = [
    sum(row[i] * weight_vector[i] for i in range(len(row)))
    for row in data_matrix
    if sum(row) % 3 == 0
]

# Itertools operations
combination_sum = sum(
    reduce(lambda x, y: x + y, combo)
    for combo in itertools.combinations(sorted_filtered, 2)
    if sum(combo) % 7 == 0
)

# Final aggregation with modular arithmetic
temp_result = (
    level_1 +
    (bit_pattern % 1000) +
    (power_result % 500) +
    len(nested_result) * 100 +
    (combination_sum % 200) +
    configuration['iterations'] * 15
)

# Ultimate calculation with multiple transformations
target_result = (
    (temp_result * 3) % 8192 +
    (reduced_hash % 256) +
    (len(char_codes) * 7) +
    (1 if all([is_threshold_met, is_pattern_valid, is_power_significant]) else 0)
) % 10000

print(f"Target result: {target_result}")