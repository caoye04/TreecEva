import re
from collections import defaultdict
from functools import reduce

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

tokens = ['a1b2', 'c3d4', 'e5f6', 'g7h8']
prime_weights = [2, 3, 5, 7]
fib_indices = [4, 6, 8, 10]

char_sets = [frozenset(re.findall(r'[a-z]', token)) for token in tokens]
numeric_sets = [frozenset(re.findall(r'\d', token)) for token in tokens]

intersection_cardinalities = [
    len(char_sets[i] & numeric_sets[i]) for i in range(len(tokens))
]

lcm_chain = reduce(lcm, prime_weights)
fibonacci_sum = sum(fibonacci(i) for i in fib_indices)

verification_components = [
    lcm_chain * intersection_cardinalities[i] + fibonacci_sum
    for i in range(len(intersection_cardinalities))
]

verification_score = sum(
    component * len(tokens[i])
    for i, component in enumerate(verification_components)
)

print(f"Result: {verification_score}")