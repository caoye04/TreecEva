from itertools import combinations

def analyze_performance(metrics):
    # Irrelevant helper: computes variance but not used in final logic
    mean_val = sum(metrics) / len(metrics)
    variance = sum((x - mean_val) ** 2 for x in metrics) / len(metrics)
    return variance

def filter_outliers(data, threshold=2):
    # Dead code path — never actually called
    return [x for x in data if abs(x - sum(data)/len(data)) < threshold]

def calculate_final_score(ranks, importance_weights):
    total = 0
    temp_offset = 0

    # Simulate historical baseline (distractor computation)
    baseline = sum(ranks) / len(ranks)
    adjustment_factor = 0.95

    for i, (rank, weight) in enumerate(zip(ranks, importance_weights)):
        # Relevant scoring logic
        contribution = (10 - rank) * weight  # Higher weight amplifies better (lower) ranks
        total += contribution

        # Distractor: tracking unused trend
        if rank < baseline:
            temp_offset += 1

    # Additional irrelevant transformation
    decayed_total = total * adjustment_factor
    normalized = abs(decayed_total) % 1000

    # Key result built from meaningful logic
    final = int(normalized + temp_offset)  # temp_offset adds minor interference
    return final

# Main execution block
if __name__ == '__main__':
    # Input data
    candidate_ranks = [3, 1, 4, 2, 5]
    feature_weights = [0.8, 1.2, 0.9, 1.1, 0.7]

    # Unused variables — red herrings
    performance_metrics = [88, 92, 76, 85, 94]
    outlier_data = [10, 15, 12, 1000, 14]  # clearly has outlier but ignored

    # Compute auxiliary metric (not used)
    _ = analyze_performance(performance_metrics)

    # Generate combinatorial pairs (completely irrelevant to final score)
    pair_combinations = list(combinations(candidate_ranks, 2))
    combination_count = len(pair_combinations)

    # Lambda-based filtering (semi-relevant structure but not impacting outcome)
    valid_ranks = list(filter(lambda x: x <= 5, candidate_ranks))  # all are <=5

    # Core calculation — this determines the answer
    final_score = calculate_final_score(candidate_ranks, feature_weights)

    # Print result as required
    print(f"Result: {final_score}")