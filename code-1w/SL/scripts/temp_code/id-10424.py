def calculate_final_score(records, importance):
    total = 0
    bonus_tracker = []
    penalty_magnitude = 0

    # Irrelevant pre-processing: analyzing record lengths (distractor)
    record_lengths = [len(str(r)) for r in records]
    avg_length = sum(record_lengths) / len(record_lengths)

    # Real logic begins: enumerate with conditional weighting
    for i, value in enumerate(records):
        weight = importance[i % len(importance)]
        contribution = value * weight

        # Apply dynamic adjustment using lambda (relevant)
        adjuster = lambda x, idx: x * 1.1 if idx % 2 == 0 else x * 0.95
        adjusted = adjuster(contribution, i)

        # Accumulate only even-index contributions to total
        if i % 2 == 0:
            total += adjusted

        # Tracking bonuses (semi-relevant but not used directly)
        if value > 50:
            bonus_tracker.append(contribution * 0.1)

        # Simulated penalty logic (never actually applied)
        if contribution < 20:
            penalty_magnitude += 5  # Dead-end computation

    # Secondary processing: zipping indices and values (mix of relevant/irrelevant)
    indexed_data = list(zip(range(len(records)), records))
    filtered_indices = [idx for idx, val in indexed_data if val > 30]

    # Additional distraction: unused set operation
    unique_contributions = set(int(adjuster(v * importance[i % len(importance)], i)) for i, v in enumerate(records))
    unused_set_metric = len(unique_contributions) + sum(unique_contributions) // 100

    # Final score calculation depends only on total and number of high-value records
    high_value_count = len([v for v in records if v > 40])
    final_score = int(total + high_value_count * 1.5)

    return final_score

# Input data
data = [25, 80, 15, 60, 45, 70]
weights = [2, 1.5, 3]

# Execute
temp_var = sum(d ** 2 for d in data)  # Irrelevant computation
intermediate_result = list(map(lambda x: x + 10, weights))  # Unused helper
final_score = calculate_final_score(data, weights)
print(f"Target result: {final_score}")