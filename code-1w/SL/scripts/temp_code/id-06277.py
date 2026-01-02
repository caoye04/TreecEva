def evaluate_performance(metrics, base):
    adjustment_factor = 0.85
    penalty_threshold = base * 1.1
    bonus_threshold = base * 0.9
    
    # Irrelevant statistical tracking (distractor)
    mean_metric = sum(metrics) / len(metrics) if metrics else 0
    variance_proxy = sum((x - mean_metric) ** 2 for x in metrics) / len(metrics) if metrics else 0
    outlier_count = 0
    temp_accum = 0
    
    for val in metrics:
        if val > penalty_threshold:
            outlier_count += 1
        temp_accum += val % 10  # Distraction: unused accumulation

    # Real logic begins: categorize metrics relative to base
    strong_performers = {x for x in metrics if x < bonus_threshold}
    weak_performers = {x for x in metrics if x >= penalty_threshold}
    mid_range = metrics - strong_performers - weak_performers  # Set difference

    # Secondary distraction: spurious normalization
    normalized_sum = 0
    for x in metrics:
        if x != 0:
            normalized_sum += x / abs(x)  # Sign counting, not impactful

    # Core scoring logic
    score = len(strong_performers) * 10
    score -= len(weak_performers) * 5
    
    consistency_bonus = 10 if len(strong_performers) >= 3 else 0
    stability_penalty = 5 if len(weak_performers) >= 2 else 0
    
    final_score = score + consistency_bonus - stability_penalty
    
    # Dead code path (never executed under current logic)
    hypothetical_boost = 0
    if len(mid_range) == 0 and False:  # Always false
        hypothetical_boost = 20
    
    return final_score

# Setup data
baseline = 80
raw_data = {75, 85, 70, 90, 60, 88}
noise_filter = [x for x in raw_data if x % 5 == 0]  # Filtering irrelevantly
metric_set = set(noise_filter)  # Final metric set used

# Execution point of interest
final_score = evaluate_performance(metric_set, baseline)
print(f"Result: {final_score}")