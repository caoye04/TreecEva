from itertools import combinations

def analyze_response_time(rt):
    if rt < 200:
        return 'fast'
    elif rt < 500:
        return 'medium'
    else:
        return 'slow'

def compute_stability_index(seq):
    diffs = [abs(seq[i] - seq[i+1]) for i in range(len(seq)-1)]
    return sum(diffs) / len(diffs) if diffs else 0

def evaluate_consistency(ratings):
    unique_ratings = set(ratings)
    if len(unique_ratings) == 1:
        return 10
    elif len(unique_ratings) <= 3:
        return 5
    else:
        return 0

def generate_feedback_hierarchy(scores):
    mapping = {}
    for idx, score in enumerate(scores):
        if score >= 90:
            mapping[idx] = 'excellent'
        elif score >= 75:
            mapping[idx] = 'good'
        elif score >= 60:
            mapping[idx] = 'average'
        else:
            mapping[idx] = 'poor'
    return mapping

def aggregate_performance(feedback_levels):
    performance_map = {'excellent': 4, 'good': 3, 'average': 2, 'poor': 1}
    base_values = [performance_map[v] for v in feedback_levels.values()]
    
    # Irrelevant combination analysis (distractor)
    combo_count = 0
    for r in range(2, 4):
        combo_count += len(list(combinations(base_values, r)))
    
    adjustment_factor = 1.2 if combo_count > 10 else 0.8
    
    # Real computation path
    raw_avg = sum(base_values) / len(base_values)
    stability = compute_stability_index(base_values)
    consistency_bonus = evaluate_consistency(base_values)
    
    # Multiple intermediate variables (some not used later)
    temp_scaling = raw_avg * adjustment_factor
    outlier_check = [x for x in base_values if x < 2]
    suppression_factor = 0.95 if len(outlier_check) > 1 else 1.0
    
    final_score = (raw_avg + stability / 10) * (consistency_bonus / 5)
    
    # Dead code branch (misleading)
    if False:
        final_score = temp_scaling * suppression_factor
        final_score = round(final_score, 3)
    
    return int(final_score)

# Simulated input data
response_times = [150, 250, 600, 400, 180, 300]
accuracy_scores = [88, 92, 76, 95, 81, 73]

# Intermediate processing with irrelevant tracking
state_log = []
for rt in response_times:
    state_log.append(analyze_response_time(rt))

feedback_levels = generate_feedback_hierarchy(accuracy_scores)

# Key execution point
final_score = aggregate_performance(feedback_levels)

print(f"Result: {final_score}")