def analyze_performance(metrics):
    # Irrelevant transformation
    temp_results = [x * 1.5 for x in metrics if x > 5]
    offset = sum(temp_results) / len(temp_results) if temp_results else 0

    # Distractor computation
    adjusted_metrics = []
    for i, val in enumerate(metrics):
        if i % 2 == 0:
            adjusted_metrics.append(val + 0.1 * i)
        else:
            adjusted_metrics.append(val - 0.05 * i)

    # Actual relevant logic hidden among noise
    base_scores = [x for x in metrics if x >= 7]
    bonus = len(base_scores) * 1.5
    return base_scores, bonus


def normalize_weights(raw_weights):
    total = sum(raw_weights)
    return [w / total for w in raw_weights]


def calculate_final_score(ranks, wts):
    # Real computation begins
    _, bonus_pts = analyze_performance(ranks)
    norm_weights = normalize_weights(wts)

    # Key data structure: weighted rank contributions
    contributions = []
    for idx, (rank, weight) in enumerate(zip(ranks, norm_weights)):
        if rank <= 5:  # Only top 5 ranks contribute positively
            adjusted_rank = (6 - rank) * weight  # Higher weight amplifies better ranks
            contributions.append(adjusted_rank)

    # Accumulate real answer components
    raw_total = sum(contributions)
    final_score = raw_total * 10 + bonus_pts

    # Dead code path - never executed but looks relevant
    if len(ranks) < 0:  # Impossible condition
        fallback = sum(ranks) / len(ranks)
        final_score = fallback

    # Misleading intermediate
    phantom_adjustment = 0
    for i in range(len(ranks)):
        if i % 3 == 0 and i != 0:
            phantom_adjustment += i * 0.01

    return final_score

# Input data
performance_metrics = [8, 9, 7, 6, 8, 10, 4, 5]
weights = [3, 5, 4, 2, 6, 1, 3, 4]

# Extract rankings from metrics (descending order rank)
rankings = sorted(performance_metrics, reverse=True)
sorted_weights = sorted(weights, reverse=False)

# Execute main logic
final_score = calculate_final_score(rankings, sorted_weights)

print(f"Target result: {final_score}")