from collections import defaultdict, Counter

# Simulated telemetry data from distributed sensors
telemetry_streams = [
    [12, 15, 14, 13, 45, 16, 12, 11, 10, 9],
    [8, 9, 10, 52, 11, 13, 14, 15, 16, 17],
    [20, 19, 18, 17, 16, 15, 14, 13, 12, 63],
    [25, 24, 23, 22, 21, 20, 19, 18, 17, 16]
]

# Irrelevant baseline model (distractor)
def calculate_entropy(values):
    freq = Counter(values)
    total = len(values)
    entropy = 0
    for count in freq.values():
        p = count / total
        if p > 0:
            entropy -= p * __import__('math').log2(p)
    return round(entropy, 3)

# Unused diagnostic function (dead code path)
def analyze_pattern(sequence):
    trend = []
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend.append(1)
        elif sequence[i] < sequence[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    return trend

# Misleading normalization function (decoy)
def normalize_readings(data_stream):
    max_val = max(data_stream)
    return [x / max_val for x in data_stream]

# Auxiliary transformation with partial relevance
def extract_anomalies(stream, threshold=50):
    anomalies = []
    for idx, val in enumerate(stream):
        if val > threshold:
            anomalies.append((idx, val))
    return anomalies

# Complex preprocessing pipeline with distractors
def preprocess_logs(raw_streams):
    processed = []
    stats_log = defaultdict(int)
    
    for i, stream in enumerate(raw_streams):
        # Real processing step
        filtered = [x for x in stream if x < 40]  # Ignore overflow values
        smoothed = list(map(lambda x: x * 0.9, filtered))
        
        # Distractor: unused entropy calculation
        entropy_val = calculate_entropy(stream)
        stats_log[f'stream_{i}_entropy'] = entropy_val
        
        # Distractor: normalization not used later
        normalized = normalize_readings(stream)
        
        # Real step: store cleaned data
        processed.append(smoothed)
    
    # Fake aggregation (not actually used)
    fake_aggregate = sum(stats_log.values())
    
    return processed

# Core logic buried in multiple layers
def build_log_entries(cleaned_streams):
    entries = []
    for stream_idx, stream in enumerate(cleaned_streams):
        entry = {
            'stream_id': f'S{stream_idx}',
            'readings': stream,
            'timestamp': 1623450000 + stream_idx * 100,
            'diagnostics': {}
        }
        
        # Real diagnostic: average reading
        avg_reading = sum(stream) / len(stream) if stream else 0
        entry['diagnostics']['avg'] = round(avg_reading, 2)
        
        # Real: peak detection (below threshold)
        peak = max(stream) if stream else 0
        entry['diagnostics']['peak'] = peak
        
        # Distractor: inject meaningless metadata
        entry['version'] = 'v2.1'
        entry['redundant_flag'] = (len(stream) % 2 == 0)
        
        entries.append(entry)
    
    return entries

# Threshold policy manager (mixed relevant/irrelevant)
def load_system_thresholds():
    thresholds = {
        'critical_load': 35.0,
        'warning_level': 25.0,
        'safe_range': 20.0,
        'decay_factor': 0.85,
        'heartbeat_interval': 5  # unused
    }
    
    # Distractor computation
    temp_vals = [35.0, 25.0, 20.0]
    mid_point = sum(temp_vals) / 3
    thresholds['midpoint_proxy'] = round(mid_point, 2)  # unused
    
    return thresholds

# Main processing with early returns and filtering
def evaluate_health_status(metrics, policy):
    if not metrics or 'avg' not in metrics:
        return 'UNKNOWN'
    
    avg = metrics['avg']
    peak = metrics.get('peak', 0)
    
    if avg > policy['critical_load']:
        return 'CRITICAL'
    elif avg > policy['warning_level']:
        return 'WARNING'
    elif peak > policy['warning_level'] * 1.2:
        return 'ELEVATED'
    else:
        return 'STABLE'

# Data correlation across streams (with red herring)
def correlate_events(log_entries):
    time_gaps = []
    for i in range(1, len(log_entries)):
        gap = log_entries[i]['timestamp'] - log_entries[i-1]['timestamp']
        time_gaps.append(gap)
    
    # This is calculated but never used (misleading intermediate)
    avg_gap = sum(time_gaps) / len(time_gaps) if time_gaps else 0
    return time_gaps  # returned but irrelevant to final result

# Final metric processor with key logic
def process_metrics(log_entries, system_thresholds):
    results = []
    
    # Correlation called but result ignored (distraction)
    _ = correlate_events(log_entries)
    
    for entry in log_entries:
        status = evaluate_health_status(entry['diagnostics'], system_thresholds)
        
        # Real transformation: decay-adjusted score
        raw_avg = entry['diagnostics']['avg']
        decay_factor = system_thresholds['decay_factor']
        adjusted_score = raw_avg * decay_factor
        
        # Only certain statuses contribute
        if status in ['WARNING', 'ELEVATED', 'CRITICAL']:
            results.append(adjusted_score)
        
        # Dead branch (never reached due to logic above)
        if status == 'MYTHICAL_STATE':  
            results.append(999)
    
    # Final computation
    if results:
        # Weighted emphasis on worst-case
        base = sum(results)
        modifier = len([r for r in results if r > 20])
        final_value = int(base * (1.1 + 0.1 * modifier))
    else:
        final_value = 100
    
    # Key variable assignment
    final_diagnostic = final_value + 5  # Final offset
    
    return final_diagnostic

# Execution flow
if __name__ == '__main__':
    # Step 1: Preprocess raw telemetry
    cleaned_data = preprocess_logs(telemetry_streams)
    
    # Step 2: Build structured log entries
    log_entries = build_log_entries(cleaned_data)
    
    # Step 3: Load system policies
    system_thresholds = load_system_thresholds()
    
    # Step 4: Compute final diagnostic score
    final_diagnostic = process_metrics(log_entries, system_thresholds)
    
    # Output result
    print(f"Result: {final_diagnostic}")