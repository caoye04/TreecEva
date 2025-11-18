from collections import defaultdict
from math import gcd
from functools import reduce

def calculate_lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Cryptographic key components
key_primes = [17, 19, 23, 29, 31]
key_exponents = [3, 2, 4, 1, 5]

# Initialize DP table for storing intermediate GCD results
gcd_memo = defaultdict(int)
score_tracker = defaultdict(lambda: defaultdict(int))

# Calculate base scores using prime exponents
base_scores = list(map(lambda x: x[0] * x[1], zip(key_primes, key_exponents)))

# Dynamic programming phase for calculating overlapping GCD strengths
for i in range(len(base_scores)):
    for j in range(i+1, len(base_scores)):
        if i == 0:
            gcd_memo[(i,j)] = gcd(base_scores[i], base_scores[j])
        else:
            gcd_memo[(i,j)] = gcd(gcd_memo[(i-1,j)], base_scores[i])
        
        # Apply conditional scoring based on GCD values
        if gcd_memo[(i,j)] > 10:
            score_tracker[i][j] = base_scores[i] + base_scores[j]
        elif gcd_memo[(i,j)] > 5:
            score_tracker[i][j] = calculate_lcm(base_scores[i], base_scores[j])
        else:
            score_tracker[i][j] = base_scores[i] * base_scores[j]

# Aggregate final score using reduction
final_components = []
for i in range(len(base_scores)):
    for j in range(i+1, len(base_scores)):
        final_components.append(score_tracker[i][j])

final_score = reduce(lambda acc, val: acc + (val if val % 2 == 0 else val * 2), final_components, 0)
print(f"Result: {final_score}")