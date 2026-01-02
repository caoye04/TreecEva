import math

def analyze_signal_strength(raw_data, threshold=0.75):
    filtered = [x for x in raw_data if x > threshold]
    return len(filtered) / len(raw_data) if raw_data else 0

def compute_entropy(values):
    total = sum(values)
    probabilities = [v / total for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probabilities)

def validate_checksum(record):
    # Irrelevant validation function (dead end)
    checksum = 0
    for c in str(record):
        checksum += ord(c) % 7
    return checksum % 5 == 0

def generate_diagnostics(telemetry):
    # Distractor: complex but unused structure
    temp_analysis = {
        'peaks': [i for i, x in enumerate(telemetry) if x > 0.9],
        'trend': 'rising' if telemetry[-1] > telemetry[0] else 'falling',
        'noise_ratio': sum(1 for x in telemetry if 0.1 < x < 0.3) / len(telemetry)
    }

    # Real computation buried in noise
    signal_quality = analyze_signal_strength(telemetry)
    entropy_metric = compute_entropy([max(x, 1e-6) for x in telemetry])
    
    # Multiple layers of irrelevant transformations
    dummy_map = {i: math.sin(i * 0.1) for i in range(len(telemetry))}
    phantom_score = sum(math.tanh(dummy_map[i] * x) for i, x in enumerate(telemetry) if i % 3 == 0)

    # Core logic obscured by context
    base_score = signal_quality * 100
    complexity_penalty = entropy_metric * 10
    return base_score - complexity_penalty

def aggregate_metrics(log_entries, system_state):
    # Unused variables and misleading calculations
    critical_flags = [entry['status'] for entry in log_entries if entry.get('critical', False)]
    anomaly_count = sum(1 for entry in log_entries if entry['level'] == 'ANOMALY')
    
    # Red herring: checksum analysis on irrelevant field
    valid_records = [r for r in log_entries if validate_checksum(r['timestamp'])]
    spurious_index = sum(hash(r['event']) % 100 for r in valid_records) // len(valid_records) if valid_records else 0
    
    # Actual signal hidden in multiple data structures
    performance_logs = [e for e in log_entries if e['source'] == 'PERF_MONITOR']
    metrics = []
    for log in performance_logs:
        raw_telemetry = log['telemetry']
        # Real processing step
        diagnostic_value = generate_diagnostics(raw_telemetry)
        metrics.append(diagnostic_value)
    
    # Key computation
    avg_diagnostic = sum(metrics) / len(metrics) if metrics else 0
    
    # Complex conditional with decoy branches
    if system_state['mode'] == 'SAFE' and len(critical_flags) > 2:
        adjustment = -15.0
    elif system_state['health'] < 0.5 and anomaly_count > 5:
        adjustment = -25.0
    else:
        adjustment = -5.0  # This is always taken due to input state
    
    final_diagnostic = avg_diagnostic + adjustment
    
    # Dead code path (never reached due to prior logic)
    if spurious_index > 1000:
        final_diagnostic *= 1.1
    
    return final_diagnostic

# Main execution with seeded, deterministic inputs
log_entries = [
    {
        'timestamp': '2023-10-05T08:00:01Z',
        'source': 'PERF_MONITOR',
        'level': 'INFO',
        'telemetry': [0.82, 0.85, 0.91, 0.76, 0.88, 0.93, 0.84, 0.87],
        'status': 'nominal',
        'event': 'SYS_INIT'
    },
    {
        'timestamp': '2023-10-05T08:05:22Z',
        'source': 'PERF_MONITOR',
        'level': 'ANOMALY',
        'telemetry': [0.79, 0.83, 0.80, 0.85, 0.81, 0.84, 0.82, 0.86],
        'status': 'degraded',
        'event': 'LOAD_SPIKE',
        'critical': True
    },
    {
        'timestamp': '2023-10-05T08:11:45Z',
        'source': 'PERF_MONITOR',
        'level': 'ANOMALY',
        'telemetry': [0.88, 0.89, 0.92, 0.87, 0.90, 0.91, 0.88, 0.86],
        'status': 'nominal',
        'event': 'GC_CYCLE'
    }
]

system_state = {
    'mode': 'NORMAL',
    'health': 0.8,
    'uptime': 36720,
    'load_avg': [1.2, 1.5, 1.1]
}

# Execute key statement
final_diagnostic = aggregate_metrics(log_entries, system_state)
print(f"Result: {final_diagnostic}")