import itertools
import functools

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

def compute_combinatorial_value(lst):
    if len(lst) < 2:
        return 1
    product = 1
    for r in range(1, len(lst)+1):
        combinations = list(itertools.combinations(lst, r))
        for combo in combinations:
            product *= sum(combo)
    return product

message = "the quick brown fox jumps over the lazy dog"
tokens = message.split()
word_lengths = list(map(len, tokens))
prime_lengths = list(filter(is_prime, word_lengths))
product_of_primes = functools.reduce(lambda x, y: x * y, prime_lengths, 1)
security_score = compute_combinatorial_value(prime_lengths) % (product_of_primes + 1)
print(f"Result: {security_score}")