import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Generate primes up to 30
prime_candidates = [i for i in range(2, 31) if is_prime(i)]

# Calculate modular exponentiations
mod_exp_results = {p: pow(p, p+1, 31) for p in prime_candidates}

# Find primes where result equals 1
special_primes = {p for p, result in mod_exp_results.items() if result == 1}

# Process special primes through a switch-like structure
cryptographic_components = []
for prime in sorted(special_primes):
    match prime % 5:
        case 0:
            cryptographic_components.append(prime * 2)
        case 1:
            cryptographic_components.append(prime ** 2)
        case 2:
            cryptographic_components.append(int(math.log(prime) * 100))
        case 3:
            cryptographic_components.append(prime << 2)
        case 4:
            cryptographic_components.append(prime | 15)

# Calculate final key using GCD and LCM operations
if len(cryptographic_components) >= 2:
    first_pair_gcd = math.gcd(cryptographic_components[0], cryptographic_components[1])
    last_pair_lcm = (cryptographic_components[-1] * cryptographic_components[-2]) // math.gcd(cryptographic_components[-1], cryptographic_components[-2])
    cryptographic_key = first_pair_gcd + last_pair_lcm
else:
    cryptographic_key = sum(cryptographic_components)

print(f"Result: {cryptographic_key}")