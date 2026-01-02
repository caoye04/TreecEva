def aggregate_performance(ranks, metrics):
    # Irrelevant transformation: unused in final result
    dummy_transform = list(map(lambda x: (x[0], x[1] ** 2 + 1), ranks))

    # Misleading intermediate: looks important but not used
    shadow_score = sum([v for k, v in ranks if k % 2 == 0]) * 0.5

    # Core logic begins: extract top performers
    filtered_ranks = [v for k, v in ranks if v > 75]
    rank_set = set(filtered_ranks)

    # Additional distraction: complex but irrelevant set operation
    auxiliary_set = set(range(50, 100, 3))
    overlap = rank_set & auxiliary_set  # Used nowhere

    # Real computation starts: weighted combination
    base_val = metrics['throughput'] // 10  # Integer division
    bonus = len(filtered_ranks) * 3

    # Multiple assignments to increase cognitive load
    adjustment = 0
    if len(filtered_ranks) >= 3:
        adjustment += 5
    if metrics['latency'] < 120:
        adjustment += 7

    # Tuple unpacking: relevant state update
    scaling_factor, offset = (1.2, 4) if metrics['errors'] == 0 else (0.9, 6)

    # Distractor: dead code path due to fixed input
    temp_debug = None
    if metrics['errors'] > 100:  # Never true
        temp_debug = [x * 0.1 for x in filtered_ranks]

    # Actual answer derivation
    raw_score = (base_val + bonus + adjustment) * scaling_factor + offset
    final_score = int(round(raw_score))

    return final_score

# Input setup
rankings = [(1, 80), (2, 92), (3, 67), (4, 95), (5, 88)]
base_metrics = {
    'throughput': 420,
    'latency': 110,
    'errors': 0
}

# Execution point
final_score = aggregate_performance(rankings, base_metrics)
print(f"Target result: {final_score}")