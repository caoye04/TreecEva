import re
from functools import reduce
from math import gcd

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Encoded packet signatures
packet_signatures = ['A1B2C3', 'D4E5F6', 'G7H8I9']

# Extract numeric components and apply transformations
numeric_values = []
for signature in packet_signatures:
    numbers = list(map(int, re.findall(r'\d', signature)))
    transformed = [n**2 if n % 2 == 0 else n**3 for n in numbers]
    numeric_values.append(transformed)

# Create sets from transformed values
value_sets = [frozenset(vals) for vals in numeric_values]

# Find intersection of all sets
common_elements = reduce(lambda a, b: a & b, value_sets)

# Calculate LCM of common elements if any exist
if common_elements:
    checksum_base = reduce(lcm, common_elements)
else:
    checksum_base = 0

# Apply cryptographic weighting using lambda
weight_function = lambda x: (x & 0xFF) ^ ((x >> 8) & 0xFF)
weighted_checksum = weight_function(checksum_base) if checksum_base else 0

# Final verification score combines weighted checksum with set cardinality
verification_score = weighted_checksum + len(common_elements)

print(f"Result: {verification_score}")