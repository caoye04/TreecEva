from collections import Counter
import math

def calculate_entropy(group):
    count = Counter(group)
    total = len(group)
    entropy = 0.0
    for freq in count.values():
        p = freq / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 3)

def analyze_distribution(data):
    # Irrelevant preprocessing step (minimal interference)
    normalized = [x / sum(data) for x in data]
    threshold = 0.1
    significant = [x for x in normalized if x > threshold]
    return len(significant)

data_groups = [
    [1, 1, 1, 2, 2],
    [1, 2, 3, 4, 5],
    [2, 2, 2, 2]
]

# Secondary analysis with no effect on main result
sample_sizes = list(map(len, data_groups))
sample_sizes_filtered = [s for s in sample_sizes if s > 3]
size_count = len(sample_sizes_filtered)

# Core computation
compute_entropy = lambda g: calculate_entropy(g)
total_entropy = sum([compute_entropy(group) for group in data_groups])

Result: {total_entropy}