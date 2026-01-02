def evaluate_performance(data, importance):
    # Initialize various tracking variables
    base_points = 0
    bonus_adjustment = 0
    penalty_tracker = 0
    temp_result = []

    # Irrelevant string processing (uses string methods as required)
    status_labels = ['pass', 'warn', 'fail', 'unknown']
    cleaned_labels = list(map(str.strip, map(str.lower, status_labels)))
    label_filter = lambda x: x in cleaned_labels and x != 'unknown'

    # Core logic begins
    for i, value in enumerate(data):
        weight = importance[i]
        if value >= 80:
            base_points += value * weight * 0.1
            bonus_adjustment += 5 * weight
        elif value < 60:
            penalty_tracker += 10 * weight
        else:
            base_points += value * weight * 0.05

    # Distractor computation: uses bitwise but doesn't affect final result directly
    diagnostic_flag = (len(data) << 2) ^ 7
    debug_mask = diagnostic_flag & 0xF

    # Another red herring: complex-looking but unused calculation
    derived_metrics = [x ** 0.5 for x in data if x > 0]
    normalized = sum(derived_metrics) / len(derived_metrics) if derived_metrics else 0
    auxiliary_score = round(normalized * 2.718) & 255  # Bitwise AND for no real purpose

    # Actual score formation (depends only on earlier tracked values)
    intermediate = base_points + bonus_adjustment - penalty_tracker

    # Final transformation using lambda (required feature)
    scale_factor = lambda x: x * 1.1 if x > 100 else x * 1.2
    adjusted_intermediate = scale_factor(intermediate)

    # One last irrelevant check
    if debug_mask > 5:
        adjusted_intermediate -= 3  # Minor red herring adjustment not affecting core path

    # This is the actual answer variable
    final_score = int(adjusted_intermediate + 0.5)  # Round to nearest integer

    return final_score

# Main execution
metrics = [85, 72, 90, 45, 77]
weights = [0.2, 0.3, 0.1, 0.3, 0.1]

result = evaluate_performance(metrics, weights)
print(f"Result: {result}")