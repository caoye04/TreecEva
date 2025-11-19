def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

def count_distinct_primes(n):
    factors = set()
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            factors.add(d)
            n //= d
        d += 1
    if n > 1:
        factors.add(n)
    return len(factors)

def crypto_strength(num):
    if num < 2:
        return 0
    lpf = largest_prime_factor(num)
    cdp = count_distinct_primes(num)
    return lpf * cdp

numbers = range(100, 151)
aggregate_strength = sum(crypto_strength(n) for n in numbers)
print(f"Result: {aggregate_strength}")