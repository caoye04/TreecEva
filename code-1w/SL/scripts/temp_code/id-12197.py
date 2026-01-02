def analyze_performance(metrics, thresholds):
    # Irrelevant transformation
    temp_data = [x * 1.5 for x in metrics if x > 10]
    adjusted_metrics = [max(0, x - 5) for x in metrics]

    # Distractor: complex but unused calculation
    outlier_count = 0
    for val in adjusted_metrics:
        if val > 30:
            outlier_count += 1
    derived_offset = outlier_count * 2.5

    # Real logic begins: filter and categorize
    passing = set()
    marginal = set()
    for i, val in enumerate(adjusted_metrics):
        if val >= thresholds['pass']:
            passing.add(i)
        elif val >= thresholds['marginal']:
            marginal.add(i)

    # Compute overlap between marginal and passing (semi-relevant)
    overlap = len(passing & marginal)

    # Actual score components
    base_score = sum(adjusted_metrics)
    bonus = len(passing) * 5
    penalty = len(set(range(len(metrics))) - passing) * 2

    # More distractors
    avg_metric = sum(temp_data) / len(temp_data) if temp_data else 0
    dummy_flag = avg_metric > 20

    # Nested logic with tuple unpacking
    modifiers = (bonus, penalty, derived_offset, overlap)
    adjustment_factor = 1.0
    if modifiers[0] > 20:
        if modifiers[1] < 10:
            adjustment_factor = 1.2
        else:
            adjustment_factor = 0.9
    else:
        adjustment_factor = 0.8

    intermediate_score = (base_score + bonus - penalty) * adjustment_factor

    # Final normalization using min/max logic
    cap_limit = max(100, base_score // 2)
    final_score = min(intermediate_score, cap_limit)

    return int(final_score)

# Main execution
metrics_data = [23, 15, 34, 8, 12, 45, 29, 6]
thresh_levels = {'pass': 20, 'marginal': 10}

# Unused helper — dead code path
def validate_input(data):
    return all(isinstance(x, int) for x in data)

# Unused variables
buffer_cache = []
scaling_factor = 3.1415
status_flags = {'initialized': True, 'validated': False}

result_code = analyze_performance(metrics_data, thresh_levels)
final_score = result_code
print(f"Result: {final_score}")