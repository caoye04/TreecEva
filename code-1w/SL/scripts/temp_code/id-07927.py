import itertools

# Simulated sensor data processing pipeline for industrial equipment monitoring
def collect_telemetry():
    raw_signals = [127, 85, 194, 63, 201, 48, 177, 92]
    timestamps = list(range(1000, 1008))
    return list(zip(timestamps, raw_signals))

def filter_outliers(signal_pairs, threshold=150):
    filtered = []
    noise_floor = []
    for ts, val in signal_pairs:
        if val > threshold:
            filtered.append((ts, val))
        else:
            noise_floor.append(val)  # irrelevant storage
    adjustment_factor = sum(noise_floor) / len(noise_floor) if noise_floor else 0
    adjusted = [(ts, val - adjustment_factor) for ts, val in filtered]
    return adjusted

def compute_envelope(signal_list):
    magnitudes = [val for _, val in signal_list]
    peak = max(magnitudes)
    rms = (sum(x**2 for x in magnitudes) / len(magnitudes)) ** 0.5
    crest_factor = peak / rms if rms != 0 else 0
    return {'peak': peak, 'rms': rms, 'crest_factor': crest_factor}

def generate_synthetic_features(base_metrics):
    # Distractor function: generates unused advanced diagnostics
    synthetic = {}
    for i in range(3):
        synthetic[f'phantom_metric_{i}'] = base_metrics['rms'] * (1.0 + i * 0.1)
    return synthetic  # never used

def derive_health_index(crest):
    if crest < 2.0:
        return 95
    elif crest < 3.0:
        return 75
    elif crest < 4.0:
        return 50
    else:
        return 20

def apply_calibration_adjustment(raw_index, age_years):
    # Complex but partially irrelevant adjustment logic
    age_factors = {1: 1.0, 2: 0.95, 3: 0.9, 4: 0.85, 5: 0.8}
    factor = age_factors.get(age_years, 0.8)
    adjusted = raw_index * factor
    if adjusted > 90:
        category = 'A'
    elif adjusted > 70:
        category = 'B'
    else:
        category = 'C'
    return adjusted, category  # returns tuple but only first used

def slice_critical_window(data_points, window_size=3):
    # Uses slicing to extract most recent anomalies
    sorted_by_time = sorted(data_points, key=lambda x: x[0], reverse=True)
    recent = sorted_by_time[:window_size]
    return [val for _, val in recent]

def calculate_variance(samples):
    n = len(samples)
    if n < 2:
        return 0.0
    mean = sum(samples) / n
    return sum((x - mean) ** 2 for x in samples) / (n - 1)

def detect_trend(pattern):
    if len(pattern) < 2:
        return 'stable'
    diffs = [pattern[i+1] - pattern[i] for i in range(len(pattern)-1)]
    pos = sum(1 for d in diffs if d > 0)
    neg = sum(1 for d in diffs if d < 0)
    if pos > neg:
        return 'increasing'
    elif neg > pos:
        return 'decreasing'
    else:
        return 'stable'

def evaluate_performance(metrics_dict, reference_level):
    # Core evaluation logic
    cf = metrics_dict['crest_factor']
    health = derive_health_index(cf)
    calibrated, _ = apply_calibration_adjustment(health, 4)
    deviation = abs(calibrated - reference_level)
    penalty = deviation * 0.5
    score = calibrated - penalty
    return int(score)

def main():
    # Irrelevant preprocessing block
    temp_buffer = [x for x in range(50, 60, 2)]
    temp_stats = {"avg": sum(temp_buffer)/len(temp_buffer), "cnt": len(temp_buffer)}
    
    # Main data flow
    raw_data = collect_telemetry()
    clean_data = filter_outliers(raw_data)
    envelope_stats = compute_envelope(clean_data)
    
    # Dead code path - looks important but unused
    advanced_diagnostics = generate_synthetic_features(envelope_stats)
    diagnostic_summary = {"count": len(advanced_diagnostics), "version": "2.1"}
    
    # Critical window analysis (used later)
    critical_values = slice_critical_window(clean_data, 3)
    variance_estimate = calculate_variance(critical_values)
    trend_analysis = detect_trend(critical_values)
    
    # Secondary distraction: unused dictionary aggregation
    summary_report = {}
    summary_report['envelope'] = envelope_stats
    summary_report['variance'] = variance_estimate
    summary_report['trend'] = trend_analysis
    summary_report['timestamp'] = 1007
    summary_report['source_count'] = len(clean_data)
    
    # Additional red herring: complex but unused itertools operation
    permutations = list(itertools.permutations([1, 2, 3]))[:2]  # computed but not used
    permutation_sum = sum(sum(p) for p in permutations) if permutations else 0
    
    # Final computation chain
    baseline_ref = 80
    final_score = evaluate_performance(envelope_stats, baseline_ref)
    
    # Distraction: meaningless bit manipulation
    magic_constant = 0xABCDEF
    obscured = final_score ^ magic_constant
    obscured >>= 4
    obscured &= 0xFF
    
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()