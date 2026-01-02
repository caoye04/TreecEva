from collections import defaultdict, Counter

# Simulate user feedback analytics across multiple platform benchmarks
def analyze_feedback_patterns(raw_logs):
    feedback_counts = defaultdict(int)
    temporal_trend = []
    auxiliary_sum = 0

    for log in raw_logs:
        action = log['action']
        category = log['category']
        timestamp = log['timestamp']

        if action == 'submit' and category in ['usability', 'performance', 'security']:
            feedback_counts[category] += 1
            temporal_trend.append(timestamp)

        # Irrelevant processing - distractor (dead logic path)
        elif action == 'view':
            auxiliary_sum += len(category)

    return feedback_counts, temporal_trend

# Evaluate system performance based on feedback distribution
def evaluate_performance(counts, levels):
    base_weights = {'usability': 3, 'performance': 5, 'security': 8}
    score_components = []

    for cat, count in counts.items():
        weighted_val = base_weights.get(cat, 1) * count
        score_components.append(weighted_val)

    total_raw_score = sum(score_components)
    adjustment_factor = len(score_components) if len(score_components) > 1 else 1

    # Complex but partially irrelevant transformation
    transformed_vals = [val ** 0.5 for val in score_components if val > 4]
    decay_correction = sum(transformed_vals) / (len(transformed_vals) or 1) if transformed_vals else 0

    # Final scoring with minor correction
    final_score = int((total_raw_score / adjustment_factor) + decay_correction)
    return final_score

# Generate synthetic benchmark levels
benchmark_levels = [i**2 for i in range(1, 6)]

# Simulated logs with mixed actions and categories
raw_interaction_logs = [
    {'action': 'submit', 'category': 'usability', 'timestamp': 1001},
    {'action': 'submit', 'category': 'performance', 'timestamp': 1002},
    {'action': 'submit', 'category': 'security', 'timestamp': 1003},
    {'action': 'submit', 'category': 'usability', 'timestamp': 1004},
    {'action': 'submit', 'category': 'performance', 'timestamp': 1005},
    {'action': 'submit', 'category': 'security', 'timestamp': 1006},
    {'action': 'submit', 'category': 'security', 'timestamp': 1007},
    {'action': 'view', 'category': 'docs', 'timestamp': 1008},
    {'action': 'view', 'category': 'faq', 'timestamp': 1009},
    {'action': 'submit', 'category': 'usability', 'timestamp': 1010}
]

# Extract meaningful feedback data
feedback_data, trend_sequence = analyze_feedback_patterns(raw_interaction_logs)

# Compute performance metric
final_score = evaluate_performance(feedback_data, benchmark_levels)

# Print result as required
print(f"Result: {final_score}")