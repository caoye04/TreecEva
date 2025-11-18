from itertools import product

def hamming_distance(a, b):
    return bin(a ^ b).count('1')

# Generate all possible 4-bit patterns (0 to 15)
patterns = range(16)

# Count patterns with Hamming distance exactly 2 from 0b1010 (decimal 10)
distinctive_count = sum(1 for p in patterns if hamming_distance(p, 0b1010) == 2)

# Apply a transformation based on parity
if distinctive_count % 2 == 0:
    result_value = distinctive_count * 3
else:
    result_value = distinctive_count + 5

# Final adjustment based on a conditional expression
result_value = result_value if result_value > 20 else result_value * 2

print(f"Result: {result_value}")