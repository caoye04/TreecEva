import itertools

# Simulated telemetry data from distributed sensor array
def collect_sensor_data():
    return [
        {'node': 'A1', 'temp': 23.5, 'load': 0.68, 'status': 1},
        {'node': 'B2', 'temp': 26.3, 'load': 0.82, 'status': 1},
        {'node': 'C3', 'temp': 28.1, 'load': 0.91, 'status': 1},
        {'node': 'D4', 'temp': 22.7, 'load': 0.54, 'status': 1},
        {'node': 'E5', 'temp': 31.0, 'load': 0.95, 'status': 0}
    ]

# Irrelevant auxiliary function - dead code path
def analyze_network_latency(samples):
    avg = sum([s['latency'] for s in samples]) / len(samples)
    return avg * 0.87

# Decoy transformation - never used
transform_stream = lambda data: [\
    {k: (v * 1.05 if k == 'temp' else v) for k, v in item.items()} \
    for item in data if item['status'] == 1]

# System-wide thresholds for health checks
system_thresholds = {
    'overload': 0.85,
    'overheat': 30.0,
    'min_nodes': 3
}

# Secondary metrics with red herring variables
historical_peaks = {
    'max_load': 0.99,
    'max_temp': 35.6,
    'event_count': 142
}

# Misleading diagnostic flag - looks important but unused
emergency_override = False

# Data preprocessing with distractor operations
def normalize_entries(raw_logs):
    normalized = []
    total_weight = 0.0
    
    for entry in raw_logs:
        # Compute irrelevant weight factor
        weight = entry['load'] ** 2 + (entry['temp'] / 100)
        total_weight += weight
        
        # Transform status to descriptive string (not used later)
        entry['status_str'] = 'active' if entry['status'] else 'failed'
        
        # Augment with dummy rolling average
        entry['rolling_load'] = entry['load'] * 0.7 + 0.1
        
        normalized.append(entry)
    
    # Spurious normalization - not used
    for e in normalized:
        e['weighted_score'] = (e['load'] + e['temp'] / 100) / total_weight
    
    return normalized

# Complex filtering using multiple concepts
def filter_active_nodes(entries):
    # Use itertools to create artificial complexity
    sorted_entries = sorted(entries, key=lambda x: x['load'], reverse=True)
    grouped = {k: list(v) for k, v in itertools.groupby(sorted_entries, key=lambda x: x['status'])}
    
    active_set = grouped.get(1, [])
    
    # Apply secondary filter - temperature threshold
    filtered = [e for e in active_set if e['temp'] < system_thresholds['overheat']]
    
    # Dead branch - condition never met due to data
    if len(active_set) > historical_peaks['event_count']:
        filtered = active_set  # would bypass temp filter
    
    return filtered

# Core metric calculation with hidden logic chain
def calculate_stability_index(nodes):
    if len(nodes) < system_thresholds['min_nodes']:
        return 0.0
    
    # Primary computation disguised among distractions
    load_products = 1.0
    temp_sum = 0.0
    
    for node in nodes:
        # Real contribution to answer
        load_products *= (1 + node['load'])  # compound effect
        temp_sum += node['temp'] ** 0.5
        
        # Fake diagnostics
        node['anomaly_score'] = (node['load'] > 0.9) * (node['temp'] > 29.0)
    
    # Actual formula used for answer
    index = load_products * (temp_sum / len(nodes))
    
    # Multiple alternative calculations that are not taken
    alt_index_v1 = sum(n['load'] for n in nodes) * 10
    alt_index_v2 = max(n['temp'] for n in nodes) * len(nodes)
    
    return round(index, 6)

# Final processing with lambda abstraction
def process_metrics(logs, thresholds):
    # Step 1: Normalize logs (with side effects)
    cleaned_logs = normalize_entries(logs)
    
    # Step 2: Filter operational nodes
    valid_nodes = filter_active_nodes(cleaned_logs)
    
    # Step 3: Calculate core stability metric
    stability = calculate_stability_index(valid_nodes)
    
    # Step 4: Apply policy rules (mostly irrelevant)
    compliance_flags = []
    for node in cleaned_logs:
        overload = node['load'] > thresholds['overload']
        overheat = node['temp'] > thresholds['overheat']
        compliance_flags.append(not (overload or overheat))
    
    # Decoy aggregation
    final_compliance = all(compliance_flags)
    peak_load_node = max(cleaned_logs, key=lambda x: x['load'])
    
    # Critical result - only this matters
    diagnostic_code = int(stability * 100) % 10000
    final_diagnostic = diagnostic_code + 1000  # shift base
    
    # Unused complex structure
    report_summary = {
        'nodes_analyzed': len(cleaned_logs),
        'nodes_operational': len([n for n in cleaned_logs if n['status']]),
        'stability_raw': stability,
        'peak_load': peak_load_node['load'],
        'diagnostic_key': f'DIAG-{diagnostic_code}'
    }
    
    return final_diagnostic

# Execution flow
if __name__ == '__main__':
    raw_entries = collect_sensor_data()
    
    # Unused network analysis
    # network_samples = [{'latency': 45}, {'latency': 52}]
    # latency_baseline = analyze_network_latency(network_samples)
    
    final_diagnostic = process_metrics(raw_entries, system_thresholds)
    print(f"Target result: {final_diagnostic}")