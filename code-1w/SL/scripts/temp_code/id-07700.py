def analyze_performance(metrics):
    base_score = sum([m['value'] for m in metrics if m['active']])
    adjustments = 0
    temp_log = []
    for i, m in enumerate(metrics):
        if m['type'] == 'speed' and m['value'] > 80:
            adjustments += 5
            temp_log.append(f"Speed bonus at index {i}")
        elif m['type'] == 'accuracy' and m['value'] < 50:
            adjustments -= 10
            temp_log.append(f"Accuracy penalty at index {i}")
    return base_score, adjustments


def validate_ranks(ranks):
    sorted_ranks = sorted(ranks)
    median_rank = sorted_ranks[len(sorted_ranks) // 2]
    outlier_count = len([r for r in ranks if r > 90])
    dummy_calc = sum([x * 2 for x in ranks]) / (len(ranks) or 1)
    return median_rank, outlier_count


def compute_final_score(ranks, flags):
    rank_sum = sum(ranks)
    flag_bonus = 10 if any(flags) else 0
    
    # Simulate historical average adjustment (distractor)
    historical_avg = 74.3
    projected_growth = (rank_sum / len(ranks)) * 0.12 if rank_sum > 200 else 0
    growth_buffer = projected_growth * 0.5  # Unused distraction

    base, adj = analyze_performance([
        {'value': rank_sum, 'active': True, 'type': 'speed'},
        {'value': len(ranks), 'active': True, 'type': 'accuracy'},
        {'value': flag_bonus, 'active': False, 'type': 'bonus'}
    ])
    
    median_rank, outliers = validate_ranks(ranks)
    
    # Intermediate distractors
    normalization_factor = 100 / (median_rank or 1)
    temp_result = (base + adj) * normalization_factor
    unused_metric = temp_result % 7  # Dead-end variable

    final_score = base + adj + flag_bonus - outliers
    
    # Irrelevant filtering
    valid_metrics = {f'metric_{i}': v for i, v in enumerate([base, adj, flag_bonus]) if v != 0}
    return int(final_score)

# Input data
rank_data = [85, 72, 91, 64, 77]
bonus_flags = [False, True, False]

final_score = compute_final_score(rank_data, bonus_flags)
print(f"Result: {final_score}")