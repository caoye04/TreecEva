def calculate_final_score(performances, incentives):
    base_points = 0
    penalty = 0
    temp_multiplier = 1.0
    adjustment_factor = 0.0  # unused red herring

    # Simulate performance evaluation with distractors
    for index, (rank, bonus) in enumerate(zip(performances, incentives)):
        if index % 2 == 0:
            base_points += (rank + 1) * 10
            temp_multiplier *= 1.1
        else:
            base_points -= rank // 2
            if bonus > 5:
                penalty += 2

    # Irrelevant statistical tracking (dead computation)
    avg_rank = sum(performances) / len(performances) if performances else 0
    max_bonus = max(incentives) if incentives else 0
    decay_rate = 0.95 ** len(performances)  # unused

    # Conditional logic with case conversion distraction
    status_flags = ['HIGH', 'MEDIUM', 'LOW']
    normalized_flags = [flag.lower() for flag in status_flags]
    scaling_factor = 1.5 if 'high' in normalized_flags else 1.0

    # Core calculation buried among distractions
    raw_score = base_points - (penalty * 5)
    final_score = int(raw_score * scaling_factor)

    # Extra irrelevant combinatorics
    combinations_count = 0
    for i in range(len(performances)):
        for j in range(i + 1, len(performances)):
            combinations_count += 1  # computed but not used

    return final_score

# Input data
rankings = [3, 7, 2, 8, 1]
bonuses = [6, 4, 8, 3, 9]

# Dead code path
if False:
    debug_info = {"step": "skipped"}

final_score = calculate_final_score(rankings, bonuses)
print(f"Result: {final_score}")