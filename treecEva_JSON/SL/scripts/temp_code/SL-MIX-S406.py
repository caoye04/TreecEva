from math import gcd
from functools import reduce
from itertools import permutations

def ascii_sum(s):
    return sum(ord(c) for c in s)

seed = 123
perms = [''.join(p) for p in permutations(str(seed))]
transformed_values = [ascii_sum(p) for p in perms]
value_counts = {v: transformed_values.count(v) for v in set(transformed_values)}
unique_values = list(value_counts.keys())
final_gcd = reduce(gcd, unique_values)

print(f"Result: {final_gcd}")