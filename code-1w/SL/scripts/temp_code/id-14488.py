def calculate_final_score(ranks, weight_map):
    base_score = 0
    penalty_adjustment = 0
    bonus_tracker = []
    temp_result = []

    # Irrelevant string processing (distractor)
    status_messages = ['valid', 'ignored', 'valid', 'skipped', 'valid']
    for i, msg in enumerate(status_messages):
        if 'skip' in msg:
            continue
        processed = msg.upper().replace('I', '1')
        temp_result.append(len(processed))

    # Real computation begins: weighted rank scoring with modular arithmetic
    sorted_ranks = sorted(ranks)
    normalized_weights = [w / sum(weight_map.values()) for w in weight_map.values()]

    for idx, (rank_val, norm_weight) in enumerate(zip(sorted_ranks, normalized_weights)):
        weighted_contribution = rank_val * norm_weight
        if idx % 2 == 0:
            base_score += weighted_contribution * 1.5
        else:
            base_score += weighted_contribution

    # Spurious loop with no effect on final result (dead code path)
    outlier_count = 0
    for val in ranks:
        deviation = abs(val - sum(ranks) / len(ranks))
        if deviation > 10:
            outlier_count += 1
    if outlier_count > 5:
        penalty_adjustment -= 5

    # Bonus logic using string method on numeric strings (semi-relevant distraction)
    str_codes = ['A1', 'B2', 'C3', 'D4']
    for code in str_codes:
        if code.endswith('2') or code.startswith('C'):
            bonus_tracker.append(code.strip('ABCDEF'))

    # Final adjustment using combinatorics-inspired offset
    n = len(ranks)
    k = 3
    combination_estimate = 1
    for i in range(min(k, n - k)):
        combination_estimate *= (n - i)
        combination_estimate //= (i + 1)

    final_score = int(base_score + combination_estimate // 10)
    return final_score

# Main execution context
rankings = [12, 5, 8, 21, 3, 16]
weights = {'w1': 0.2, 'w2': 0.1, 'w3': 0.3, 'w4': 0.15, 'w5': 0.25}

# Additional irrelevant variables and operations
unused_buffer = [0] * 100
for j in range(len(unused_buffer)):
    unused_buffer[j] = j * j % 7

# Key statement
final_score = calculate_final_score(rankings, weights)
print(f"Target result: {final_score}")