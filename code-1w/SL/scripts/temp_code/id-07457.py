def evaluate_performance(data, importance):
    temp_result = 0
    base_adjustment = 0.1
    scaling_factor = len(data) + 2
    offset_tracker = [i * 0.5 for i in range(len(data))]
    
    # Irrelevant pre-processing (distractor)
    normalized = []
    total = sum(data)
    for val in data:
        normalized.append((val / total) * 100 if total != 0 else 0)
    
    # Real computation masked by noise
    weighted_sum = 0
    for i in range(len(data)):
        contribution = data[i] * importance[i]
        if contribution > 5:  # Threshold filter
            weighted_sum += contribution * base_adjustment
        else:
            weighted_sum -= contribution * 0.1
    
    # Dummy loop with no effect (dead code path)
    temp_value = 0
    for x in offset_tracker:
        temp_value += x ** 2
        if temp_value > 100:
            break  # Unreachable under current inputs

    # Slicing distraction
    slice_window = offset_tracker[1:4]
    slice_effect = sum(slice_window) * 0.05

    # Actual logic buried in middle
    adjustment = 0
    for w in importance:
        if w >= 0.3:
            adjustment += 1.5
    
    final_score = weighted_sum + adjustment + slice_effect
    
    # Unused variables to increase cognitive load
    consistency_check = all(m >= 0.2 for m in importance)
    peak_metric = max(data)
    decay_rate = 0.95

    return int(final_score)

# Input setup
metrics = [8, 6, 7, 5, 3]
weights = [0.4, 0.5, 0.3, 0.6, 0.2]

# Execution point of interest
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")