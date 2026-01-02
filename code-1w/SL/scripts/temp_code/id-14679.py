def analyze_efficiency(workload, thresholds):
    # Irrelevant transformation
    temp_analysis = {x: (x ** 2 + 3) // 2 for x in workload if x > 5}
    adjusted = [val for val in workload if val % 2 == 0]
    cumulative = sum(adjusted)
    
    # Distractor: complex but unused logic with sets
    valid_points = {i for i in range(len(workload)) if workload[i] >= thresholds.get('min', 0)}
    outlier_indices = {i for i in range(len(workload)) if workload[i] > thresholds.get('max', 100)}
    filtered_indices = valid_points - outlier_indices
    
    # Dead code path (never executed due to condition)
    secondary_score = 0
    if len(outlier_indices) > 100:
        backup_weights = [0.1 * x for x in adjusted[::-1]]
        secondary_score = sum(backup_weights) // len(backup_weights)

    # Real computation buried in noise
    efficiency_ratio = len(filtered_indices) / len(workload) if workload else 0
    return efficiency_ratio


def compute_stability(data_stream):
    # Unrelated stability metric (distractor)
    mean_val = sum(data_stream) / len(data_stream)
    variance = sum((x - mean_val) ** 2 for x in data_stream) / len(data_stream)
    return variance < 15

# Unused helper function (decoy)
def normalize_input(seq):
    max_val = max(seq)
    return [x / max_val for x in seq]

# Simulated sensor readings and baselines
current_readings = [12, 15, 8, 22, 19, 6, 31, 14, 25, 18]
baseline_metrics = {
    'min': 10,
    'max': 30,
    'target': 20
}

# Fake feature extraction (irrelevant)
feature_vector = []
for i, val in enumerate(current_readings):
    if val > baseline_metrics['target']:
        feature_vector.append(i * val % 7)

# Create dummy sets for set operations (some relevant, some not)
high_performers = {x for x in current_readings if x >= baseline_metrics['min']}
low_outliers = {x for x in current_readings if x < 10}
acceptable_range = set(range(baseline_metrics['min'], baseline_metrics['max']))
overlap_region = high_performers & acceptable_range  # Actually used later

# Simulate feedback from multiple sources (mix of real and fake)
feedback_raw = [14, 18, 22, 9, 30, 11, 25]
feedback_set = set(feedback_raw)

def evaluate_performance(feedback, baseline):
    # Core logic hidden among distractions
    base_threshold = baseline['min']
    cap_limit = baseline['max']
    
    # Distractor: unused nested comprehension
    _ = [[x * y for y in feedback if y < cap_limit] for x in feedback if x > base_threshold]
    
    # Actual signal: count how many feedback points are in acceptable overlap
    consensus = feedback & overlap_region  # Key intersection
    alignment_bonus = len(consensus) * 2
    
    # Additional logic using arithmetic and boolean mix
    base_efficiency = analyze_efficiency(current_readings, baseline)
    stability_flag = compute_stability(current_readings)
    
    # Final calculation chain
    raw_score = int(base_efficiency * 100) + alignment_bonus
    if stability_flag:
        raw_score += 5
    
    # Red herring: complex but unused bitwise op
    masked_score = raw_score ^ 0xFF & 0x3F | 0x10
    
    # Final adjustment based on logical condition
    final_modifier = 10 if len(consensus) >= 3 else -7
    final_score = raw_score + final_modifier
    
    # Critical output
    return final_score

# Execution point of interest
final_score = evaluate_performance(feedback_set, baseline_metrics)
print(f"Target result: {final_score}")