import math
import itertools

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

def next_prime(n):
    candidate = n + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate

# Generate first 7 primes
primes = []
candidate = 2
while len(primes) < 7:
    if is_prime(candidate):
        primes.append(candidate)
    candidate += 1

# Compute LCM sequence starting with 1
lcm_sequence = [1]
for i in range(5):  # Generate 5 terms
    next_p = next_prime(lcm_sequence[-1])
    lcm_val = (lcm_sequence[-1] * next_p) // math.gcd(lcm_sequence[-1], next_p)
    lcm_sequence.append(lcm_val)

# Combinations of 3 distinct primes from first 7 primes
prime_combinations = list(itertools.combinations(primes, 3))
combination_entropy_sum = 0
for combo in prime_combinations:
    product = combo[0] * combo[1] * combo[2]
    combination_entropy_sum += math.log(product)

# Floating point operations and logical conditions
base_entropy = math.log(lcm_sequence[-1])
total_entropy = base_entropy + combination_entropy_sum

valid_configs = 0
for combo in prime_combinations:
    condition_a = combo[0] + combo[1] > combo[2]
    condition_b = combo[0] * combo[2] < total_entropy
    if condition_a and condition_b:
        valid_configs += 1

# Final calculation using logical operations
final_key_strength = 0
if valid_configs > 10 or total_entropy > 50:
    final_key_strength = int(total_entropy * valid_configs)
else:
    final_key_strength = int(total_entropy + valid_configs)

print(f"Result: {final_key_strength}")