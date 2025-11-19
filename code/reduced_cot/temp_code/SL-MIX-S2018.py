from math import gcd
from functools import reduce

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def generate_primes(limit):
    primes = []
    num = 2
    while len(primes) < limit:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Initialize observation parameters
stellar_seeds = generate_primes(2)
sequence_length = 10
modulus_base = reduce(lambda x, y: x * y // gcd(x, y), stellar_seeds)  # LCM of seeds

# Generate cosmic signature sequence
cosmic_signature = [stellar_seeds[0], stellar_seeds[1]]
for idx in range(2, sequence_length):
    cosmic_signature.append(cosmic_signature[idx-1] + cosmic_signature[idx-2])

# Validation process
validation_key = 0
for element in cosmic_signature[:8]:
    if element % modulus_base != 0:
        validation_key = -1
        break
else:
    # If all checked elements are valid, compute validation key
    filtered_values = list(filter(lambda x: x > modulus_base, cosmic_signature[:8]))
    if filtered_values:
        validation_key = sum(map(lambda x: x // modulus_base, filtered_values))
    else:
        validation_key = 0

print(f"Result: {validation_key}")