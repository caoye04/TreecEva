from math import factorial
from functools import lru_cache

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def permute_count(n, r):
    return factorial(n) // factorial(n - r)

@lru_cache(maxsize=None)
def combination_count(n, r):
    if r > n:
        return 0
    return factorial(n) // (factorial(r) * factorial(n - r))

class KeyProfile:
    def __init__(self, base_chars, extension_chars):
        self.base = base_chars
        self.extension = extension_chars
        self.length = len(base_chars) + len(extension_chars)
    
    @property
    def is_balanced(self):
        return len(self.base) == len(self.extension)

# Initialize cryptographic components
primary_chars = ['A', 'B', 'C']
secondary_chars = ['X', 'Y']
key_profile = KeyProfile(primary_chars, secondary_chars)

# Calculate combinatorial metrics
base_permutations = permute_count(len(primary_chars), 2)
extension_combinations = combination_count(len(secondary_chars)+2, 2)

# Apply Fibonacci weighting based on key profile length
fib_weight = fibonacci(key_profile.length) if key_profile.is_balanced else fibonacci(key_profile.length - 1)

# Determine adjustment factor using ternary operator
adjustment_factor = 3 if len(primary_chars) > len(secondary_chars) else (2 if len(primary_chars) == len(secondary_chars) else 1)

# Compute intermediate security metric
security_metric = (base_permutations + extension_combinations) * fib_weight

# Calculate final key strength with conditional modifier
final_key_strength = security_metric - (adjustment_factor * 10) if security_metric > 50 else security_metric + (adjustment_factor * 5)

print(f"Result: {final_key_strength}")