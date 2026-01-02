import itertools

# Simulated sensor data processing pipeline for industrial monitoring system
def collect_diagnostics():
    return [72, 65, 88, 91, 54, 77, 83]

def normalize_readings(readings):
    max_val = max(readings)
    return [round(x / max_val * 100) for x in readings]

def filter_anomalies(normalized):
    threshold = 60
    return [x for x in normalized if x >= threshold]

def compute_trend(data):
    changes = [b - a for a, b in zip(data[:-1], data[1:])]    
    return sum(changes) / len(changes) if changes else 0

# Irrelevant auxiliary function - decoy
def predict_failure_risk(values):
    risk = 0
    for v in values:
        if v > 90:
            risk += 10
        elif v > 80:
            risk += 5
    return risk * 1.5

def aggregate_summary(cleaned):
    avg = sum(cleaned) / len(cleaned)
    peak = max(cleaned)
    count = len(cleaned)
    # Dead computation - misleading intermediate
    dummy_weight = (peak * 0.3 + avg * 0.7) // 2
    return {'average': avg, 'peak': peak, 'count': count}

def apply_calibration(summary, factor=1.05):
    calibrated_avg = summary['average'] * factor
    adjusted_peak = min(summary['peak'] * 1.02, 100)
    # Unused variable - red herring
    synthetic_index = (calibrated_avg + adjusted_peak) / 2 * 1.1
    summary['calibrated_avg'] = calibrated_avg
    return summary

def assess_stability(trend, cleaned_data):
    if abs(trend) < 5:
        return 'stable'
    elif trend > 0:
        return 'rising'
    else:
        return 'falling'

# Complex logic with distractors
def generate_insights(calib, status, trend):
    insight_map = {
        'stable': lambda x: x * 0.95,
        'rising': lambda x: x * 1.08,
        'falling': lambda x: x * 0.87
    }
    base = calib.get('calibrated_avg', 0)
    # Misleading transformation
    shadow_value = base * 1.2 if status == 'rising' else base * 0.85
    adjusted_base = insight_map.get(status, lambda x: x)(base)
    
    # Multiple distractor variables
    phantom_metric = adjusted_base ** 0.5 * 3.14
    noise_factor = len([x for x in range(5) if x % 2 == 0])  # constant 3
    final_adjustment = adjusted_base + (trend * 0.5) - (noise_factor * 0.2)
    
    return round(final_adjustment, 2)

def evaluate_performance(metrics, baseline):
    performance_gap = metrics['calibrated_avg'] - baseline
    volatility_penalty = abs(metrics.get('volatility', 0)) * 0.3
    # Critical line - answer depends on this
    final_score = int((performance_gap * 1.2) - volatility_penalty + 70)
    
    # Dead code path - never executed
    if final_score < 0:
        final_score = 0
    elif final_score > 150:
        excess = final_score - 150
        final_score = 150 - int(excess * 0.1)
    
    return final_score

# Main execution flow
raw_data = collect_diagnostics()
normalized_data = normalize_readings(raw_data)
cleaned_readings = filter_anomalies(normalized_data)
trend_value = compute_trend(cleaned_readings)
diagnostic_summary = aggregate_summary(cleaned_readings)
calibrated_summary = apply_calibration(diagnostic_summary)
operational_status = assess_stability(trend_value, cleaned_readings)
insight_value = generate_insights(calibrated_summary, operational_status, trend_value)

# Unused but plausible-looking computations - red herrings
failure_risk = predict_failure_risk(raw_data)
system_health = (insight_value + calibrated_summary['average']) / 2
baseline_reference = 75
volatility_index = compute_trend(normalized_data)  # not used later

# Key statement - target for evaluation
calibrated_summary['volatility'] = abs(volatility_index) * 0.5  # injects into dict
final_score = evaluate_performance(calibrated_summary, baseline_reference)

print(f"Result: {final_score}")