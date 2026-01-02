def analyze_performance(logs, importance_weights):
    total_entries = len(logs)
    cumulative = 0
    adjustments = []
    
    # Irrelevant preprocessing: count entry types (distractor)
    type_count = {'minor': 0, 'major': 0}
    for entry in logs:
        if 'fix' in entry[1]:
            type_count['minor'] += 1
        else:
            type_count['major'] += 1
    
    # Real computation begins
    trend_analysis = {}
    for idx, (rating, note) in enumerate(logs):
        weight = importance_weights.get(idx % len(importance_weights), 1.0)
        scaled_rating = rating * weight
        cumulative += scaled_rating
        
        # Track trends per index group (semi-relevant)
        group = idx // 2
        if group not in trend_analysis:
            trend_analysis[group] = []
        trend_analysis[group].append(scaled_rating)
    
    # Compute average with bias correction (core logic)
    base_avg = cumulative / total_entries if total_entries else 0
    
    # Distractor: elaborate trend summary not used later
    trend_summary = {}
    for g, values in trend_analysis.items():
        trend_summary[g] = {
            'count': len(values),
            'first': values[0],
            'deviation': abs(values[0] - base_avg)
        }
    
    # Secondary adjustment based on pattern density (irrelevant but plausible)
    pattern_density = 0
    for i in range(1, len(logs)):
        if logs[i][0] > logs[i-1][0]:
            pattern_density += 1
    
    # Final score depends only on base_avg and fixed bonus
    stability_bonus = 5 if pattern_density > len(logs) / 2 else 0  # minor influence
    final_value = base_avg * 10 + stability_bonus
    
    return int(final_value)

# Main execution
feedback_log = [
    (4, "good progress"),
    (5, "excellent fix"),
    (3, "needs improvement"),
    (4, "on track"),
    (5, "major milestone achieved")
]

weights = {0: 1.2, 1: 0.8, 2: 1.0}

# Dead code path: unused helper (distractor)
def compute_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

# Unused variable (distractor)
last_review_cycle = "Q3_2023"

# Key execution point
final_score = analyze_performance(feedback_log, weights)

# Output result
print(f"Result: {final_score}")