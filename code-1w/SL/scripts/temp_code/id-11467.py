def analyze_performance(metrics, thresholds):
    # Irrelevant transformation (distractor)
    normalized = [round((m - min(metrics)) / (max(metrics) - min(metrics) + 1e-5), 3) for m in metrics]
    
    high_performers = 0
    compliance_flags = []

    for i, metric in enumerate(metrics):
        # Semi-relevant logic: count how many exceed individual thresholds
        if metric > thresholds[i % len(thresholds)]:
            high_performers += 1
        
        # Conditional expression used idiomatically
        status = 'pass' if metric >= thresholds[i % len(thresholds)] * 0.9 else 'review'
        compliance_flags.append(status)

    # Distractor computation: unused weighted average
    weights = [0.5 if f == 'pass' else 0.1 for f in compliance_flags]
    weighted_avg = sum(m * w for m, w in zip(metrics, weights)) / sum(weights) if weights else 0

    # Core logic: bitwise consistency check across compliance (relevant)
    binary_state = 0
    for flag in compliance_flags:
        binary_state ^= 1 if flag == 'pass' else 0  # XOR accumulator
    
    # Nested condition with conditional expression
    adjustment_factor = 1.2 if high_performers >= len(metrics) // 2 else 0.8
    penalty = 10 if binary_state == 0 else 0

    # Key intermediate result
    base_score = sum(metrics) / len(metrics)

    # Final score depends on multiple prior paths
    final_score = (base_score * adjustment_factor) - penalty

    # Print required for traceability
    print(f"Result: {final_score}")
    
    return final_score

# Simulated input data
metrics_data = [85, 92, 78, 96, 88]
thresholds_config = [80, 90, 75, 95, 85]

# Execution point of interest
final_score = analyze_performance(metrics_data, thresholds_config)