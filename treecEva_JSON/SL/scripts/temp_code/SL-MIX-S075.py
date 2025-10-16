class PrimeNode:
    def __init__(self, prime_factor):
        self.prime_factor = prime_factor
        self.next = None

def get_prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

import itertools

number = 210
prime_factors = sorted(list(set(get_prime_factors(number))))

# Create linked list of primes
head = None
for p in reversed(prime_factors):
    node = PrimeNode(p)
    node.next = head
    head = node

# Process linked list with bit operations
values = []
current = head
position = 0
while current:
    pf = current.prime_factor
    shifted = pf << position
    masked = shifted & 0xFF
    xor_result = masked ^ (pf >> 1)
    values.append(xor_result)
    position += 1
    current = current.next

# Apply reduction using lambda and itertools
reducer = lambda acc, x: acc ^ (x * 3 + 1)
cipher_strength = 0
for val in values:
    cipher_strength = reducer(cipher_strength, val)

cipher_strength = cipher_strength & 0xFFFF  # Final mask
print(f"Result: {cipher_strength}")