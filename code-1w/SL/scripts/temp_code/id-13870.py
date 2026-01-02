def evaluate_performance(metrics):
    base_score = 0
    penalty_factor = 1.0
    bonus_multiplier = 1.0

    # Irrelevant preprocessing: Normalize metrics (not all used)
    normalized = {k: v / (sum(metrics.values()) + 1e-5) for k, v in metrics.items()}
    
    # Distractor: Compute entropy (unused in final logic)
    import math
    entropy = -sum(p * math.log(p + 1e-10) for p in normalized.values())

    # Relevant metric extraction
    accuracy = metrics.get('accuracy', 0)
    latency = metrics.get('latency', 100)
    throughput = metrics.get('throughput', 0)
    consistency = metrics.get('consistency', 0)

    # Misleading intermediate score branches
    if accuracy > 85:
        base_score += 20
        if latency < 50:
            base_score += 10
            bonus_multiplier *= 1.2
        elif latency < 80:
            base_score += 5
        else:
            penalty_factor *= 0.9
    
    if throughput > 1000:
        base_score += 15
        # Dead code path — condition never reached due to fixed inputs
        if False and consistency > 90:
            base_score += 25
    else:
        base_score += 5

    # Set operations to assess quality bands (semi-relevant)
    high_tier = {i for i in range(90, 101)}
    mid_tier = {i for i in range(70, 90)}
    tier_flags = set()
    
    if accuracy in high_tier:
        tier_flags.add('high_accuracy')
    if throughput // 100 in high_tier:
        tier_flags.add('high_throughput_norm')

    # Another distraction: dictionary transformation
    score_breakdown = {
        'base': base_score,
        'penalty': penalty_factor,
        'bonus': bonus_multiplier,
        'flags': len(tier_flags)
    }

    # Actual scoring logic
    raw_score = base_score * bonus_multiplier
    raw_score -= abs(latency - 60) * 0.5  # Penalty for deviation from ideal latency

    # Final adjustment based on consistency band using dict lookup
    consistency_band = 'low'
    if consistency >= 85:
        consistency_band = 'high'
    elif consistency >= 70:
        consistency_band = 'medium'
    
    band_adjustment = {'low': -5, 'medium': 0, 'high': 8}
    adjusted_score = raw_score + band_adjustment[consistency_band]

    # Key assignment point
    final_score = int(round(adjusted_score))

    return final_score

# Simulated model evaluation metrics
metrics_data = {
    'accuracy': 92,
    'latency': 68,
    'throughput': 1200,
    'consistency': 76
}

# Execution point of interest
final_score = evaluate_performance(metrics_data)
print(f"Result: {final_score}")