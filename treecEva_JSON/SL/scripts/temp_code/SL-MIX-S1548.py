from functools import reduce
from math import gcd

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Generate primes up to 50
primes = list(filter(is_prime, range(2, 51)))

# Select primes that are 1 mod 4
selected_primes = list(filter(lambda p: p % 4 == 1, primes))

# Calculate mean of selected primes
mean_prime = sum(selected_primes) // len(selected_primes)

# Compute product of selected primes
product_primes = reduce(lambda x, y: x * y, selected_primes, 1)

# Apply modular arithmetic
modulus = 100
base = mean_prime % modulus
exponent = len(selected_primes)
mod_exp_result = pow(base, exponent, modulus)

# Compute GCD
common_divisor = gcd(mod_exp_result, product_primes)

# Final transformation using ternary operator and logical operations
is_valid_base = base > 10 and base < 50
adjusted_base = mod_exp_result + 5 if is_valid_base else mod_exp_result - 5
final_exponent = 3 if common_divisor == 1 else 2

cipher_key = (adjusted_base ** final_exponent) % 79

print(f"Result: {cipher_key}")