def analyze_performance(metrics, thresholds):
    # Irrelevant transformation (distractor)
    adjusted_metrics = [m * 1.05 for m in metrics if m > 0]
    
    # Semi-relevant filtering
    passed = [m for m in metrics if m >= thresholds['min_pass']]
    excellence = [m for m in metrics if m >= thresholds['excellent']]

    # Distractor: unused computation
    avg_adjusted = sum(adjusted_metrics) / len(adjusted_metrics) if adjusted_metrics else 0
    peak_deviation = max(adjusted_metrics) - min(adjusted_metrics) if adjusted_metrics else 0

    return len(passed), len(excellence)


def generate_diagnostic_report(data):
    # Complex but partially irrelevant preprocessing
    baseline = sum(data) / len(data)
    deviations = [abs(x - baseline) for x in data]
    significant_dev = [d for d in deviations if d > baseline * 0.1]
    
    # Unused aggregation
    high_dev_count = len(significant_dev)
    total_variance = sum(d ** 2 for d in deviations) / len(deviations) if deviations else 0

    # Core logic embedded within noise
    if len(data) < 5:
        return {'status': 'insufficient', 'score': 0}
    
    above_avg = [x for x in data if x > baseline]
    stability_ratio = len(above_avg) / len(data)
    
    return {
        'status': 'complete',
        'score': stability_ratio,
        'size': len(data)
    }

# Main execution block with mixed concerns
def calculate_final_score(raw_inputs):
    # Key parameter transformations
    processed = [x + 2 for x in raw_inputs if x % 2 == 1]  # Only odd numbers get incremented
    filtered = [p for p in processed if p < 50]  # Filter based on threshold

    # Distractor: elaborate set operations with no impact
    unique_orig = set(raw_inputs)
    unique_proc = set(processed)
    overlap = unique_orig.intersection(unique_proc)
    symmetric_diff = unique_orig.symmetric_difference(set(filtered))
    
    # Unused statistical measures
    mean_orig = sum(raw_inputs) / len(raw_inputs)
    mean_proc = sum(processed) / len(processed) if processed else 0
    fluctuation_index = abs(mean_proc - mean_orig) / mean_orig if mean_orig != 0 else 0

    # Conditional branching with nested logic
    if len(filtered) > 10:
        bonus_factor = 1.5
    elif len(filtered) >= 5:
        bonus_factor = 1.2
    else:
        bonus_factor = 1.0

    base_score = sum(filtered)
    adjustment = 0
    for val in filtered:
        if val > 40:
            adjustment += 3
        elif val > 30:
            adjustment += 2
        else:
            adjustment += 1
    
    # Final computation
    final_score = int((base_score + adjustment) * bonus_factor)
    
    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Simulate input data
input_stream = [12, 15, 22, 33, 41, 8, 19, 27, 36, 44, 5, 11, 29, 31, 48]

# Call diagnostic (partially irrelevant)
diag = generate_diagnostic_report(input_stream)

# Extract performance stats (semi-relevant)
pass_count, excel_count = analyze_performance(input_stream, {
    'min_pass': 25,
    'excellent': 40
})

# Compute target result
final_score = calculate_final_score(input_stream)