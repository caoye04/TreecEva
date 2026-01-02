from itertools import combinations
import math

def shannon_entropy(counts):
    total = sum(counts)
    probabilities = [c / total for c in counts]
    entropy = sum(-p * math.log2(p) for p in probabilities if p > 0)
    return round(entropy, 4)

# Simulate character frequency observations in encrypted segments
segment_a = [8, 12, 5, 1]
segment_b = [7, 13, 6, 0]
segment_c = [9, 11, 4, 2]

# Compute entropy for each segment
entropies = []
for seg in [segment_a, segment_b, segment_c]:
    entropy = shannon_entropy(seg)
    entropies.append(entropy)

# Combine pairwise segments and compute joint entropy contribution
joint_contributions = []
for pair in combinations([segment_a, segment_b, segment_c], 2):
    merged = [sum(freqs) for freqs in zip(pair[0], pair[1])]
    joint_entropy = shannon_entropy(merged)
    joint_contributions.append(joint_entropy)

# Final aggregation step
baseline_avg = sum(entropies) / len(entropies)
bonus = max(joint_contributions) - baseline_avg

total_entropy = sum(entropies)
total_entropy += bonus  # Adjust for cross-segment redundancy reduction

print(f"Result: {total_entropy}")