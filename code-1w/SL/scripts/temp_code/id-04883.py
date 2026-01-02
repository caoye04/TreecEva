def generate_primes(n):
    sieve = [True] * n
    sieve[0:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n, i):
                sieve[j] = False
    return set(i for i, is_prime in enumerate(sieve))


def generate_fibonacci(n):
    fib_set = set()
    a, b = 0, 1
    while a < n:
        fib_set.add(a)
        a, b = b, a + b
    return fib_set

# Generate prime numbers below 50
prime_set = generate_primes(50)

# Generate Fibonacci numbers below 50
fibonacci_set = generate_fibonacci(50)

# Compute intersection size
overlap_count = len(prime_set & fibonacci_set)

# Irrelevant auxiliary variable (minor distraction)
redundant_sum = sum(range(5))

print(f"Result: {overlap_count}")