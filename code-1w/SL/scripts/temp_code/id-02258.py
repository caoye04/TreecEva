def evaluate_performance(data, config):
    base = sum(d * c for d, c in zip(data, config))
    adjustment = 0
    
    if base > 100:
        adjustment = -10
    elif base < 50:
        adjustment = 5
    else:
        adjustment = 2

    # Irrelevant tracking variables (distractors)
    temp_history = [base]
    temp_history.append(base * 0.1)
    temp_history.append(sum(temp_history))

    scaling_factor = 1.0
    for i in range(3):
        scaling_factor *= 0.95  # Minor decay, not used in final logic

    # Unused computation path
    derived_metrics = [x ** 0.5 for x in data if x > 10]
    outlier_count = len([x for x in data if x > 90])

    # Actual result calculation
    raw_score = base + adjustment
    bonus = 3 if outlier_count > 1 else 0
    final = raw_score + bonus

    # Dead code branch (never executed due to fixed condition)
    if False:
        fallback = sum(data) // len(data)
        final = fallback

    return final

# Main execution
metrics = [85, 72, 91, 45, 60]
weights = [0.2, 0.3, 0.1, 0.25, 0.15]

# Preprocessing step with slicing (relevant)
data_slice = metrics[1:4]
processed = list(map(lambda x: x + 5 if x < 50 else x, metrics))

# Dummy recursive function (distractor)
def dummy_accumulate(lst, idx=0):
    if idx >= len(lst):
        return 0
    return lst[idx] * 0.01 + dummy_accumulate(lst, idx + 1)

_ = dummy_accumulate(metrics)

final_score = evaluate_performance(metrics, weights)
print(f"Target result: {final_score}")