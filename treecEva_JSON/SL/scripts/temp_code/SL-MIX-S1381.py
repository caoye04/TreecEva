import itertools
import math

def modular_power(base, exponent, modulus):
    return pow(base, exponent, modulus)

def calculate_log_sum(numbers):
    return sum(math.log(n) for n in numbers if n > 0)

# Base cryptographic components
base_key = [2, 3, 5]
cipher_modulus = 97
validation_set = {12, 24, 36, 48}

# Generate all permutations of length 2 from base key
permutations = list(itertools.permutations(base_key, 2))

# Calculate exponential values for each permutation
exp_results = []
for p in permutations:
    exp_results.append(modular_power(p[0], p[1], cipher_modulus))

# Create a dictionary mapping permutation to its exponential result
perm_exp_map = dict(zip(permutations, exp_results))

# Apply logarithmic transformation to exponential results
log_transformed = [calculate_log_sum([r]) for r in exp_results]

# Find intersection of log transformed values (rounded) with validation set
rounded_logs = {int(l) for l in log_transformed}
valid_keys = rounded_logs & validation_set

# Final verification key is the product of valid keys raised to the power of their count
valid_count = len(valid_keys)
final_verification_key = 1
for key in valid_keys:
    final_verification_key *= modular_power(key, valid_count, cipher_modulus)

print(f"Result: {final_verification_key}")