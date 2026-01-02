from itertools import combinations

# Simulate evaluation of candidate solutions based on consistency and weight
weights = [3, 7, 2, 9, 4]
consistency = [0.8, 0.5, 0.9, 0.4, 0.6]
labels = ['A', 'B', 'C', 'D', 'E']

# Irrelevant pre-processing: shuffle labels (not used in final logic)
shuffled_labels = [labels[i] for i in range(len(labels)-1, -1, -1)]

# Misleading normalization (never used)
normalized_weights = [w / sum(weights) for w in weights]

# Identify high-consistency candidates
high_consistency = [i for i, c in enumerate(consistency) if c > 0.5]

# Generate all valid pairs from high-consistency indices
valid_pairs = list(combinations(high_consistency, 2))

# Compute pairwise compatibility score using lambda
compatibility_scorer = lambda x, y: abs(weights[x] - weights[y]) * (consistency[x] + consistency[y])

pair_scores = []
for p in valid_pairs:
    score = compatibility_scorer(p[0], p[1])
    pair_scores.append(score)

# Dummy filter: only keep scores above threshold (some are below, so partial filtering)
filtered_scores = [s for s in pair_scores if s > 8.0]

# Compute average of filtered scores (semi-relevant but not final)
avg_filtered = sum(filtered_scores) / len(filtered_scores) if filtered_scores else 0

# Balance metric: count how many original weights are above median
median_weight = sorted(weights)[len(weights)//2]
above_median_count = len([w for w in weights if w > median_weight])

# Create balanced_items: indices where weight > median and consistency > 0.55
balanced_items = []
for i in range(len(weights)):
    if weights[i] > median_weight and consistency[i] > 0.55:
        balanced_items.append(i)

# Dead code: unused helper function
# def useless_transform(x): return x ** 2 + 1

# Core ranking logic
def calculate_ranking(indices):
    if not indices:
        return 0
    # Use combination count as base
    base = len(list(combinations(indices, 2)))
    # Boost by sum of consistency values at those indices
    boost = sum(consistency[i] for i in indices)
    return base * boost

final_score = calculate_ranking(balanced_items)
print(f"Target result: {final_score}")