from math import gcd
from functools import reduce
from itertools import combinations

def lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0

def get_primes_up_to(n):
    sieve = [True] * (n+1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

# Molecular adjacency matrix (symmetric, undirected graph)
molecular_bonds = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 1, 1, 0]
]

num_atoms = len(molecular_bonds)
prime_weights = get_primes_up_to(num_atoms * num_atoms)
path_products = set()

for node_a, node_b in combinations(range(num_atoms), 2):
    if molecular_bonds[node_a][node_b]:
        for node_c in range(num_atoms):
            if molecular_bonds[node_b][node_c] and node_c != node_a:
                product = prime_weights[node_a] * prime_weights[node_b] * prime_weights[node_c]
                path_products.add(product)

if path_products:
    topological_index = reduce(lcm, path_products)
else:
    topological_index = 0

print(f"Result: {topological_index}")