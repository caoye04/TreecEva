import math

# Simulated system log analyzer with decoy metrics
def analyze_response_time(timestamps):
    if not timestamps:
        return 0
    avg = sum(timestamps) / len(timestamps)
    variance = sum((t - avg) ** 2 for t in timestamps) / len(timestamps)
    # Irrelevant computation (decoy)
    peak_load = max(timestamps) * len(timestamps) if timestamps else 0
    return avg

# Dead function - never called but looks important
def calculate_throughput(events, duration):
    if duration <= 0:
        return 0.0
    ops_per_sec = len(events) / duration
    overhead = 0.1 * ops_per_sec
    return ops_per_sec - overhead

# Bit manipulation red herring
def scramble_id(user_id):
    xored = user_id ^ 0xFFFF
    shifted = ((xored << 3) & 0xFFFF) | (xored >> 13)
    masked = shifted & 0xBEEF
    return masked

def filter_anomalies(records):
    # Linear search through records to find anomalies
    anomalies = []
    for r in records:
        if r.get('status') == 'ERROR' and r.get('retry_count', 0) > 2:
            anomalies.append(r)
    # Misleading transformation (not used later)
    critical_ids = [scramble_id(rec['id']) for rec in anomalies]
    return anomalies

def compute_stability_index(metrics):
    base_score = 0.0
    weights = {'cpu': 0.3, 'mem': 0.4, 'disk': 0.2, 'net': 0.1}
    
    # Some metrics are missing intentionally to test logic
    for key in weights:
        if key in metrics:
            base_score += metrics[key] * weights[key]
    
    # Apply non-linear penalty (relevant)
    if 'latency' in metrics and metrics['latency'] > 50:
        base_score *= 0.7
    
    # Decoy calculation
    synthetic_boost = sum(math.sin(metrics.get(k, 0)) for k in ['cpu', 'mem']) * 0.05
    
    return round(base_score, 4)

def evaluate_performance(log_entries):
    # Key processing pipeline
    filtered_logs = [e for e in log_entries if e['level'] != 'DEBUG']
    
    # Extract response times only from INFO or ERROR entries
    response_times = []
    error_count = 0
    for entry in filtered_logs:
        if 'response_ms' in entry:
            response_times.append(entry['response_ms'])
        if entry['level'] == 'ERROR':
            error_count += 1
    
    avg_response = analyze_response_time(response_times)
    
    # Stability component
    mock_metrics = {
        'cpu': 68.5,
        'mem': 72.1,
        'latency': avg_response,
        'disk': 45.0,
        'net': 80.2
    }
    stability = compute_stability_index(mock_metrics)
    
    # Weighted scoring with lambda-based adjustment factor
    adjuster = lambda x: 1.0 if x < 100 else 0.85 if x < 200 else 0.6
    response_factor = adjuster(avg_response)
    
    # Final score calculation (this is the real answer path)
    raw_score = (100 - error_count * 5) * stability * response_factor
    final_score = int(round(raw_score))
    
    # Dead code branch - unreachable due to logic above
    if final_score < 0:
        final_score = 0
    elif final_score > 1000:
        final_score = 1000  # Clamped, though unnecessary here
        
    return final_score

# Simulated log data (real input)
log_data = [
    {'id': 101, 'level': 'INFO', 'response_ms': 85, 'retry_count': 0},
    {'id': 102, 'level': 'DEBUG', 'details': 'ignored'},  # filtered out
    {'id': 103, 'level': 'ERROR', 'response_ms': 190, 'retry_count': 3},
    {'id': 104, 'level': 'INFO', 'response_ms': 75, 'retry_count': 0},
    {'id': 105, 'level': 'ERROR', 'response_ms': 210, 'retry_count': 1},
    {'id': 106, 'level': 'INFO', 'response_ms': 95, 'retry_count': 0},
    {'id': 107, 'level': 'INFO', 'response_ms': 65, 'retry_count': 0},
]

# Trigger evaluation
target_result = evaluate_performance(log_data)
print(f"Result: {target_result}")