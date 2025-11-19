from dataclasses import dataclass
from functools import reduce
from math import gcd

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)
    return primes

@dataclass(frozen=True)
class ResearchGroup:
    authors: frozenset
    publications: int

    def shared_factor_strength(self, other_group):
        # Calculate product of author IDs for each group
        self_product = reduce(lambda x, y: x * y, self.authors, 1)
        other_product = reduce(lambda x, y: x * y, other_group.authors, 1)
        
        # Find common prime factors
        primes = sieve_of_eratosthenes(max(self_product, other_product))
        common_primes = [p for p in primes if self_product % p == 0 and other_product % p == 0]
        
        # Return sum of common prime factors multiplied by publication overlap
        overlap = min(self.publications, other_group.publications)
        return sum(common_primes) * overlap if common_primes else 0

# Define research groups
group_alpha = ResearchGroup(authors=frozenset({2, 3, 5}), publications=7)
group_beta = ResearchGroup(authors=frozenset({3, 5, 7}), publications=5)
group_gamma = ResearchGroup(authors=frozenset({2, 7, 11}), publications=3)

collaboration_network = [group_alpha, group_beta, group_gamma]

# Compute collaboration index
prime_factors = sieve_of_eratosthenes(20)
even_primes = {p for p in prime_factors if p % 2 == 0}
odd_primes = {p for p in prime_factors if p % 2 != 0}

# Check if any group has authors that are all odd primes
homogeneous_groups = 0
for group in collaboration_network:
    if all(author in odd_primes for author in group.authors):
        homogeneous_groups += 1

# Calculate collaboration index based on group interactions
if homogeneous_groups > 1:
    collaboration_index = group_alpha.shared_factor_strength(group_beta) + group_beta.shared_factor_strength(group_gamma)
else:
    # Find the group with maximum shared factor strength with any other group
    max_strength = 0
    for i in range(len(collaboration_network)):
        for j in range(i+1, len(collaboration_network)):
            strength = collaboration_network[i].shared_factor_strength(collaboration_network[j])
            if strength > max_strength:
                max_strength = strength
    collaboration_index = max_strength

print(f"Result: {collaboration_index}")