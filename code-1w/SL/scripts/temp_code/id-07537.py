def analyze_performance_metrics(raw_data):
    # Preprocess raw sensor readings (distractor: not actually used)
    processed = [x * 1.05 for x in raw_data if x > 0]
    outlier_count = len([x for x in processed if x > 95])

    # Core logic begins: rank determination via set operations
    valid_ranks = set(range(1, 26))
    achieved_scores = [88, 92, 76, 94, 85, 70, 98, 82]
    tier_thresholds = {'A': 90, 'B': 80, 'C': 70}

    # Compute high performers using set logic
    high_performers = {i for i, s in enumerate(achieved_scores) if s >= tier_thresholds['A']}
    mid_performers = {i for i, s in enumerate(achieved_scores) if tier_thresholds['B'] <= s < tier_thresholds['A']}
    eligible_ranks = valid_ranks - {len(achieved_scores) + 5, len(achieved_scores) + 6}  # Artificial constraint

    # Assign ranks based on score order (descending)
    sorted_indices = sorted(range(len(achieved_scores)), key=lambda i: achieved_scores[i], reverse=True)
    rank_map = {idx: rank + 1 for rank, idx in enumerate(sorted_indices)}
    rank_set = set(rank_map.values())

    # Performance tier mapping
    performance_tiers = {}
    for i, score in enumerate(achieved_scores):
        if score >= tier_thresholds['A']:
            performance_tiers[i] = 'A'
        elif score >= tier_thresholds['B']:
            performance_tiers[i] = 'B'
        else:
            performance_tiers[i] = 'C'

    # Distractor computation: stability index (not used in final result)
    moving_avg = sum(achieved_scores[-3:]) / 3
    volatility = max(achieved_scores) - min(achieved_scores)
    stability_index = moving_avg / (volatility + 1e-5)

    # Final score calculation depends only on rank_set and performance_tiers
    return rank_set, performance_tiers


def calculate_final_score(ranks, tiers):
    # Use set properties
    max_rank = max(ranks)
    min_rank = min(ranks)
    rank_span = max_rank - min_rank

    # Count tier distribution
    tier_counts = {k: 0 for k in 'ABC'}
    for t in tiers.values():
        if t in tier_counts:
            tier_counts[t] += 1

    # Irrelevant transformation (dead code path)
    temp_weights = []
    for i in range(3):
        if i == 0:
            temp_weights.append(1.0)
        elif i == 1:
            temp_weights.append(0.5)  # Never actually used

    # Actual scoring logic
    base_score = 50
    rank_bonus = 100 // (min_rank + 1)
    tier_bonus = 5 * tier_counts['A'] + 2 * tier_counts['B']
    span_penalty = rank_span * 2

    # Final formula
    intermediate = base_score + rank_bonus + tier_bonus - span_penalty
    adjustment = 1 if len(ranks & {1, 2, 3}) else 0  # Bonus if top 3 ranks present
    final_score = intermediate + adjustment

    return final_score

# Main execution flow
raw_input_data = [85, 76, 90, 64, 92, 88, 73]  # Unused in final logic but part of preprocessing
rank_set, performance_tiers = analyze_performance_metrics(raw_input_data)
final_score = calculate_final_score(rank_set, performance_tiers)
print(f"Target result: {final_score}")