import math

def hamming_weight(n):
    return bin(n).count('1')

bases = range(3, 8)
exponents = range(1, 11)
modulus = 19
hamming_threshold = 3

unique_patterns = set()

for base in bases:
    for exp in exponents:
        result = pow(base, exp, modulus)
        if hamming_weight(result) >= hamming_threshold:
            unique_patterns.add(result)

if len(unique_patterns) > 0:
    cryptographic_score = math.log2(len(unique_patterns))
else:
    cryptographic_score = 0

print(f"Result: {cryptographic_score}")