def analyze_performance(metrics, thresholds):
    # Irrelevant transformation: bit manipulation red herring
    magic_offset = (len(metrics) << 2) ^ 0xCAFEBABE
    magic_offset = magic_offset - 0xCAFEBABE if magic_offset > 0xCAFEBABE else magic_offset

    # Distractor: complex but unused conditional expression
    anomaly_flag = 'critical' if any(m < t * 0.1 for m, t in zip(metrics, thresholds)) else ('warning' if sum(metrics) > 500 else 'normal')

    adjusted = []
    for i, (m, t) in enumerate(zip(metrics, thresholds)):
        # Relevant logic hidden among distractions
        deviation = abs(m - t)
        penalty = deviation * 0.1 if m < t else 0
        
        # Distractor: dead code path (never executed due to prior condition)
        bonus = 0
        if m > t and i % 5 == 0:  # Rare index condition never met in input
            bonus = 10

        adjusted.append(m - penalty + bonus)

    # Another decoy: sophisticated but irrelevant dictionary operation
    stats_summary = {
        f'metric_{i}': {'raw': m, 'threshold': t, 'adjusted': adj} 
        for i, (m, t, adj) in enumerate(zip(metrics, thresholds, adjusted))
    }
    
    # Unused recursive helper (red herring)
    def calculate_entropy(data, depth=0):
        if depth > 3 or len(data) == 0:
            return 0
        mid = len(data) // 2
        return calculate_entropy(data[:mid], depth+1) + calculate_entropy(data[mid:], depth+1) + (data[0] if data else 0)

    # Real computation begins here — buried in noise
    base_score = sum(adjusted)
    
    # Conditional expression with actual impact
    multiplier = 1.25 if all(m >= t * 0.8 for m, t in zip(metrics, thresholds)) else 0.75
    
    # Final aggregation using dictionary-derived statistic (only one field matters)
    volatility = max(adjusted) - min(adjusted)
    
    # Key assignment: this is the target variable
    final_score = base_score * multiplier
    
    # Decoy output operations
    debug_info = {
        'volatility_index': volatility,
        'anomaly': anomaly_flag,
        'offset_trace': magic_offset & 0xFFFF  # Truncated nonsense
    }
    
    # Only this line matters
    print(f"Result: {final_score}")
    return final_score

# Simulated input data (deterministic)
performance_metrics = [85, 90, 78, 92, 88]
alert_thresholds = [80, 85, 75, 90, 85]

# Entry point
final_score = analyze_performance(performance_metrics, alert_thresholds)