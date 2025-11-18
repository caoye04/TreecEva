from math import gcd
from functools import reduce
from collections import defaultdict

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

tetrahedron_edges = [
    [12, 15, 18, 21, 24, 27],
    [10, 14, 22, 26, 34, 38],
    [11, 13, 17, 19, 23, 29],
    [16, 20, 25, 30, 35, 40],
    [28, 32, 36, 42, 45, 48]
]

accumulated_energy = 0.0
prime_edge_cache = {}

def get_prime_product(edges):
    product = 1
    for edge in edges:
        if edge not in prime_edge_cache:
            prime_edge_cache[edge] = is_prime(edge)
        if prime_edge_cache[edge]:
            product *= edge
    return product

for edges in tetrahedron_edges:
    prime_product = get_prime_product(edges)
    if prime_product > 1:
        g = reduce(gcd, edges)
        resonance_index = prime_product / g
        accumulated_energy += resonance_index
    else:
        # If no prime edges, contribute zero to energy
        pass

# Apply a final normalization factor based on number of tetrahedrons
normalization_factor = len(tetrahedron_edges) ** 0.5
accumulated_energy = accumulated_energy / normalization_factor

print(f"Result: {accumulated_energy}")