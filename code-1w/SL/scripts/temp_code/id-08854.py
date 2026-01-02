def analyze_performance(records):
    base_weights = [0.2, 0.3, 0.5]
    adjusted_totals = []
    temp_offset = 0

    for record in records:
        raw_sum = sum(record)
        if raw_sum > 100:
            temp_offset += 10
        weighted_sum = sum(val * weight for val, weight in zip(record, base_weights))
        adjusted_totals.append(weighted_sum + temp_offset)

    return adjusted_totals


def filter_outliers(scores):
    mean_val = sum(scores) / len(scores)
    deviation_threshold = 1.5
    filtered = [s for s in scores if abs(s - mean_val) / mean_val < deviation_threshold]
    return filtered if len(filtered) > 0 else scores


def calculate_ranking(data_list):
    rankings = sorted(data_list, reverse=True)
    rank_map = {val: idx + 1 for idx, val in enumerate(rankings)}
    composite = 0
    for val in data_list:
        composite += val * rank_map[val]
    return int(composite // len(data_list))

# Simulated dataset: [accuracy, latency_bonus, energy_penalty]
data_samples = [
    [85, 12, 5],
    [90, 8, 7],
    [78, 15, 3],
    [94, 6, 9],
    [88, 9, 4]
]

# Irrelevant preprocessing (distractor)
max_vals = [max(col) for col in zip(*data_samples)]
min_vals = [min(col) for col in zip(*data_samples)]
normalized = [[(v - min_vals[i]) / (max_vals[i] - min_vals[i]) for i, v in enumerate(row)] for row in data_samples]

# Actual processing chain
processed_data = analyze_performance(data_samples)
filtered_data = filter_outliers(processed_data)

# Key computational step with distractors around it
intermediate_result = list(map(lambda x: x + 5 if x < 85 else x, processed_data))
shadow_copy = [x for x in processed_data]
dummy_aggregate = sum([x * x for x in shadow_copy]) // len(shadow_copy)

final_score = calculate_ranking(processed_data)

# Misleading secondary calculation (dead path)
candidate_alt = calculate_ranking(filtered_data)
if final_score < 100 and candidate_alt > final_score:
    final_score = candidate_alt * 0.9

print(f"Result: {final_score}")