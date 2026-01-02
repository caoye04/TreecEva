def calculate_final_score(items, importance_weights):
    base_score = 0
    adjustment_factor = 0.0
    temp_buffer = []
    cumulative_shift = 0

    for idx, (item, weight) in enumerate(zip(items, importance_weights)):
        raw_value = item * weight
        if idx % 2 == 0:
            base_score += raw_value * 1.1
        else:
            base_score -= raw_value * 0.9

        # Irrelevant computation - distractor
        squared_deviation = (item - weight) ** 2
        temp_buffer.append(squared_deviation)

    # Dummy loop - dead code path but looks meaningful
    for _ in range(3):
        adjustment_factor += 0.01
        adjustment_factor = round(adjustment_factor, 2)

    # Another irrelevant accumulator
    total_pairs = 0
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            total_pairs += 1

    # Actual logic: apply fixed correction based on length parity
    if len(items) % 2 == 1:
        cumulative_shift = 5
    else:
        cumulative_shift = -3

    final_score = base_score + cumulative_shift

    return final_score

# Main data
values = [12, 8, 15, 20]
weights = [0.5, 1.0, 0.8, 1.2]

# Misleading pre-computations
sum_check = sum(values) * 0.1
duplicate_data = [x * 2 for x in values if x > 10]

result = calculate_final_score(values, weights)
Result: {result}