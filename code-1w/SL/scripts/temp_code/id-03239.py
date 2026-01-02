from collections import defaultdict

# Simulate student assessment scoring with weighted criteria and noise filtering
def evaluate_performance(records, importance):
    raw_scores = []
    temp_buffer = []
    total_weight = sum(importance.values())
    normalized_weights = {k: v / total_weight for k, v in importance.items()}

    # Irrelevant preprocessing: track category counts (not used later)
    category_count = defaultdict(int)
    for record in records:
        category_count[record['category']] += 1

    scaling_factor = 1.0  # Unused scaling placeholder (distractor)
    adjustment_log = []  # Dead storage for potential adjustments (never used)

    for record in records:
        base = record['score']
        category = record['category']
        
        # Apply non-linear transformation based on effort (irrelevant for final logic)
        effort_modifier = 1 + (record.get('effort', 3) * 0.05)
        adjusted = base * effort_modifier
        
        if base < 50:
            continue  # Filter out failing scores early
        
        weighted_contribution = adjusted * normalized_weights[category]
        raw_scores.append(weighted_contribution)
        
        # Red herring computation: accumulates but unused
        temp_buffer.append(adjusted ** 0.5)

    # Secondary filtering: only keep top 4 contributions
    raw_scores.sort(reverse=True)
    selected = raw_scores[:4]

    # Final aggregation: mean of top weighted contributions
    final_mean = sum(selected) / len(selected) if selected else 0

    # Additional distraction: unused recursive helper
    def smooth(x, depth=0):
        if depth >= 2:
            return x
        return smooth(x * 0.9, depth + 1)

    # Final scoring with fixed offset
    ceiling_limit = 95.0
    if final_mean > ceiling_limit:
        final_mean = ceiling_limit

    final_score = int(round(final_mean))  # Discrete rounding to integer

    return final_score

# Input data
weights = {
    'exam': 4,
    'project': 3,
    'quiz': 2,
    'homework': 1
}

assessments = [
    {'score': 88, 'category': 'exam', 'effort': 4},
    {'score': 76, 'category': 'project', 'effort': 5},
    {'score': 45, 'category': 'quiz'},  # filtered out (failing)
    {'score': 92, 'category': 'exam', 'effort': 3},
    {'score': 81, 'category': 'homework', 'effort': 4},
    {'score': 94, 'category': 'project', 'effort': 2},
    {'score': 73, 'category': 'quiz', 'effort': 3},
    {'score': 89, 'category': 'exam', 'effort': 4}
]

# Execution point
final_score = evaluate_performance(assessments, weights)
print(f"Result: {final_score}")