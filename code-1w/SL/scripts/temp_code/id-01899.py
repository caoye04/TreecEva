def calculate_final_score(records, importance):
    base_scores = {}
    penalties = {}
    bonus_tracker = []

    for idx, (key, value) in enumerate(records.items()):
        temp_score = 0
        if idx % 2 == 0:
            temp_score += value * 1.5
        else:
            temp_score += value * 0.8

        adjustment = 0
        if value > 50:
            adjustment -= 3
        if idx in [1, 3]:
            adjustment += 2

        # Irrelevant tracking
        penalty_log = f"Penalty applied at {idx}: {adjustment}"
        penalties[key] = adjustment

        base_scores[key] = temp_score + adjustment

    # Dummy loop with no impact
    for _ in range(2):
        bonus_tracker.append(1)

    aggregate = 0.0
    total_weight = 0.0

    # Use of zip and dictionary ops
    keys_sorted = sorted(base_scores.keys())
    values_sorted = [base_scores[k] for k in keys_sorted]
    weighted_values = [v * importance[k] for k, v in base_scores.items()]

    for w_val, weight in zip(weighted_values, importance.values()):
        aggregate += w_val
        total_weight += weight

    normalized = aggregate / total_weight if total_weight != 0 else 0

    outlier_check = [v for v in base_scores.values() if v > 60]
    correction_factor = 0.95 if len(outlier_check) > 1 else 1.0

    # Final computation
    final_score = normalized * correction_factor

    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Input data
data = {'alpha': 40, 'beta': 70, 'gamma': 30, 'delta': 80}
weights = {'alpha': 0.2, 'beta': 0.5, 'gamma': 0.1, 'delta': 0.2}

# Execution
final_score = calculate_final_score(data, weights)