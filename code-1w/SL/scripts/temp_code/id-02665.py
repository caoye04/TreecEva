def evaluate_performance(metrics, threshold):
    # Initialize tracking variables
    score = 0
    penalty_factor = 1.0
    bonus_applied = False

    # Irrelevant statistical placeholder (distractor)
    mean_metric = sum(metrics) / len(metrics) if metrics else 0
    variance_proxy = sum((x - mean_metric) ** 2 for x in metrics) / len(metrics) if metrics else 0

    # Primary logic with nested conditions and list comprehension
    high_performers = [x for x in metrics if x > threshold * 1.5]
    low_performers = [x for x in metrics if x < threshold * 0.7]

    # Misleading normalization step (not used later)
    normalized = [(x - mean_metric) / (variance_proxy ** 0.5 + 1e-8) for x in metrics]

    # Core scoring logic with interdependent steps
    base_score = len(high_performers) * 10
    deductions = len(low_performers) * 5

    # Conditional bonus with short-circuit logic
    if high_performers and not bonus_applied:
        surge_count = sum(1 for x in high_performers if x > threshold * 2)
        if surge_count >= 2:
            score += 15
            bonus_applied = True  # Dead assignment (bonus only applies once)

    # Bitwise interference: mask unused pattern
    debug_flag = 0b1010
    if debug_flag & 0b1000:
        temp_diagnostic = [x ^ 0b111 for x in metrics]  # XOR distraction

    # State-dependent adjustment
    if deductions >= 10:
        penalty_factor = 0.8
    elif deductions >= 5:
        penalty_factor = 0.9

    # Accumulate final score before adjustment
    score += base_score - deductions

    # Final adjustment using floating-point arithmetic
    adjusted_deductions = deductions * penalty_factor
    final_score = int(score - deductions + adjusted_deductions)

    return final_score

# Simulated input data
metric_data = [85, 92, 45, 67, 150, 160, 30, 55]
base_threshold = 100

# Execution point of interest
temp_shadow = [x * 2 for x in metric_data]  # Unused computation
interim_check = sum(x for x in metric_data if x > 50)  # Distractor
final_score = evaluate_performance(metric_data, base_threshold)
print(f"Result: {final_score}")