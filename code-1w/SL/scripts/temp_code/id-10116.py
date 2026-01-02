from itertools import cycle

# Simulate sensor data processing pipeline with weighted scoring
def evaluate_performance(metrics, weights):
    base_score = 0
    adjustment_factor = 0.85
    temp_buffer = []
    
    # Irrelevant pre-processing: normalize metrics (not used in final logic)
    normalized = [m / max(metrics) for m in metrics]
    scaling_constant = sum(normalized) * 0.1
    
    # Real logic begins: weighted sum with conditional boosts
    boosted_weights = []
    for i, w in enumerate(weights):
        if metrics[i] > 90:
            boosted_weights.append(w * 1.2)
        elif metrics[i] < 50:
            boosted_weights.append(w * 0.7)  # Penalty for low performance
        else:
            boosted_weights.append(w)
    
    # Secondary distraction: simulate historical trend analysis (unused)
    historical_delta = 0
    hist_cycle = cycle([1.02, 0.98, 1.01])
    for _ in range(len(metrics)):
        historical_delta += next(hist_cycle)
    
    # Core scoring logic
    raw_weighted_sum = sum(metrics[i] * boosted_weights[i] for i in range(len(metrics)))
    weight_total = sum(boosted_weights)
    
    # Apply adjustment factor from earlier (only this part matters)
    base_score = raw_weighted_sum / weight_total if weight_total != 0 else 0
    
    # Conditional bonus for consistency (additional logic step)
    variance = sum((x - sum(metrics)/len(metrics))**2 for x in metrics) / len(metrics)
    if variance < 100:
        base_score += 5  # Consistency bonus
    
    # Final non-linear transformation (key step)
    final_score = int(base_score * adjustment_factor + 0.5)  # Rounded integer result
    
    # Dead code: logging to unused system
    log_entry = f'Score computed: {final_score}'
    debug_mode = False
    if debug_mode:
        print(log_entry)
        temp_buffer.append(log_entry)
    
    return final_score

# Input data
metrics = [88, 92, 76, 95, 83]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Distraction: unused alternative weighting scheme
alt_weights = [w ** 1.1 for w in weights]
shadow_score = sum(m * w for m, w in zip(metrics, alt_weights))

# Key execution point
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")