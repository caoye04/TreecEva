from math import prod
from itertools import permutations

def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return primes

# Map letters to primes
alphabet = 'abcdefghijklmnopqrstuvwxyz'
primes_list = sieve_of_eratosthenes(100)[:26]
char_to_prime = dict(zip(alphabet, primes_list))
prime_to_char = {v: k for k, v in char_to_prime.items()}

# Document signature
signature = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29 * 31 * 37 * 41 * 43 * 47 * 53 * 59 * 61 * 67 * 71 * 73 * 79 * 83 * 89 * 97 * 101

# Factorize the signature to get primes
factors = []
current_signature = signature
for p in primes_list:
    while current_signature % p == 0:
        factors.append(p)
        current_signature //= p
    if current_signature == 1:
        break

# Decode primes back to characters
original_chars = [prime_to_char[p] for p in factors]

# Filter out vowels
vowels_set = frozenset('aeiou')
consonants = [c for c in original_chars if c not in vowels_set]

# Sort consonants alphabetically
sorted_consonants = sorted(consonants)

# Count unique arrangements of the first 5 consonants considering duplicates
first_five = sorted_consonants[:5]
unique_perms = set(permutations(first_five))
final_arrangements = len(unique_perms)

print(f"Result: {final_arrangements}")