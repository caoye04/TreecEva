from collections import defaultdict

# Simulate user feedback analysis for system performance tuning
def analyze_feedback(reports):
    feedback_counts = defaultdict(int)
    severity_tally = 0
    temp_multiplier = 1

    for report in reports:
        category = report['category']
        severity = report['severity']
        resolved = report['resolved']

        if not resolved and severity > 1:
            feedback_counts[category] += 1
            severity_tally += severity

        # Distractor: irrelevant computation with no effect on final result
        temp_multiplier *= (severity % 3 + 1)

    # Additional noise: unused intermediate calculation
    average_severity = severity_tally / len(reports) if reports else 0
    adjustment_factor = int(average_severity * 2) if average_severity > 0.5 else 1

    return feedback_counts

# Evaluate system performance based on feedback and benchmarks
def evaluate_performance(counts, levels):
    base_score = 0
    penalty = 0
    stage_weights = [0.5, 0.7, 1.0]

    for idx, level in enumerate(levels):
        key = f"module_{level}"
        frequency = counts.get(key, 0)

        if frequency > 0:
            base_score += frequency * stage_weights[idx]
            if frequency >= 3:
                penalty += 2

    # Complex but partially redundant logic
    if base_score > 10:
        base_score = base_score * 0.9
    elif base_score > 5:
        base_score = base_score * 0.95

    # Final adjustment
    final_value = int(base_score - penalty)

    # Dead code path - never executed due to logic above
    if final_value < 0 and False:
        final_value = 0

    return final_value

# Input data
bug_reports = [
    {'category': 'module_2', 'severity': 2, 'resolved': False},
    {'category': 'module_3', 'severity': 3, 'resolved': False},
    {'category': 'module_3', 'severity': 2, 'resolved': False},
    {'category': 'module_3', 'severity': 3, 'resolved': False},
    {'category': 'module_1', 'severity': 1, 'resolved': True},
    {'category': 'module_2', 'severity': 3, 'resolved': False},
    {'category': 'module_2', 'severity': 2, 'resolved': False},
    {'category': 'module_3', 'severity': 3, 'resolved': False}
]

benchmark_levels = [1, 2, 3]

# Step 1: Process feedback
feedback_counts = analyze_feedback(bug_reports)

# Step 2: Compute performance score
final_score = evaluate_performance(feedback_counts, benchmark_levels)

# Output result
print(f"Result: {final_score}")