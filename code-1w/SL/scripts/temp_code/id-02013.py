from collections import defaultdict, Counter

# Simulated sensor log processing for a distributed system health monitor
def analyze_patterns(sequence, window_size=3):
    pattern_count = defaultdict(int)
    for i in range(len(sequence) - window_size + 1):
        window = tuple(sequence[i:i+window_size])
        pattern_count[window] += 1
    return pattern_count

def evaluate_stability(risk_series):
    if len(risk_series) < 2:
        return 0
    trend_changes = 0
    for i in range(1, len(risk_series)):
        if (risk_series[i] - risk_series[i-1]) * (risk_series[i-1] - risk_series[i-2]) < 0 if i > 1 else False:
            trend_changes += 1
    return trend_changes

def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values if v > 0]
    entropy = -sum(p * __import__('math').log2(p) for p in probabilities)
    return round(entropy, 6)

def extract_anomalies(records, severity_cap=8):
    anomalies = []
    for record in records:
        if record.get('status') == 'ERROR' and record.get('severity', 0) > 5:
            anomalies.append(record['code'])
    return anomalies

def mock_calibration(data):
    # Irrelevant calibration function – dead code path
    calibrated = [x * 0.98 for x in data]
    return [round(c, 2) for c in calibrated]

def assess_load_distribution(services):
    loads = [s['load'] for s in services]
    avg_load = sum(loads) / len(loads)
    variance = sum((x - avg_load) ** 2 for x in loads) / len(loads)
    return avg_load, variance

def filter_events(timestamps, labels):
    # Misleading function using zip and enumerate but not contributing to final result
    labeled_events = []
    for idx, (ts, lbl) in enumerate(zip(timestamps, labels)):
        if 'critical' in lbl.lower() and idx % 2 == 0:
            labeled_events.append(f'{ts}:{lbl}')
    return labeled_events

def derive_health_index(metrics):
    base_score = 100
    for key, value in metrics.items():
        if 'error' in key:
            base_score -= value * 1.5
        elif 'latency' in key:
            base_score -= value // 10
    return max(base_score, 0)

def process_metrics(log_data, thresholds):
    # Core relevant logic begins here
    event_types = [entry['type'] for entry in log_data]
    type_counts = Counter(event_types)
    
    critical_count = type_counts.get('CRITICAL', 0)
    warning_count = type_counts.get('WARNING', 0)
    info_count = type_counts.get('INFO', 0)
    
    # Compute weighted risk score
    risk_score = (
        critical_count * 5.0 +
        warning_count * 2.0 +
        info_count * 0.5
    )
    
    # Extract numeric traces from logs
    traces = []
    for entry in log_data:
        if 'trace' in entry:
            traces.extend(entry['trace'])
    
    # Analyze trace patterns
    pattern_freq = analyze_patterns(traces, 2)
    complex_patterns = sum(1 for freq in pattern_freq.values() if freq > 1)
    
    # Evaluate stability based on trace deltas
    trace_diffs = [abs(traces[i] - traces[i-1]) for i in range(1, len(traces))]
    instability_score = evaluate_stability(trace_diffs[:10])
    
    # Compute entropy of trace distribution
    entropy = compute_entropy(traces)
    
    # Health index from auxiliary metrics
    aux_metrics = {
        'error_rate': 12,
        'latency_avg_ms': 145
    }
    health_index = derive_health_index(aux_metrics)
    
    # Threshold comparison
    threshold_met = [
        critical_count < thresholds['max_critical'],
        risk_score < thresholds['risk_limit'],
        entropy > thresholds['min_entropy']
    ]
    
    # Final diagnostic calculation (this is the actual answer)
    final_diagnostic = (
        (critical_count * 100) +
        (instability_score * 10) +
        int(entropy * 10) +
        (0 if all(threshold_met) else 500)
    )
    
    # Unused intermediate variables (distractors)
    avg_load, load_variance = assess_load_distribution([
        {'name': 'svc_a', 'load': 78},
        {'name': 'svc_b', 'load': 85},
        {'name': 'svc_c', 'load': 65}
    ])
    calibration_test = mock_calibration([100, 200, 300])
    anomaly_codes = extract_anomalies([
        {'status': 'ERROR', 'severity': 7, 'code': 'E99'},
        {'status': 'WARN', 'severity': 4, 'code': 'W22'}
    ])
    filtered_events = filter_events(
        [1678886400, 1678886401, 1678886402],
        ['critical-alert', 'info-only', 'critical-reset']
    )
    
    return final_diagnostic

# Input data
log_data = [
    {'type': 'CRITICAL', 'trace': [5, 7, 5, 3]},
    {'type': 'WARNING', 'trace': [7, 5, 3, 2]},
    {'type': 'CRITICAL', 'trace': [3, 2, 1, 1]},
    {'type': 'INFO', 'trace': [2, 1, 1, 0]}
]

system_thresholds = {
    'max_critical': 3,
    'risk_limit': 25.0,
    'min_entropy': 1.0
}

# Execution
final_diagnostic = process_metrics(log_data, system_thresholds)
print(f"Target result: {final_diagnostic}")