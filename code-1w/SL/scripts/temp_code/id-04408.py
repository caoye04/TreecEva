from itertools import combinations

# Simulate evaluation of balanced binary sequences for fairness testing
def generate_binary_profiles(n):
    """Generate all binary sequences of length n with equal 0s and 1s."""
    if n % 2 != 0:
        return []
    half = n // 2
    indices = list(range(n))
    profiles = []
    for pos_ones in combinations(indices, half):
        profile = [0] * n
        for i in pos_ones:
            profile[i] = 1
        profiles.append(profile)
    return profiles

def compute_entropy(vector):
    """Compute basic entropy-like measure (for distraction)"""
    from math import log2
    count_0 = vector.count(0)
    count_1 = vector.count(1)
    total = len(vector)
    if count_0 == 0 or count_1 == 0:
        return 0.0
    p0 = count_0 / total
    p1 = count_1 / total
    return -p0 * log2(p0) - p1 * log2(p1)

def analyze_pairwise_consistency(profiles):
    """Analyze consistency across all profile pairs (some used, some not)"""
    n_profiles = len(profiles)
    consistency_matrix = [[0]*n_profiles for _ in range(n_profiles)]
    entropy_values = [compute_entropy(p) for p in profiles]  # Distractor: computed but not fully used

    for i in range(n_profiles):
        for j in range(i+1, n_profiles):
            matches = sum(1 for a, b in zip(profiles[i], profiles[j]) if a == b)
            score = abs(matches - len(profiles[i])//2)  # deviation from random match
            consistency_matrix[i][j] = score
            consistency_matrix[j][i] = score

    # Extract highly consistent pairs (difference <= 1 from expected)
    balanced_pairs = []
    expected = len(profiles[0]) // 2
    for i in range(n_profiles):
        for j in range(i+1, n_profiles):
            matches = sum(a == b for a, b in zip(profiles[i], profiles[j]))
            if abs(matches - expected) <= 1:
                balanced_pairs.append((i, j, matches))

    # Irrelevant aggregation (dead computation path)
    avg_consistency = sum(sum(row) for row in consistency_matrix) / (n_profiles * n_profiles) if n_profiles else 0

    return balanced_pairs, entropy_values, avg_consistency

def calculate_ranking(pair_list):
    """Rank pair list by third element, take weighted sum"""
    sorted_pairs = sorted(pair_list, key=lambda x: x[2], reverse=True)
    ranking_score = 0
    for idx, (_, _, matches) in enumerate(sorted_pairs):
        weight = len(sorted_pairs) - idx
        ranking_score += weight * matches
    return ranking_score

# Main execution flow
sequence_length = 6
all_profiles = generate_binary_profiles(sequence_length)
distinctive_features = {tuple(p): hash(tuple(p)) % 100 for p in all_profiles}  # unused distractor map

# Analyze only the balanced interaction pairs
pairs_data, entropies, avg_cons = analyze_pairwise_consistency(all_profiles)

# Critical computation point
final_score = calculate_ranking(pairs_data)

# Print final result as required
print(f"Result: {final_score}")