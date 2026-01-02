def calculate_final_score(records, importance_weights):
    base_total = 0
    adjustment_factor = 0.0
    temp_sum = 0  # distractor variable
    outlier_count = 0  # semi-relevant for logic but not final answer

    score_log = []
    weighted_items = []

    for i, (key, value) in enumerate(records.items()):
        if value < 0:
            outlier_count += 1
            continue

        weight = importance_weights.get(key, 1)
        contribution = value * weight
        weighted_items.append(contribution)

        if i % 2 == 0:
            adjustment_factor += 0.1  # minor cumulative effect

    # Simulate secondary processing path (partially irrelevant)
    temp_data = [x for x in weighted_items if x > 5]
    temp_avg = sum(temp_data) / len(temp_data) if temp_data else 0

    for idx, item in enumerate(weighted_items):
        if idx < 2 and item > 10:
            base_total += item * 1.1
        else:
            base_total += item

    # Introduce red herring computation
    dummy_calc = 0
    for k in range(3):
        dummy_calc += k ** 2  # completely irrelevant

    # Use of zip to align metadata (real use case)
    indices = list(range(len(weighted_items)))
    for index, item in zip(indices, weighted_items):
        if index == 0:
            base_total -= item * 0.05  # small correction

    # Final adjustment using accumulated factor
    final_value = base_total + (adjustment_factor * 10)

    return int(round(final_value))

# Main execution
raw_data = {'A': 12, 'B': -5, 'C': 8, 'D': 15, 'E': 6}
decay_weights = {'A': 1.2, 'C': 0.9, 'D': 1.1, 'E': 0.8}

intermediate_result = 0
for v in raw_data.values():
    intermediate_result += v // 2  # distractor loop

final_score = calculate_final_score(raw_data, decay_weights)
print(f"Target result: {final_score}")