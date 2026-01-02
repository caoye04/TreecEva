from collections import defaultdict

# Simulate user feedback analysis across multiple benchmark tiers
def analyze_feedback(raw_logs):
    log_counter = defaultdict(int)
    temporal_weights = [1.0, 0.9, 0.8, 0.7, 0.6]
    irrelevant_sum = 0

    for entry in raw_logs:
        category = entry['type']
        severity = entry['level']
        log_counter[category] += severity * 1.5

    # Distraction: unused computation on timing decay
    for i in range(len(temporal_weights)):
        irrelevant_sum += temporal_weights[i] ** 2

    return dict(log_counter)

# Process hierarchical benchmark results
def process_benchmarks(levels):
    base_multipliers = {1: 2, 2: 3, 3: 4}
    total_power = 0
    level_bonus = 0

    for lvl in levels:
        if lvl in base_multipliers:
            total_power += base_multipliers[lvl] ** 2
            level_bonus += lvl * 0.5  # Unused downstream

    adjusted_power = total_power * 1.1
    return adjusted_power

# Core evaluation logic
def evaluate_performance(feedback, benchmarks):
    base_score = 0
    penalty_factor = 0.85
    noise_accumulator = 0

    # Relevant scoring from feedback categories
    for key in feedback:
        if 'critical' in key:
            base_score += feedback[key] * 2
        elif 'warning' in key:
            base_score += feedback[key] * 1.5
        else:
            base_score += feedback[key]

    # Additional relevant adjustment from benchmark structure
    benchmark_modifier = process_benchmarks(benchmarks)

    # Irrelevant distraction: simulate logging overhead
    for _ in range(3):
        noise_accumulator += len('overhead')

    final_score = (base_score * penalty_factor) + (benchmark_modifier / 10)
    return int(final_score)

# Input data setup
feedback_data = [
    {'type': 'critical_error', 'level': 4},
    {'type': 'warning_log', 'level': 3},
    {'type': 'info_message', 'level': 5},
    {'type': 'critical_timeout', 'level': 6}
]

benchmark_levels = [1, 2, 2, 3]

# Execute analysis pipeline
feedback_counts = analyze_feedback(feedback_data)
processed_levels = benchmark_levels  # Redundant assignment for distraction
final_score = evaluate_performance(feedback_counts, benchmark_levels)

print(f"Result: {final_score}")