from math import gcd
from functools import reduce

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Generate cosmic signature
first_four_primes = [2, 3, 5, 7]
initial_value = reduce(lcm, first_four_primes)

cosmic_signature = [initial_value]
for i in range(1, 12):
    next_val = gcd(i, cosmic_signature[-1])
    cosmic_signature.append(next_val)

# Apply filter using list comprehension
filtered_values = [x for x in cosmic_signature if 1 < x < 10]

# Calculate final result using lambda and sum
signature_sum = sum(filter(lambda v: v > 1 and v < 10, cosmic_signature))

print(f"Result: {signature_sum}")