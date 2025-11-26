def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Process number range with slicing and itertools
import itertools

numbers = list(range(2, 50))
prime_candidates = numbers[::2] + numbers[1::3]
filtered_candidates = [x for x in prime_candidates if x % 3 != 0]

# Distractor operations (not used in final result)
prime_squares = [x**2 for x in filtered_candidates if x < 20]
dummy_sum = sum(prime_squares)

# Main logic with modular arithmetic
valid_primes = []
for num in filtered_candidates:
    if is_prime(num) and num % 4 == 1:
        valid_primes.append(num)

# Another distractor operation
prime_pairs = list(itertools.combinations(valid_primes, 2))

final_output = sum(valid_primes)
print(f"Result: {final_output}")