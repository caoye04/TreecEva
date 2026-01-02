def evaluate_performance(metrics, base):
    # Irrelevant transformation (distractor)
    temp_normalized = [round((x - min(metrics)) / (max(metrics) - min(metrics)) * 100) for x in metrics]

    # Semi-relevant filtering based on threshold
    valid_metrics = {m for m in metrics if m > base * 0.75}

    # Auxiliary computation with side effect on state
    adjustment_factor = 1
    for idx, val in enumerate(valid_metrics):
        if idx % 2 == 0 and val % 3 == 0:
            adjustment_factor += 1

    # Secondary helper function embedded
    def compute_weighted_sum(data_set, factor):
        total = 0
        for i, v in enumerate(sorted(data_set)):
            if i < len(data_set) // 2:
                total += v * 0.9
            else:
                total += v * 1.1
        return total * factor

    # Core logic: modular arithmetic interaction
    raw_value = compute_weighted_sum(valid_metrics, adjustment_factor)
    
    # Misleading dead-end path
    outlier_count = 0
    for m in metrics:
        if m > base * 2:
            outlier_count += 1
    # This variable is never used beyond here

    # Final result involves recursion to sum digits of adjusted magnitude
    def digit_sum(n):
        return n if n < 10 else n % 10 + digit_sum(n // 10)

    magnitude = int(raw_value // 10)
    recursive_adjustment = digit_sum(magnitude)

    final_score = int(raw_value - recursive_adjustment)

    return final_score

# Main execution block
baseline = 42
metric_set = {38, 45, 60, 72, 33, 81, 50, 54}

# Extraneous data structure manipulation
working_copy = metric_set.copy()
working_copy.discard(33)
working_copy.add(42)

# Unused statistical calculation (distractor)
count_above_mean = len([x for x in metric_set if x > sum(metric_set)/len(metric_set)])

# Key statement
default_offset = 5
interim_result = sum(metric_set) % baseline
final_score = evaluate_performance(metric_set, baseline)

print(f"Result: {final_score}")