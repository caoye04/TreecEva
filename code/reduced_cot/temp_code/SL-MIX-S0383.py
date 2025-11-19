def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = []
for num in range(2, 30):
    if is_prime(num):
        primes.append(num)

transform = lambda x: x * 2
transformed_primes = list(map(transform, primes))

from math import gcd
final_sum = 0
for p in transformed_primes:
    final_sum += gcd(p, 15)

print(f"Result: {final_sum}")