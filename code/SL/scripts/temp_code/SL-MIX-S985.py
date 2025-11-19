import math
from functools import reduce

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

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

lunar_sequence = [3]  # Initial term
modular_increment = 7
signal_count = 12

for position in range(2, signal_count + 1):
    sum_previous = sum(lunar_sequence)
    term_numerator = (sum_previous + (position % modular_increment))
    new_term = math.gcd(position, term_numerator)
    lunar_sequence.append(new_term)

# Calculate signal strength using various number theory operations
prime_positions = [i for i in range(1, signal_count+1) if is_prime(i)]
lunar_primes = [lunar_sequence[i-1] for i in prime_positions]
gcd_of_primes = gcd_list(lunar_primes) if lunar_primes else 0

composite_count = signal_count - len(prime_positions) - 1  # Subtract 1 for number 1
lunar_composites = [lunar_sequence[i-1] for i in range(1, signal_count+1) if not is_prime(i) and i > 1]
lcm_of_composites = reduce(lambda x, y: lcm(x, y) if x and y else (x or y), lunar_composites, 1) if lunar_composites else 1

weighted_sum = sum(val * (idx + 1) for idx, val in enumerate(lunar_sequence))
frequency_adjustment = (weighted_sum % 13) + 1

lunar_signal_strength = (gcd_of_primes * lcm_of_composites + frequency_adjustment) % 1000

print(f"Result: {lunar_signal_strength}")