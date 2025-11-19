from math import gcd
from itertools import combinations

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

threshold = 100
lower_bound = 5
upper_bound = 20
valid_pairs = []

for a, b in combinations(range(lower_bound, upper_bound + 1), 2):
    if gcd(a, b) == 1 and (a * b) < threshold:
        valid_pairs.append((a, b))

prime_count = sum(1 for pair in valid_pairs if is_prime(pair[0]) or is_prime(pair[1]))
composite_count = len(valid_pairs) - prime_count

security_index = float(prime_count * 3.5 - composite_count * 1.2)
print(f"Result: {security_index}")