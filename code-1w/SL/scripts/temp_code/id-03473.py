def analyze_metrics(values):
    temp_results = []
    offset = len(values) // 2
    for i, val in enumerate(values):
        if i % 2 == 0:
            temp_results.append(val ** 2 + offset)
        else:
            temp_results.append(val - offset)
    return temp_results

extra_weights = [1.5, 2.0, 0.8, 3.1]
dummy_lookup = {x: x * 1.1 for x in range(15)}

# Simulate preprocessing pipeline
data_stream = [3, -1, 4, 2, 5]
filtered_data = [x for x in data_stream if x > 0]
processed_data = analyze_metrics(filtered_data)

# Irrelevant transformation chain (distractor)
shadow_buffer = []
for idx, item in enumerate(extra_weights):
    shadow_buffer.append(item ** 1.5)

# Additional misleading calculation
aggregate_noise = sum([dummy_lookup[i] for i in range(5, 10)])
useless_sum = aggregate_noise * 0.1

# Core logic with state tracking and conditional branching
def calculate_ranking(metrics):
    base_rank = 0
    penalty = 0
    for j, metric in enumerate(metrics):
        if j < len(metrics) // 2:
            base_rank += metric * (j + 1)
        else:
            if metric > 10:
                penalty += 2
            base_rank += metric // 2
    # Final adjustment based on condition
    if len(metrics) % 2 == 1:
        base_rank += 5
    return base_rank - penalty

intermediate_check = sum(processed_data) / len(processed_data)
final_score = calculate_ranking(processed_data)
print(f"Result: {final_score}")