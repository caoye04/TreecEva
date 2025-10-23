import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

primes = [i for i in range(2, 50) if is_prime(i)]
prime_indices = {p: idx for idx, p in enumerate(primes, 1)}

selected_primes = [p for p in primes if p < 20]
indices = [prime_indices[p] for p in selected_primes]
lcm_value = indices[0]
for i in indices[1:]:
    lcm_value = (lcm_value * i) // math.gcd(lcm_value, i)

bit_shifted = lcm_value << 2
adjusted_value = bit_shifted if bit_shifted > 1000 else bit_shifted * 3

cryptographic_key = adjusted_value
if cryptographic_key > 5000 and (cryptographic_key & 0xF) == 0:
    cryptographic_key += 100
else:
    cryptographic_key -= 50

print(f"Result: {cryptographic_key}")