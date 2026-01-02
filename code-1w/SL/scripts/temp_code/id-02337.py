def calculate_performance(data):
    # Preprocessing phase with some irrelevant transformations
    normalized = [x * 0.95 for x in data if x > 0]
    offsets = list(map(lambda y: y + 10, [1, 2, 3]))  # Unused computation

    # Core logic: compute weighted performance score
    base_score = sum(normalized)
    bonus_factor = 1.1 if len(normalized) > 5 else 1.05

    # Simulate conditional optimization pass
    adjustments = []
    for i, val in enumerate(normalized):
        if i % 2 == 0:
            adjusted = val * bonus_factor
        else:
            adjusted = val * 0.98  # Minor penalty on odd indices
        adjustments.append(round(adjusted, 3))

    # Secondary validation using zip (partly redundant)
    paired = list(zip(normalized, adjustments))
    variance_check = sum(abs(a - b) for b, a in paired)

    # Dummy filtering with string-based flagging (distractor block)
    status_flags = ['valid' if x >= 5 else 'low' for x in normalized]
    flagged_count = len([f for f in status_flags if 'low' in f])

    # Final aggregation logic
    raw_total = sum(adjustments)
    penalty_deduction = flagged_count * 3.25
    final_score = raw_total - penalty_deduction

    # Dead code path - never executed but adds cognitive load
    if False:
        fallback = sum(data) * 0.5
        final_score = fallback

    return final_score

# Input dataset
benchmark_data = [12, 7, 15, 4, 9, 13, 6]

# Execute main logic
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")