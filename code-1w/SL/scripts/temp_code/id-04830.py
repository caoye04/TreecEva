from itertools import combinations

# Simulate user engagement metrics across multiple app modules
def analyze_engagement(base_metrics, thresholds):
    high_performers = []
    temp_debug_log = []

    for i, metric in enumerate(base_metrics):
        normalized = (metric - min(base_metrics)) / (max(base_metrics) - min(base_metrics) + 1e-5)
        category = 'A' if normalized > thresholds['A'] else ('B' if normalized > thresholds['B'] else 'C')
        
        # Irrelevant transformation (distractor)
        transformed = sum([x ** 0.5 for x in base_metrics[:i+1] if x > 1])
        temp_debug_log.append(transformed)

        if category == 'A':
            high_performers.append(i)

    return high_performers

# Rank calculation with combinatorics and filtering
def compute_rank_value(entries):
    total_pairs = 0
    valid_triplets = 0

    # Real logic: count specific modular arithmetic patterns
    for pair in combinations(entries, 2):
        if (pair[0] * pair[1]) % 7 == 0:
            total_pairs += 1

    # Semi-relevant but not used directly in final score
    unused_entropy = sum([len(str(x)) for x in entries])

    for triplet in combinations(entries, 3):
        if sum(triplet) % 5 == 0 and all(x > 2 for x in triplet):
            valid_triplets += 1

    # Distractor computation
    dummy_aggregate = list(map(lambda x: x ** 2 - x, entries))
    filtered_dummies = [val for val in dummy_aggregate if val % 3 == 0]

    return total_pairs + 3 * valid_triplets

# Final scoring with conditional scaling
def calculate_final_score(ranks, multiplier):
    base = sum(ranks) * multiplier
    adjustment = 0

    # Nested conditionals for scaling (some paths never taken in this input)
    if len(ranks) > 5:
        adjustment += 10
    elif len(ranks) == 4:
        adjustment += 5
    else:
        adjustment -= 2

    # Extra distraction: simulate unused feature interactions
    interactions = []
    for i in range(len(ranks)):
        for j in range(i+1, len(ranks)):
            interaction = ranks[i] * ranks[j] - abs(i - j)
            if interaction > 5:
                interactions.append(interaction)

    # Unused but computed
    avg_interaction = sum(interactions) / (len(interactions) + 1)

    return int(base + adjustment)

# Main execution
if __name__ == "__main__":
    raw_scores = [8, 12, 5, 21, 16, 4, 9]
    config_thresholds = {'A': 0.6, 'B': 0.3}
    bonus_multiplier = 1.75

    # Step 1: Identify top-performing indices
    top_indices = analyze_engagement(raw_scores, config_thresholds)

    # Step 2: Compute derived rank values using combinatorial logic
    derived_values = [compute_rank_value(raw_scores[:idx+1]) for idx in top_indices]

    # Step 3: Apply final transformation (target statement)
    final_score = calculate_final_score(derived_values, bonus_multiplier)

    print(f"Result: {final_score}")