from itertools import combinations
from math import ceil

# Simulate student assessment scoring with weighted aggregation and noise filtering

def analyze_pattern(seq):
    if len(seq) < 3:
        return False
    # Irrelevant pattern check (distractor)
    for i in range(len(seq) - 2):
        if seq[i] + seq[i+2] == 2 * seq[i+1]:
            return True
    return False

# Distractor function - never called
def calculate_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = sum(counts.values())
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * __import__('math').log2(p)
    return entropy

# Main processing pipeline
assessments = [85, 90, 78, 92, 88]
weights = [0.2, 0.25, 0.15, 0.3, 0.1]

# Noise detection via set operations (semi-relevant)
baseline_set = {75, 80, 85, 90}
reading_set = set(assessments)
anomalies = reading_set.symmetric_difference(baseline_set)

# Generate all possible weight triplets (mostly irrelevant)
weight_triplets = list(combinations(weights, 3))
triplet_count = len(weight_triplets)

# Normalize weights (actually relevant)
sum_weights = sum(weights)
normalized_weights = [w / sum_weights for w in weights]

# Apply exponential smoothing factor (distractor)
smoothing_factor = 0.1
smoothed_scores = []
for s in assessments:
    adjusted = s * (1 + smoothing_factor) if s < 85 else s * (1 - smoothing_factor)
    smoothed_scores.append(round(adjusted))

# Use original assessments (not smoothed) — makes smoothing a red herring
aggregate = 0
for i in range(len(assessments)):
    aggregate += assessments[i] * normalized_weights[i]

# Final adjustment based on performance threshold
if aggregate > 85:
    bonus = 5
else:
    bonus = 2

# Introduce dummy tracking state (distractor)
class StateTracker:
    def __init__(self):
        self.step = 0
        self.log = []

tracker = StateTracker()
tracker.step += 1

# Critical assignment
final_score = int(ceil(aggregate)) + bonus

# Debug prints removed for clarity
Result: final_score