from collections import defaultdict, Counter

# Simulated sensor fusion system for autonomous drone diagnostics
def analyze_temporal_pattern(sequence, threshold=5):
    counter = 0
    trend_score = 0
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            counter += 1
            trend_score += (sequence[i] - sequence[i-1]) * 1.5
    return counter > threshold, round(trend_score, 3)

def evaluate_signal_stability(readings):
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    stable = variance < 12.5
    return stable, round(variance, 3)

def extract_critical_windows(data_stream, window_size=4):
    windows = [data_stream[i:i+window_size] for i in range(0, len(data_stream), window_size)]
    peaks = [max(win) for win in windows if len(win) == window_size]
    return peaks

def filter_anomalies(peaks, limit=85):
    return [p for p in peaks if p <= limit]

def compute_health_factor(metrics):
    base = metrics.get('temp_trend', 0)
    stability = metrics.get('signal_var', 0)
    response_time = metrics.get('latency', 0)
    flag_weight = metrics.get('active_flags', 0)
    
    # Irrelevant distraction: complex-looking but unused formula
    decoy_score = (base ** 2 + stability * 1.7) / (response_time + 1) if response_time else 0
    
    health = base * 1.3 - stability * 0.4 + max(10 - response_time, 0) * 0.8
    return round(health, 3)

def aggregate_metrics(timing_data, flags):
    raw_sequence = timing_data.get('timestamps', [])
    signal_readings = timing_data.get('signals', [])
    latency_snapshot = timing_data.get('latency', 20)
    
    # Real computation branch
    trend_detected, temp_trend = analyze_temporal_pattern(raw_sequence)
    is_stable, var_score = evaluate_signal_stability(signal_readings)
    all_peaks = extract_critical_windows(raw_sequence)
    valid_peaks = filter_anomalies(all_peaks)
    peak_count = len(valid_peaks)
    
    # Distractor variables - used nowhere meaningful
    shadow_metrics = defaultdict(lambda: 0)
    shadow_metrics['baseline'] = sum(raw_sequence) // len(raw_sequence)
    shadow_metrics['peak_flux'] = max(raw_sequence) - min(raw_sequence)
    shadow_metrics['decoy_flag'] = flags.count('ERR') * 2
    
    # More distractions: unused lambda and slicing that looks important
    process_fn = lambda x: x[::2] if len(x) > 5 else x
    sliced_view = process_fn(signal_readings[:12])
    inverted_view = signal_readings[::-1]
    median_like = sorted(sliced_view)[len(sliced_view)//2] if sliced_view else 0
    
    # Dummy logic with short-circuit that doesn't affect outcome
    debug_mode = False
    log_threshold = 0
    if debug_mode and (log_threshold > 5 or len(inverted_view) < 30):
        print("Diagnostic logging active")  # Dead code path
    
    # Critical metric construction
    diagnostic_vector = {
        'temp_trend': temp_trend,
        'signal_var': var_score,
        'latency': latency_snapshot,
        'active_flags': len([f for f in flags if f in ['WARN', 'ERR']]),
        'peak_count': peak_count
    }
    
    # Final computation
    preliminary_score = compute_health_factor(diagnostic_vector)
    adjustment = 0
    if diagnostic_vector['active_flags'] > 0:
        adjustment -= 5.5
    if not is_stable:
        adjustment -= 3.2
    
    final_diagnostic = round(preliminary_score + adjustment, 3)
    
    # This print is required for execution trace
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulated input data - realistic sensor fusion scenario
timing_input = {
    'timestamps': [3, 5, 9, 14, 20, 27, 35, 44],
    'signals': [88, 85, 87, 86, 89, 83, 85, 90, 88, 84, 86, 87, 85, 91, 89, 82],
    'latency': 18
}

flag_log = ['INFO', 'INFO', 'WARN', 'INFO', 'DEBUG', 'ERR']

# Execution point of interest
final_diagnostic = aggregate_metrics(timing_input, flag_log)