from collections import Counter
from itertools import permutations
import math

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

genetic_markers = ['A', 'B', 'C', 'D']
score_counter = Counter()

for perm in permutations(genetic_markers, 3):
    checksum = sum(ord(char) * fibonacci(i+1) for i, char in enumerate(perm))
    normalized_checksum = checksum % 100
    score_counter[normalized_checksum] += 1

max_frequency = max(score_counter.values())
dominant_score_frequency = sum(1 for freq in score_counter.values() if freq == max_frequency)

print(f"Result: {dominant_score_frequency}")