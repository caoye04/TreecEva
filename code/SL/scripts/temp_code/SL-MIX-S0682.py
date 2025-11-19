def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

primes = sieve_of_eratosthenes(100)
phrase = 'MATH'
prime_indices = [ord(char) % 10 for char in phrase]
cipher_key = 1
for index in prime_indices:
    cipher_key *= primes[index]
print(f'Result: {cipher_key}')