import itertools

def analyze_readings(readings):
    # Irrelevant transformation: converts to percentages (unused)
    normalized = [r * 0.01 for r in readings if r > 0]
    smoothed = [sum(readings[i:i+3]) / 3 for i in range(len(readings) - 2)]
    
    # Distractor: complex but unused statistical moment calculation
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    skewness = sum((x - mean_val) ** 3 for x in readings) / (len(readings) * variance ** 1.5) if variance > 0 else 0

    # Relevant logic: count how many readings exceed 85
    critical_count = len([r for r in readings if r > 85])
    return critical_count


def validate_samples(samples):
    # Unused validation function with red herring logic
    valid_set = {s for s in samples if 10 < s < 95}
    outliers = [s for s in samples if s < 5 or s > 99]
    return len(valid_set) > 0


def compute_diagnostics(data):
    # Mix of relevant and irrelevant operations
    baseline = data.get('baseline', [])
    stress_test = data.get('stress', [])
    recovery = data.get('recovery', [])

    # Dead code path: never called due to condition below
    def legacy_calibrate(x):
        return [i * 1.05 for i in x]

    # Distractor: complex set operation with no impact
    unique_stress = set(itertools.chain.from_iterable(
        [[s-1, s, s+1] for s in stress_test if s % 10 == 0]
    ))
    overlap = unique_stress.intersection(set(recovery))

    # Relevant aggregation: only baseline contributes to result
    if len(baseline) >= 3:
        moving_avg = [sum(baseline[i:i+3]) / 3 for i in range(len(baseline) - 2)]
        above_threshold = [v for v in moving_avg if v > 75]
        score = len(above_threshold) * 2
    else:
        score = 0

    # Decoy return that looks important but isn't used
    metadata_summary = {
        'entries': len(stress_test),
        'peak': max(stress_test) if stress_test else 0,
        'outlier_ratio': len([s for s in stress_test if s > 90]) / len(stress_test) if stress_test else 0
    }

    return score


def process_metrics(health_data, limits):
    # Key logic hidden among distractions
    result_map = {}
    
    for key, values in health_data.items():
        if key == 'baseline':
            # Real computation branch
            filtered = [v for v in values if v >= limits['min']]
            processed = list(map(lambda x: x ** 0.5, filtered))  # sqrt transformation
            rounded = [round(p, 2) for p in processed]
            count_valid = len([r for r in rounded if r > 8.0])
            result_map[key] = count_valid * 10
        elif key == 'stress':
            # Complex but ultimately irrelevant processing
            paired = list(itertools.combinations(values, 2))
            high_pairs = [p for p in paired if sum(p) > 150]
            result_map[key] = len(high_pairs) // 2
        else:
            result_map[key] = 0
    
    # Final aggregation: only 'baseline' matters
    final_value = sum(v for k, v in result_map.items() if k == 'baseline')
    
    # Critical side computation: character counting in decoy string
    decoy_text = "analysis_complete_2024"
    char_count = len([c for c in decoy_text if c.isdigit()])  # evaluates to 4, misleading
    
    # Another red herring: unused dictionary transformation
    dummy_audit = {
        k: {'count': len(v), 'flagged': any(x < 20 for x in v)}
        for k, v in health_data.items()
    }
    
    final_diagnostic = final_value + char_count  # char_count is distraction!
    return final_value  # Actual return ignores char_count

# Main execution block
if __name__ == '__main__':
    # Input data
    health_data = {
        'baseline': [64, 81, 100, 121, 144],
        'stress': [70, 88, 92, 96, 77],
        'recovery': [60, 68, 72]
    }
    
    thresholds = {
        'min': 60,
        'max': 150
    }

    # Call analysis functions (some return unused results)
    critical_readings = analyze_readings(health_data['stress'])
    sample_status = validate_samples(health_data['baseline'])
    diagnostic_score = compute_diagnostics(health_data)
    
    # KEY STATEMENT
    final_diagnostic = process_metrics(health_data, thresholds)
    
    # Print result
    print(f"Result: {final_diagnostic}")