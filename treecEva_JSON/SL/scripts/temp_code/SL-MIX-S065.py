import math
from collections import defaultdict

def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return [i for i in range(2, limit + 1) if is_prime[i]]

def prime_gap_sequence(primes, n):
    gaps = []
    for i in range(1, min(n+1, len(primes))):
        gaps.append(primes[i] - primes[i-1])
    return gaps

def modular_pow(base, exponent, modulus):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = (result * base) % modulus
        exponent >>= 1
        base = (base * base) % modulus
    return result

# Main computation
primes_list = sieve_of_eratosthenes(100)
gap_values = prime_gap_sequence(primes_list, 15)

transformed_gaps = []
for gap in gap_values:
    match gap:
        case 1:
            transformed_gaps.append(gap * 2)
        case 2:
            transformed_gaps.append(gap ** 2)
        case 4:
            transformed_gaps.append(int(math.log(gap) * 10))
        case 6:
            transformed_gaps.append(modular_pow(gap, 2, 10))
        case _:
            transformed_gaps.append(gap + 1)

frequency_map = defaultdict(int)
for val in transformed_gaps:
    frequency_map[val] += 1

unique_elements = list(set(transformed_gaps))
sorted_elements = sorted(unique_elements, reverse=True)

log_sum = sum(math.log(x) for x in sorted_elements if x > 0)
exp_factor = int(math.exp(log_sum / len(sorted_elements)))

encryption_base = sum(val * freq for val, freq in frequency_map.items())
encryption_key = modular_pow(encryption_base, exp_factor, 97)

print(f"Result: {encryption_key}")