def calculate_final_score(records, importance):
    total = 0
    bonus_tracker = []
    penalty_accumulator = 0  # unused red herring
    temp_result = 0

    for i, (value, weight) in enumerate(zip(records, importance)):
        if i % 2 == 0:
            temp_result = value * weight + 3
        else:
            temp_result = value * weight - 1

        if temp_result > 50:
            bonus_tracker.append(temp_result * 0.1)

        total += temp_result

    adjustment_factor = 0
    for idx, val in enumerate(bonus_tracker):
        adjustment_factor += val * 0.05  # minor influence but not critical

    secondary_sum = sum([x * 0.01 for x in records])  # irrelevant computation
    metadata_enrichment = [x + 10 for x in importance]  # dead code path

    outlier_count = 0
    for v in records:
        if v > 90:
            outlier_count += 1
            break  # early exit, rarely triggers

    final_score = total + adjustment_factor

    # Additional misleading logic
    if len(importance) > 5:
        final_score -= 2  # never reached due to input size

    return int(final_score)

# Input data
raw_data = [45, 67, 88, 41, 76]
weights = [0.8, 1.2, 0.9, 1.1, 1.0]

result = calculate_final_score(raw_data, weights)
print(f"Result: {result}")