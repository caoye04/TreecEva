def sieve(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [i for i in range(2, n+1) if is_prime[i]]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

primes = sieve(99)
prime_harmonies = 0

for i in range(len(primes)):
    for j in range(i+1, len(primes)):
        p, q = primes[i], primes[j]
        if p * q < 100 and gcd(p-1, q-1) > 1:
            prime_harmonies += 1

print(f"Result: {prime_harmonies}")