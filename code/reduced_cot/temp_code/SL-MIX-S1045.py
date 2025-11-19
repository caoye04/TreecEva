from math import gcd

def fibonacci_sequence(n):
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

# Generate first 20 Fibonacci numbers
fib_numbers = fibonacci_sequence(19)

# Select prime numbers at Fibonacci indices (excluding 0 and 1)
prime_candidates = [fib_numbers[i] for i in range(2, len(fib_numbers)) if is_prime(fib_numbers[i])]

# Calculate pairwise GCD matrix using dictionary comprehension
pairwise_gcd = {(p1, p2): gcd(p1, p2) for p1 in prime_candidates for p2 in prime_candidates}

# Determine which pairs have coprime relationship (GCD = 1)
coprime_pairs = {k: v for k, v in pairwise_gcd.items() if v == 1}

# Security index calculation using ternary operator logic
security_weights = [13, 29, 5, 89, 233]
security_index = sum(weight if (weight, weight) in coprime_pairs else weight//2 for weight in security_weights)

print(f"Result: {security_index}")