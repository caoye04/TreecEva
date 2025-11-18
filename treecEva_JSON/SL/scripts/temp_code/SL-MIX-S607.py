from functools import reduce

def prime_factors(n):
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

number_to_factor = 84
factors_list = prime_factors(number_to_factor)
unique_prime_factors = list(set(factors_list))
smallest_prime = min(unique_prime_factors)
largest_prime = max(unique_prime_factors)
security_strength = smallest_prime * largest_prime
print(f"Result: {security_strength}")