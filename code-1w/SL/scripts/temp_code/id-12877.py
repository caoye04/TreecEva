def calculate_performance(results):
    base_weight = 0.8
    bonus_factor = 1.2
    penalty_threshold = 85
    
    # Irrelevant metrics (distractors)
    avg_latency = sum(results['latency']) / len(results['latency'])
    max_memory = max(results['memory_usage'])
    consistency_score = (max(results['scores']) - min(results['scores'])) / avg_latency
    
    # Relevant computation starts
    raw_total = sum(results['scores'])
    adjustment = 0
    
    # Conditional adjustment based on performance tiers
    if raw_total > 400:
        adjustment += 20
    elif raw_total > 350:
        adjustment += 10
    else:
        adjustment -= 5

    # Bonus logic with dictionary mapping (relevant)
    tier_map = {400: 'elite', 350: 'high', 300: 'medium', 0: 'low'}
    performance_tier = None
    for threshold in sorted(tier_map.keys(), reverse=True):
        if raw_total >= threshold:
            performance_tier = tier_map[threshold]
            break
    
    # Extra, irrelevant dictionary processing
    tier_stats = {}
    for k, v in tier_map.items():
        tier_stats[v] = k * 0.1
    
    # Final score calculation (key step)
    scaled_total = raw_total * base_weight
    if performance_tier == 'elite':
        scaled_total *= bonus_factor
    
    # Apply adjustment
    final_score = scaled_total + adjustment
    
    # Dead code branch (distractor)
    if max_memory > 1000:
        final_score -= 10
    else:
        pass  # No effect
    
    return final_score

# Input data
benchmark_results = {
    'scores': [95, 87, 78, 92, 88],
    'latency': [120, 110, 115, 105, 125],
    'memory_usage': [750, 700, 780, 800, 720]
}

# Key execution point
final_score = calculate_performance(benchmark_results)
print(f"Result: {final_score}")