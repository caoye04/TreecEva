from itertools import combinations

def analyze_patterns(sequence):
    count = 0
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            if sequence[i] + sequence[j] == 7:  # red herring: counts pairs summing to 7
                count += 1
    return count

def compute_redundant_metric(data_list):
    temp_result = 0
    for idx, val in enumerate(data_list):
        temp_result += (idx * val) % 4  # irrelevant computation
    return temp_result

def extract_significant_pairs(values):
    pairs = []
    for a, b in combinations(values, 2):
        if abs(a - b) > 5:
            pairs.append((a, b))
    return len(pairs)  # unused later

def calculate_final_score(ranks, coeffs):
    score = 0.0
    normalized = [r / sum(ranks) for r in ranks]
    for n, w in zip(normalized, coeffs):
        score += n * w * 100
    return int(score)

# Main execution block
if __name__ == "__main__":
    # Input data
    rankings = [8, 12, 5, 20, 15]
    weights = [0.1, 0.2, 0.15, 0.25, 0.3]

    # Distractor computations
    pair_count = analyze_patterns(rankings)
    dummy_metric = compute_redundant_metric(rankings)
    significant_diffs = extract_significant_pairs(rankings)

    # State tracking with intermediate variables
    total_rank = sum(rankings)
    avg_rank = total_rank / len(rankings)
    adjusted_weights = [w * 1.1 for w in weights]  # not used, misleading

    # Core logic embedded among distractions
    scaling_factor = 1.0
    for i, r in enumerate(rankings):
        if r > avg_rank:
            scaling_factor *= 1.05

    # Key statement
    final_score = calculate_final_score(rankings, weights)

    # Output result
    print(f"Result: {final_score}")