import math
from functools import reduce
def gcd_list(lst):
    return reduce(math.gcd, lst) if lst else 0

def mean(data):
    return sum(data) / len(data) if data else 0

def variance(data):
    if len(data) < 2:
        return 0
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / len(data)

memo = {0: 1, 1: 2}
def harmonic_weight(n):
    if n in memo:
        return memo[n]
    hw_n_minus_1 = harmonic_weight(n-1)
    hw_n_minus_2 = harmonic_weight(n-2)
    previous_terms = [harmonic_weight(i) for i in range(n)]
    m = mean(previous_terms)
    v = variance(previous_terms)
    result = (hw_n_minus_1 + hw_n_minus_2) * m + v
    memo[n] = result
    return result

# Compute up to H(6)
for i in range(7):
    harmonic_weight(i)

sequence = [memo[i] for i in range(7)]

# Apply transformation using lambda closure
transform = lambda seq: [seq[i] + math.gcd(i, len(seq)) for i in range(len(seq))]
transformed_sequence = transform(sequence)

# The answer is the 4th element (index 4)
target_result = int(transformed_sequence[4])
print(f"Target result: {target_result}")