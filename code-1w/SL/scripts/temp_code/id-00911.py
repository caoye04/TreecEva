from itertools import combinations

def analyze_sequence(values):
    # Irrelevant computation: generates pairs but not used in final result
    pair_count = len(list(combinations(values, 2)))
    temp_sum = sum(v ** 2 for v in values if v > 0)  # Distractor: not directly used
    adjusted = [v * 1.5 for v in values]
    return sum(adjusted) // len(adjusted) if adjusted else 0

def extract_features(text_block):
    words = text_block.lower().split()
    word_lengths = [len(w) for w in words]
    avg_length = sum(word_lengths) / len(word_lengths)
    exclamation_count = text_block.count('!')  # Dead code path
    return avg_length

def evaluate_performance(metrics, limit):
    base = 0
    penalty = 0
    bonus = 0

    for k, v in metrics.items():
        if isinstance(v, str):
            processed = extract_features(v)
            if processed > 4.0:
                bonus += 2
        elif isinstance(v, (int, float)):
            base += v
            if v < 0:
                penalty += 1

    # Semi-relevant transformation
    normalized_base = max(base - penalty * 3, 0)

    # Key logic step: depends on prior state
    if bonus > 0 and normalized_base > 10:
        normalized_base *= 1.5

    # Secondary distraction: complex conditional expression
    adjustment = (1.2 if normalized_base > 15 else 1.0) if bonus else 0.8

    intermediate = normalized_base * adjustment

    # Final scoring with tuple-based weighting (core concept)
    weights = (0.6, 0.4)
    final_score = int(intermediate * weights[0] + bonus * 10 * weights[1])

    # Irrelevant list processing
    temp_list = [final_score + i for i in range(3)]
    temp_list.reverse()  # Unused operation

    return final_score

# Simulate input data
raw_values = [2, -1, 4, 3]
metric_data = {
    'latency': 12,
    'accuracy': 9,
    'log_output': 'System initialized! Process running smoothly!',
    'retries': -2,
    'status_msg': 'Task completed successfully.'
}
threshold = 5

# Orchestrate execution
avg_val = analyze_sequence(raw_values)
score_snapshot = avg_val * 0.75  # Distractor variable

final_score = evaluate_performance(metric_data, threshold)
print(f"Target result: {final_score}")