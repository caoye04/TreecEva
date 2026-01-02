import itertools

# Simulated health monitoring system with sensor fusion and diagnostic logic
def preprocess_signals(raw_readings):
    filtered = [x for x in raw_readings if 40 <= x <= 200]
    baseline = sum(filtered) / len(filtered)
    # Distractor: irrelevant transformation
    inverted = [1000 / (x + 1) for x in filtered]
    normalized = [(x - baseline) / baseline for x in filtered]
    return normalized, inverted  # 'inverted' is never used later

# Distractor function – looks important but unused in final path
def compute_heart_rate_variability(rr_intervals):
    diffs = [abs(a - b) for a, b in zip(rr_intervals, rr_intervals[1:])]
    rmssd = (sum(d ** 2 for d in diffs) / len(diffs)) ** 0.5
    return round(rmssd, 3)

# Auxiliary function for data enrichment (used)
def augment_features(values):
    squared = list(map(lambda x: x ** 2, values))
    log_vals = [abs(x) ** 0.1 for x in values if x != 0]  # Avoid log(0)
    rolling_avg = [
        (values[i] + values[i+1] + values[i+2]) / 3 
        for i in range(len(values) - 2)
    ]
    return {
        'energy': sum(squared),
        'complexity': len(log_vals),
        'trend_stability': abs(rolling_avg[-1] - rolling_avg[0]) if rolling_avg else 0
    }

# Misleading anomaly detector (partially executed red herring)
def detect_outliers(data, factor=1.5):
    sorted_data = sorted(data)
    q1, q3 = sorted_data[len(sorted_data)//4], sorted_data[3*len(sorted_data)//4]
    iqr = q3 - q1
    lower, upper = q1 - factor * iqr, q3 + factor * iqr
    outliers = [x for x in data if x < lower or x > upper]
    # This result is computed but not used in final logic
    return {'count': len(outliers), 'values': outliers, 'thresholds': (lower, upper)}

# Core diagnostic engine
def analyze_metrics(sensor_stream, criteria):
    # Step 1: Preprocess signals
    processed, _ = preprocess_signals(sensor_stream)  # Ignore second return
    
    # Step 2: Augment feature set
    features = augment_features(processed)
    
    # Step 3: Apply threshold filtering using dictionary lookup
    critical_energy = criteria['metabolic']['threshold']
    stability_ref = criteria['neurological']['stability_index']
    
    # Step 4: Simulate multi-system correlation
    correlations = []
    for a, b in itertools.pairwise(processed):
        correlations.append(abs(a * b))
    avg_corr = sum(correlations) / len(correlations) if correlations else 0
    
    # Step 5: Compute risk score (intermediate distractor)
    risk_score = 0
    if features['energy'] > critical_energy:
        risk_score += 30
    if features['trend_stability'] > stability_ref:
        risk_score += 20
    if avg_corr > 0.1:
        risk_score += 10
    
    # Distractor: dead code path due to constant condition
    emergency_override = False
    if False:  # Never executes
        backup_system = {"status": "standby", "risk": risk_score}
        emergency_override = True if backup_system["status"] == "active" else False
    
    # Step 6: Final diagnostic via weighted combination
    weight_energy = criteria['weights']['metabolic']
    weight_corr = criteria['weights']['cardio']
    weight_complexity = criteria['weights']['neural']
    
    composite_index = (
        features['energy'] * weight_energy +
        avg_corr * weight_corr +
        features['complexity'] * weight_complexity
    )
    
    # Step 7: Apply nonlinear transformation
    if composite_index > 0:
        final_diagnostic = int((composite_index ** 0.5) * 100)
    else:
        final_diagnostic = 0
    
    # Irrelevant logging operations (no effect on output)
    debug_log = f'Diagnostic complete: index={composite_index:.2f}, risk={risk_score}'
    audit_trail = [{'step': 'preprocessing', 'size': len(processed)}, {'step': 'features', 'keys': len(features)}]
    
    return final_diagnostic

# Main execution block
if __name__ == '__main__':
    # Simulated physiological data from wearable sensors
    health_data = [65, 70, 72, 68, 75, 80, 60, 55, 50, 45, 42, 210, 220, 63, 67, 71]
    
    # Threshold configuration map (real usage)
    thresholds = {
        'metabolic': {'threshold': 0.8},
        'neurological': {'stability_index': 0.5},
        'weights': {
            'metabolic': 0.6,
            'cardio': 0.3,
            'neural': 0.1
        }
    }
    
    # Dead variable assignments (red herrings)
    calibration_matrix = [[1.0, 0.1], [0.2, 0.9]]
    signal_quality = sum(1 for x in health_data if 50 <= x <= 100) / len(health_data)
    artifact_count = len([x for x in health_data if x > 200 or x < 40])
    
    # Execute outlier detection (computed but not used)
    spurious_findings = detect_outliers(health_data, factor=2.0)
    
    # Actual key computation
    final_diagnostic = analyze_metrics(health_data, thresholds)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")