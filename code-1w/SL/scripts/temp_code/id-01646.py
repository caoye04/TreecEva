def analyze_response_time(base_time, load_factor):
    adjusted_time = base_time * (1 + load_factor / 100)
    penalty = 0
    if adjusted_time > 2.0:
        penalty = (adjusted_time - 2.0) * 10
    return adjusted_time, penalty


def evaluate_stress_conditions(responses):
    stress_markers = []
    cumulative_delay = 0.0
    for resp in responses:
        raw_time = resp['time']
        server_load = resp['load']
        _, delay_penalty = analyze_response_time(raw_time, server_load)
        cumulative_delay += delay_penalty
        if delay_penalty > 5.0:
            stress_markers.append(True)
        else:
            stress_markers.append(False)
    
    # Irrelevant aggregation (distractor)
    true_count = sum(1 for x in stress_markers if x)
    false_count = len(stress_markers) - true_count
    stability_ratio = true_count / len(stress_markers) if stress_markers else 0

    # Semi-relevant transformation
    normalized_delay = round(cumulative_delay * 0.85, 3)
    return normalized_delay, stability_ratio


def aggregate_performance(feedback_levels):
    weights = {'critical': 3, 'high': 2, 'medium': 1, 'low': 0}
    total_weight = 0
    score_components = []
    
    for level in feedback_levels:
        if level in weights:
            total_weight += weights[level]
            score_components.append(weights[level])
    
    # Distractor: unused list comprehension
    filtered_levels = [lvl for lvl in feedback_levels if lvl != 'low']
    redundant_sum = sum([x for x in score_components if x > 1])

    # Actual computation path
    adjustment_factor = len(score_components) if len(score_components) > 0 else 1
    base_score = total_weight * 10
    final_score = base_score // adjustment_factor  # Integer division

    # Red herring calculation (not used)
    average_component = sum(score_components) / len(score_components) if score_components else 0
    scaled_score = round(average_component * 15.5, 2)

    return final_score

# Simulated input data
response_logs = [
    {'time': 1.8, 'load': 15},
    {'time': 2.3, 'load': 25},
    {'time': 1.9, 'load': 10},
    {'time': 2.7, 'load': 40},
    {'time': 2.1, 'load': 20}
]

# Extract feedback levels from external logic
_, ratio = evaluate_stress_conditions(response_logs)
feedback_categories = ['high', 'critical', 'medium', 'critical', 'high', 'low']

# Key execution point
final_score = aggregate_performance(feedback_categories)

print(f"Target result: {final_score}")