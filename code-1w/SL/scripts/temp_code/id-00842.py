def calculate_performance(flags, metrics):
    base_score = 0
    penalty_adjustment = 0
    temp_result = []
    
    # Irrelevant preprocessing: case conversion on string keys (distraction)
    normalized_keys = {k.lower(): v for k, v in metrics.items()}
    
    # Real logic begins: count active flags and apply conditional bonuses
    flag_count = sum(1 for f in flags if f[1] == True)
    
    # Misleading dead-end computation with set operations (semi-relevant but unused later)
    unique_categories = set(f[0].upper() for f in flags)
    category_penalty = len(unique_categories) > 3
    
    # Core scoring logic
    for key, value in normalized_keys.items():
        if 'response' in key:
            base_score += value * 1.5
        elif 'latency' in key:
            if value < 100:
                base_score += 20
            else:
                penalty_adjustment -= 5
        elif 'throughput' in key:
            base_score += min(value // 10, 25)

    # Additional distraction: complex dictionary aggregation not used directly
    summary_stats = {
        'total_entries': len(metrics),
        'average_value': sum(metrics.values()) / len(metrics),
        'high_performers': [v for v in metrics.values() if v > 50]
    }
    
    # Conditional bonus based on flag count
    bonus_multiplier = 1.2 if flag_count >= 2 else 1.0
    
    # Final score computation (this is where answer is determined)
    raw_score = base_score + penalty_adjustment
    final_score = int(raw_score * bonus_multiplier)
    
    # Dead code path: never executed due to prior logic
    if len(temp_result) > 100:
        final_score += 50  # unreachable
        
    return final_score

# Setup input data
bonus_flags = [
    ('network', True),
    ('storage', True),
    ('compute', False),
    ('security', True)
]

efficiency_map = {
    'response_time': 80,
    'latency_avg': 120,
    'throughput_mb': 185,
    'error_rate': 3.2,
    'retry_count': 1
}

# Execution point of interest
final_score = calculate_performance(bonus_flags, efficiency_map)
print(f"Result: {final_score}")