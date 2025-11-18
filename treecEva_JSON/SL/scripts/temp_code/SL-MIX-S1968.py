from math import log, factorial
from collections import defaultdict

def calculate_permutation_entropy(n, r):
    return log(factorial(n) / factorial(n - r), 2)

# Encryption key analysis parameters
key_segments = [3, 4, 2, 5]
security_weights = [0.5, 0.3, 0.8, 0.2]

# Initialize security tracking
segment_scores = defaultdict(float)

# Calculate base scores using lambda function
entropy_calculator = lambda n, r: calculate_permutation_entropy(n, r) if n >= r else 0

for i, (segment, weight) in enumerate(zip(key_segments, security_weights)):
    raw_entropy = entropy_calculator(segment + 5, segment)
    weighted_score = raw_entropy * weight
    segment_scores[i] = weighted_score

# Apply combinatoric adjustment
adjustment_factor = len(list(filter(lambda x: x > 2, key_segments)))
combined_score = sum(segment_scores.values()) * adjustment_factor

# Final security calculation with exponentiation
final_security_score = int(combined_score ** (1/3)) + int(log(combined_score, 10))

print(f'Result: {final_security_score}')