from math import gcd
from functools import reduce

def smallest_prime_factor(n):
    if n <= 1:
        return 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    return n

# Simulated character values for the first 10 positions of the decoded message
character_values = [72, 101, 108, 108, 111, 32, 87, 111, 114, 108]  # Represents "Hello Worl"

transformed_values = []
for idx in range(1, 11):  # 1-indexed positions
    spf = smallest_prime_factor(idx)
    transformed_values.append(character_values[idx-1] * spf)

# Compute GCD of all transformed values
final_gcd = reduce(gcd, transformed_values)

print(f"Result: {final_gcd}")