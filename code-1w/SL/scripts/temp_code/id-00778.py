def analyze_performance(metrics, thresholds):
    # Precompute derived metrics with some irrelevant transformations
    normalized = {k: v / 100.0 for k, v in metrics.items()}
    weighted = {k: v * 2.0 for k, v in normalized.items()}
    
    # Irrelevant computation on a subset (distractor)
    temp_debug = sum(weighted[k] for k in ['latency', 'throughput'] if k in weighted)
    adjustment_factor = temp_debug * 0.05 if temp_debug > 1 else 0.1
    
    # Core logic begins: filter metrics above threshold
    passed = set()
    for key, value in normalized.items():
        if value >= thresholds.get(key, 0.5):
            passed.add(key)
    
    # Additional distraction: unused branch with dead code hint
    if len(passed) > 10:
        fallback = [x[::-1] for x in map(str, range(len(passed)))]  # never executed
    else:
        fallback = None
    
    # Use list comprehension to compute bonus from passed categories
    bonuses = [len(category) * 0.25 for category in passed if 'error' not in category]
    base_score = sum(normalized[cat] for cat in passed)
    bonus_score = sum(bonuses)
    
    # Secondary distractor: complex but unused bitwise operation chain
    debug_flag = (len(passed) << 2) ^ 5 & len(thresholds)
    debug_flag = debug_flag + 0  # neutral operation
    
    # Final score calculation - depends only on base and bonus
    final_score = base_score + bonus_score
    
    # Print result as required
    return final_score

# Main execution context
metrics = {
    'latency': 85,
    'throughput': 92,
    'error_rate': 45,
    'availability': 99,
    'consistency': 76
}
thresholds = {
    'latency': 0.80,
    'throughput': 0.88,
    'error_rate': 0.50,
    'availability': 0.95,
    'consistency': 0.75
}

# Execute and print result
result_val = analyze_performance(metrics, thresholds)
print(f"Target result: {result_val}")