def analyze_system_load(raw_data, config):
    # Irrelevant preprocessing block (distractor)
    temp_buffer = [x ^ 0xAB for x in raw_data if x % 3 == 0]
    checksum = sum(temp_buffer) % 256

    # Real data transformation chain
    filtered_logs = list(filter(lambda x: x['status'] != 'idle', raw_data))
    
    # Misleading aggregation path (dead code)
    redundant_sum = 0
    for entry in filtered_logs:
        redundant_sum += len(entry['details']) * 2
    
    # Core logic disguised among distractions
    severity_map = {'low': 1, 'medium': 2, 'high': 3, 'critical': 4}
    weights = [severity_map.get(entry['priority'], 0) for entry in filtered_logs]
    
    # Decoy statistical calculation
    avg_weight = sum(weights) / len(weights) if weights else 0
    deviation = abs(avg_weight - 2.5)

    # Actual relevant computation with nested logic
    def compute_stress_score(entries, threshold_config):
        score = 0
        for e in entries:
            load = e['metrics']['cpu'] + e['metrics']['memory']
            if load > threshold_config['warning_level']:
                score += 1
                if e['source'] == 'core_node' and load > threshold_config['critical_level']:
                    score += 2
            timestamp_parts = [int(c) for c in e['timestamp'] if c.isdigit()]
            digit_sum = sum(timestamp_parts)
            if digit_sum % 7 == 0:
                score -= 1  # Counterintuitive penalty
        return max(score, 0)

    base_score = compute_stress_score(filtered_logs, config)

    # Complex distractor using enumerate and zip (irrelevant)
    indexed = list(enumerate([x['timestamp'] for x in filtered_logs]))
    paired = list(zip([x['status'] for x in filtered_logs], [x['priority'] for x in filtered_logs]))
    decoy_pairs = [(i, s, p) for i, (s, p) in enumerate(paired) if 'core' in s or p == 'critical']

    # Red herring: bit manipulation on timestamps (unused)
    magic_bits = 0
    for item in indexed:
        magic_bits ^= (item[0] << 2) | (len(item[1]) & 3)

    # Another misleading accumulation
    phantom_total = 0
    for idx, log in enumerate(filtered_logs):
        if idx % 2 == 0:
            phantom_total += len(log['details'].split())

    # Key processing function buried in noise
    def process_metrics(entries, thresholds):
        accumulator = 0
        factor = thresholds['baseline']
        
        for entry in entries:
            # Extract numeric components from string fields
            digits = [int(d) for d in entry['timestamp'] if d.isdigit()]
            time_value = sum(d ** (i+1) for i, d in enumerate(digits[-3:]))  # Weighted digit power sum
            
            metrics = entry['metrics']
            combined_util = (metrics['cpu'] * 0.6) + (metrics['memory'] * 0.4)
            
            if combined_util > thresholds['critical_level']:
                accumulator += time_value % 100
            
            # Secondary condition with case conversion distraction
            action_code = entry['details'].upper().replace(' ', '').count('ERROR')
            if action_code > 0:
                accumulator += action_code * 5
        
        # Final adjustment using dictionary operations
        status_count = {}
        for e in entries:
            key = e['status'].lower()
            status_count[key] = status_count.get(key, 0) + 1
        
        if status_count.get('active', 0) > 1:
            accumulator *= 2
            
        return int(accumulator)  # Ensure integer result

    # Unused but plausible-looking alternative path
    def legacy_analysis(data):
        total = 0
        for d in data:
            total += ord(d['status'][0]) % 32
        return total // len(data)

    # Critical execution point
    final_diagnostic = process_metrics(filtered_logs, config)
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    
    # Dead code to increase interference
    backup_mode = False
    if magic_bits > 1000:
        backup_mode = True
        secondary_diag = legacy_analysis(filtered_logs)

    return final_diagnostic

# Input data setup
log_entries = [
    {
        'timestamp': '2023-12-04T15:30:45Z',
        'status': 'active',
        'priority': 'high',
        'source': 'core_node',
        'details': 'System error detected in module A',
        'metrics': {'cpu': 85.2, 'memory': 78.1}
    },
    {
        'timestamp': '2023-12-04T16:15:22Z',
        'status': 'warning',
        'priority': 'medium',
        'source': 'edge_node',
        'details': 'High latency observed',
        'metrics': {'cpu': 92.1, 'memory': 88.3}
    },
    {
        'timestamp': '2023-12-04T16:40:10Z',
        'status': 'active',
        'priority': 'critical',
        'source': 'core_node',
        'details': 'CRITICAL FAILURE ERROR',
        'metrics': {'cpu': 96.7, 'memory': 94.2}
    }
]

system_thresholds = {
    'warning_level': 80.0,
    'critical_level': 90.0,
    'baseline': 1.5
}

# Execute main function
analyze_system_load(log_entries, system_thresholds)