def analyze_efficiency(metrics, baseline):
    adjusted_scores = []
    for i, val in enumerate(metrics):
        if i % 2 == 0:
            adjusted_scores.append(val * 0.9)
        else:
            adjusted_scores.append(val * 1.1)
    return [x - baseline for x in adjusted_scores]


def filter_outliers(data, threshold=50):
    # Irrelevant helper function (dead code path)
    return [x for x in data if abs(x) < threshold]


def compute_weighted_average(values, weights):
    total = 0.0
    weight_sum = 0.0
    for v, w in zip(values, weights):
        total += v * w
        weight_sum += w
    if weight_sum == 0:
        return 0.0
    return total / weight_sum

# Simulated system performance data
raw_metrics = [45, 67, 83, 52, 74]
baseline_offset = 10

# Apply efficiency analysis (has side computation)
efficiency_data = analyze_efficiency(raw_metrics, baseline_offset)

# Dummy transformations - irrelevant to final result
shifted_values = [x + 5 for x in raw_metrics if x > 60]
duplicate_check_set = set(raw_metrics)
size_placeholder = len(duplicate_check_set)

# Target metrics and feedback ratings
feedback_ratings = [4.2, 3.8, 4.5, 4.0, 4.7]
target_metrics = [80, 75, 90, 70, 95]

# Misleading intermediate calculation (not used in final answer)
avg_feedback = sum(feedback_ratings) / len(feedback_ratings)
penalty_factor = 0.95 if avg_feedback < 4.0 else 1.0

scaling_map = {i: val * 0.1 for i, val in enumerate(target_metrics)}

# Core logic: evaluate performance using specific criteria
def evaluate_performance(ratings, targets):
    normalized = [r * 10 for r in ratings]  # Scale ratings to match metric range
    differences = []
    for norm, tgt in zip(normalized, targets):
        differences.append(abs(tgt - norm))
    
    # Use dictionary to track deviation categories
    deviation_bins = {'low': 0, 'medium': 0, 'high': 0}
    for diff in differences:
        if diff < 5:
            deviation_bins['low'] += 1
        elif diff < 15:
            deviation_bins['medium'] += 1
        else:
            deviation_bins['high'] += 1
    
    # Compute score based on deviation distribution
    score = 100
    score -= deviation_bins['medium'] * 3
    score -= deviation_bins['high'] * 8
    
    # Additional penalty if any deviation exceeds 20 (short-circuit logic)
    if any(diff > 20 for diff in differences):
        score -= 5
    
    return score

# Execute key statement
temp_adjustment = [x * 0.99 for x in efficiency_data]  # Distractor
final_score = evaluate_performance(feedback_ratings, target_metrics)
print(f"Result: {final_score}")