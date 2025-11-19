import math
from itertools import combinations
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

cosmic_signatures = [
    [2, 8, 18],
    [3, 12, 27],
    [5, 20, 50],
    [7, 28, 63]
]

cosmic_evaluations = 0
for signature in cosmic_signatures:
    product = 1
    for num in signature:
        product *= num
    
    sqrt_product = int(math.sqrt(product))
    is_perfect_square = sqrt_product * sqrt_product == product
    
    prime_count = sum(1 for num in signature if is_prime(num))
    sum_divisible_by_primes = (sum(signature) % prime_count == 0) if prime_count > 0 else False
    
    valid_signature = is_perfect_square and sum_divisible_by_primes
    cosmic_evaluations += int(valid_signature)

print(f"Result: {cosmic_evaluations}")