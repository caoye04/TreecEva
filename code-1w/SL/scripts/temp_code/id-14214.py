def evaluate_performance(records, importance):
    base = 0
    bonus = 0
    penalty = 0
    temp_result = []

    # Irrelevant pre-processing: case conversion and string manipulation
    normalized_keys = list(map(lambda x: x.upper().strip(), records.keys()))
    key_length_sum = sum(len(k) for k in normalized_keys)

    # Distractor: unused recursive function
    def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

    ignored_sequence = [fibonacci(i) for i in range(5)]  # dead computation

    # Actual logic begins
    for idx, (key, value) in enumerate(records.items()):
        if 'error' in key.lower():
            penalty += value * importance['penalty_factor']
        elif 'success' in key.lower():
            base += value
            if value > 50:
                bonus += importance['bonus_rate'] * value

    # Linear search for a threshold (semi-relevant)
    thresholds = [30, 60, 90]
    level = 0
    for t in thresholds:
        if base > t:
            level += 1

    # Bonus scaling based on performance level
    scaled_bonus = bonus * (1 + level * 0.1)

    # Irrelevant string accumulation
    log_trace = ''
    for i in range(min(len(normalized_keys), 3)):
        log_trace += f"{normalized_keys[i][0]}"

    # Final score calculation
    final_score = base + scaled_bonus - penalty

    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Input data
data = {
    'success_rate_1': 75,
    'error_count_initial': 10,
    'success_rate_2': 85,
    'extra_metric': 42,  # not used
    'error_count_final': 5
}

weights = {
    'bonus_rate': 0.2,
    'penalty_factor': 1.5
}

# Execution point
final_score = evaluate_performance(data, weights)