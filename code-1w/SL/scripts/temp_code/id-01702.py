from collections import defaultdict, Counter

# Simulated sensor fusion system for environmental anomaly detection
def collect_diagnostics():
    raw_samples = [14, 17, 18, 21, 19, 23, 25, 22, 16, 15, 13, 20]
    calibration_offsets = [0.3, -0.2, 0.5, 0.1, -0.4]
    baseline_shift = sum(calibration_offsets) / len(calibration_offsets)

    # Irrelevant preprocessing: historical normalization (unused later)
    historical_mean = 18.5
    normalized_samples = [x - historical_mean + baseline_shift for x in raw_samples]

    # Critical data structure: multi-source sensor readings
    sensor_data = {
        'primary': [x * 1.02 for x in raw_samples[::2]],
        'secondary': [x * 0.98 for x in raw_samples[1::2]],
        'auxiliary': [abs(x - 20)**1.5 for x in raw_samples]
    }

    # Decoy transformation chain (dead path)
    transformed_aux = []
    for val in sensor_data['auxiliary']:
        if val > 10:
            transformed_aux.append(val * 0.75)
        else:
            transformed_aux.append(val * 1.1)
    # ^ This variable is never used again

    # Threshold policy configuration (only 'critical' and 'elevated' are used)
    thresholds = defaultdict(lambda: 0)
    thresholds.update({
        'normal': 15.0,
        'elevated': 18.5,
        'critical': 22.0,
        'extreme': 28.0  # Unused threshold
    })

    # Misleading intermediate summary
    outlier_count = sum(1 for v in raw_samples if v > 24)
    temp_alert_level = 'green' if outlier_count == 0 else 'amber'
    # ^ This alert level is recalculated properly later

    # Core processing function embedded to increase nesting
    def process_readings(data, limits):
        # Level 1: Aggregate all readings with weighting
        weighted_fusion = []
        for key, readings in data.items():
            weight = 1.2 if key == 'primary' else 0.9 if key == 'secondary' else 0.3
            weighted_fusion.extend([r * weight for r in readings])
        
        # Level 2: Apply dynamic clipping based on mode
        mode_estimate = Counter([round(x) for x in weighted_fusion]).most_common(1)[0][0]
        clipped_readings = [min(x, mode_estimate + 3) for x in weighted_fusion]
        
        # Level 3: Segment and classify
        categories = defaultdict(int)
        for val in clipped_readings:
            if val < limits['elevated']:
                categories['stable'] += 1
            elif val < limits['critical']:
                categories['warning'] += 1
            else:
                categories['alert'] += 1
        
        # Level 4: Compute diagnostic score using combinatorics
        n_total = len(clipped_readings)
        if n_total == 0:
            return 0
        
        # Complex scoring with conditional logic
        stability_ratio = categories['stable'] / n_total
        risk_factor = (categories['alert'] * 3 + categories['warning'] * 1.5) / n_total
        
        # Conditional expression determining processing path
        base_score = 40 if stability_ratio > 0.6 else 25
        adjustment = -15 if risk_factor > 2.0 else (5 if risk_factor > 0.8 else 0)
        
        # Final nonlinear transformation
        raw_diagnostic = base_score + adjustment + (stability_ratio * 100)
        
        # Dead computation: entropy calculation (unused)
        prob_dist = [categories[k] / n_total for k in ['stable', 'warning', 'alert']]
        from math import log2
        entropy = -sum(p * log2(p) for p in prob_dist if p > 0)
        # ^ Computed but not used
        
        # Secondary decoy logic: simulate rollback condition
        rollback_trigger = False
        consecutive_alerts = 0
        for val in sorted(clipped_readings, reverse=True):
            if val >= limits['critical']:
                consecutive_alerts += 1
                if consecutive_alerts >= 3:
                    rollback_trigger = True
                    break
            else:
                break
        # rollback_trigger is never used
        
        return int(raw_diagnostic)  # Deterministic integer result

    # Actual execution point of interest
    final_diagnostic = process_readings(sensor_data, thresholds)
    
    # Post-processing red herring
    audit_log = []
    for i, sample in enumerate(raw_samples):
        if sample % 2 == 0 and i % 3 == 0:
            audit_log.append(f"Sample_{i}:Verified")
    # audit_log unused
    
    # Final output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execute and capture result
collect_diagnostics()