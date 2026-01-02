from collections import defaultdict

# Simulated benchmark data across multiple test categories
test_categories = ['arithmetic', 'logic', 'assignment', 'control_flow']
raw_scores = [88, 76, 92, 81]
execution_times = [1.2, 2.1, 0.9, 1.5]  # in seconds
error_counts = [2, 5, 1, 3]

# Irrelevant normalization (distractor)
normalized_times = [round(1/t, 3) for t in execution_times]

# Weight configuration (some weights are unused)
weights = {
    'accuracy': 0.5,
    'speed': 0.3,
    'stability': 0.2,
    'redundant_metric': 0.1  # not used
}

# Mapping results by category using dictionary and enumerate
benchmark_results = defaultdict(dict)
for idx, category in enumerate(test_categories):
    benchmark_results[category]['score'] = raw_scores[idx]
    benchmark_results[category]['time'] = execution_times[idx]
    benchmark_results[category]['errors'] = error_counts[idx]

# Auxiliary function to compute sub-scores
def calculate_performance(results, weight_map):
    total_weighted_score = 0.0
    speed_bonus = 0
    stability_penalty = 0

    # Intermediate tracking variables (some are red herrings)
    performance_log = []
    max_single_score = 0
    cumulative_delay = 0.0

    for i, (cat, data) in enumerate(results.items()):  
        base_score = data['score']
        response_time = data['time']
        errors = data['errors']

        # Speed bonus logic
        if response_time < 1.0:
            speed_bonus += 5
        elif response_time > 2.0:
            speed_bonus -= 3

        # Stability penalty based on errors
        if errors == 0:
            stability_penalty += 2
        else:
            stability_penalty -= errors * 1.5

        # Weighted component calculation
        accuracy_component = base_score * weight_map['accuracy']
        speed_component = (100 / response_time) * weight_map['speed']
        stability_component = (10 - errors * 2) * weight_map['stability']

        # Aggregate score for category
        category_total = accuracy_component + speed_component + stability_component

        # Track logs (not used in final result)
        performance_log.append(f"{cat}: {category_total:.2f}")

        if category_total > max_single_score:
            max_single_score = category_total

        cumulative_delay += response_time

    # Final weighted aggregation (only this affects output)
    total_weighted_score = sum(
        (item['score'] * weight_map['accuracy'] + 
         (100 / item['time']) * weight_map['speed'] + 
         (10 - item['errors'] * 2) * weight_map['stability'])
        for item in results.values()
    )

    # Dead code: these variables are computed but not used in return
    average_delay = cumulative_delay / len(results)
    peak_bonus = max_single_score * 0.1 if max_single_score > 90 else 0

    final_raw = total_weighted_score + speed_bonus + stability_penalty
    return round(final_raw, 2)

# Misleading pre-computation (distractor)
avg_error_rate = sum(error_counts) / len(error_counts)
temp_weights = [w for w in weights.values()]

# Key execution point
final_score = calculate_performance(benchmark_results, weights)

# Additional irrelevant transformation
adjusted_final = final_score * 0.95 if avg_error_rate < 3 else final_score * 1.05

# Print target result
Result: {final_score}