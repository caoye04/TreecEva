from collections import defaultdict, Counter

# Simulated system log analysis with red herrings and complex processing
def analyze_log_patterns(log_entries):
    severity_count = defaultdict(int)
    event_types = set()
    temp_buffer = []
    cumulative_score = 0

    for entry in log_entries:
        parts = entry.split(' | ')
        level = parts[1]
        event = parts[2].split('(')[0]
        
        # Real logic: count severity levels
        severity_count[level] += 1
        
        # Distractor: collecting event types (not used later)
        event_types.add(event)
        
        # Distractor: temp buffer accumulation (dead code path)
        if 'ERROR' in level:
            temp_buffer.append(entry)

        # Distractor: fake scoring mechanism
        fake_impact = len(event) * (10 if 'CRITICAL' in level else 1)
        cumulative_score += fake_impact  # Not actually used

    return severity_count

# Irrelevant helper function (decoy)
def compute_network_latency(timestamps):
    if not timestamps:
        return 0.0
    diffs = [t2 - t1 for t1, t2 in zip(timestamps, timestamps[1:])]
    return sum(diffs) / len(diffs) if diffs else 0.0

# Core processing function with key logic buried
def evaluate_system_health(metrics, config):
    baseline = config.get('baseline', 100)
    multiplier = config.get('multiplier', 1.5)
    decay = config.get('decay', 0.1)
    
    # Real computation starts here
    adjusted_values = []
    for i, val in enumerate(metrics):
        if i % 2 == 0:
            adjusted_values.append(val * multiplier)
        else:
            adjusted_values.append(val - decay * baseline)
    
    # Distractor: unused transformation
    inverted = [1.0 / (x + 1) for x in metrics if x > 0]
    
    return adjusted_values

# Main diagnostic processor
def process_metrics(log_data, threshold_map):
    # Extract time series data from logs
    raw_metrics = []
    timestamps = []
    
    for line in log_data:
        time_part = int(line.split('|')[0])
        metric_str = line.split(',')[-1]
        try:
            raw_metrics.append(float(metric_str))
            timestamps.append(time_part)
        except:
            continue
    
    # Distractor: call irrelevant function
    avg_latency = compute_network_latency(timestamps)
    
    # Real logic: analyze log severity distribution
    severity_freq = analyze_log_patterns(log_data)
    critical_count = severity_freq.get('CRITICAL', 0)
    error_count = severity_freq.get('ERROR', 0)
    warning_count = severity_freq.get('WARNING', 0)
    
    # Distractor: unused frequency counter
    type_counter = Counter([line.split('|')[2].split('(')[0] for line in log_data])
    
    # Configuration for evaluation
    config = {
        'baseline': 80 + warning_count,
        'multiplier': 1.2 + (0.1 * critical_count),
        'decay': 0.05
    }
    
    # Process metrics through evaluation pipeline
    processed = evaluate_system_health(raw_metrics, config)
    
    # Key computation: weighted diagnostic score
    base_diagnostic = sum(processed) * (1 + 0.2 * error_count)
    
    # Apply thresholds from map
    safety_margin = threshold_map.get('margin', 10)
    risk_factor = threshold_map.get('risk', 1.0)
    
    # Final diagnostic calculation (this is the actual answer)
    final_diagnostic = int(base_diagnostic - safety_margin * risk_factor)
    
    # Distractor: alternate path never taken
    if len(timestamps) > 1000:
        final_diagnostic *= 0.9  # Unused condition
    
    # Print result as required
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulated input data
log_entries = [
    "1678874321 | CRITICAL | DISK_FAILURE(detected) | load=95.2",
    "1678874322 | ERROR | MEMORY_LEAK(identifiable) | load=88.7",
    "1678874323 | WARNING | HIGH_CPU_USAGE(threshold_met) | load=76.3",
    "1678874324 | INFO | SERVICE_RESTART(attempted) | load=45.1",
    "1678874325 | CRITICAL | NETWORK_OUTAGE(detected) | load=92.4",
    "1678874326 | ERROR | AUTHENTICATION_FAIL(repeated) | load=83.6",
    "1678874327 | WARNING | IO_BOTTLENECK(pending) | load=71.8",
    "1678874328 | DEBUG | GC_ACTIVITY(active) | load=33.9",
    "1678874329 | CRITICAL | DATABASE_CORRUPTION(found) | load=97.1",
    "1678874330 | ERROR | FILESYSTEM_FULL(imminent) | load=89.2"
]

thresholds = {
    'margin': 25,
    'risk': 2.0,
    'buffer': 500  # unused
}

# Execute main function
final_diagnostic = process_metrics(log_entries, thresholds)