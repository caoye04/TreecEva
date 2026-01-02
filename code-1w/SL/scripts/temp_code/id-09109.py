from collections import defaultdict

# Simulate employee performance evaluation across multiple metrics
def calculate_normalized(metric_data, base_factor):
    normalized = {}
    total = sum(metric_data.values())
    for k, v in metric_data.items():
        normalized[k] = (v / total) * base_factor if total > 0 else 0
    return normalized

def apply_bonus_rules(scores, threshold=75):
    boosted = {}
    bonus_applied = 0
    for metric, score in scores.items():
        if score >= threshold:
            boosted[metric] = score * 1.1
            bonus_applied += 1
        else:
            boosted[metric] = score * 0.95
    # Distractor: track bonus count but not used later
    meta_info = {'bonus_count': bonus_applied, 'version': '2.1'}
    return boosted

def recursive_adjust(values, depth):
    if depth == 0 or not values:
        return values
    adjusted = {k: v * (0.98 + depth * 0.01) for k, v in values.items()}
    return recursive_adjust(adjusted, depth - 1)

def evaluate_performance(weights, scores):
    # Step 1: Normalize weights
    norm_weights = calculate_normalized(weights, 100)
    
    # Step 2: Normalize raw scores to weight scale
    norm_scores = calculate_normalized(scores, 100)
    
    # Step 3: Apply conditional bonus logic
    enhanced_scores = apply_bonus_rules(norm_scores, threshold=70)
    
    # Step 4: Recursive smoothing over 2 levels (distractor depth)
    smoothed = recursive_adjust(enhanced_scores, depth=2)
    
    # Step 5: Weighted aggregation
    weighted_sum = 0.0
    weight_total = 0.0
    for metric in norm_weights:
        if metric in smoothed:
            weighted_sum += norm_weights[metric] * smoothed[metric]
            weight_total += norm_weights[metric]
    
    # Step 6: Final scaling with arbitrary constant (industry adjustment)
    final_raw = weighted_sum / weight_total if weight_total > 0 else 0
    
    # Irrelevant intermediate calculations (distractors)
    outlier_check = [v for v in smoothed.values() if v < 10]
    avg_outlier_gap = sum(outlier_check) / len(outlier_check) if outlier_check else 0
    calibration_shift = avg_outlier_gap * 0.05  # Not used
    
    # Final scoring with fixed transformation
    final_score = int((final_raw + 5) * 1.05)
    
    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Input data
metric_weights = {'productivity': 30, 'accuracy': 25, 'timeliness': 20, 'collaboration': 15, 'innovation': 10}
raw_scores = {'productivity': 85, 'accuracy': 90, 'timeliness': 75, 'collaboration': 80, 'innovation': 70}

# Execution point of interest
final_score = evaluate_performance(metric_weights, raw_scores)