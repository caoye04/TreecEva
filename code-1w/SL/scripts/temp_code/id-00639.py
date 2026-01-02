import itertools

def analyze_sequence(data, window_size):
    # Irrelevant helper function with dead logic
    if len(data) < window_size:
        return [0]
    averages = [sum(data[i:i+window_size]) / window_size for i in range(len(data) - window_size + 1)]
    return [x for x in averages if x > 0.5]

def generate_checksum(sequence):
    # Distractor function - never called in execution path
    checksum = 0
    for idx, val in enumerate(sequence):
        checksum ^= (val * (idx + 1)) % 256
    return checksum

def filter_anomalies(entries, threshold=75):
    # Misleading preprocessing step
    filtered = []
    for entry in entries:
        if entry['cpu'] < threshold and entry['memory'] < threshold:
            filtered.append(entry)
    return filtered or [{'cpu': 0, 'memory': 0, 'disk_io': 0}]

def compute_entropy(values):
    # Unused mathematical distraction
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values if v > 0]
    from math import log2
    return -sum(p * log2(p) for p in probs)

def main_pipeline():
    # Simulated system telemetry log entries
    log_entries = [
        {'timestamp': 1001, 'cpu': 68, 'memory': 72, 'disk_io': 12, 'network': 45},
        {'timestamp': 1002, 'cpu': 74, 'memory': 65, 'disk_io': 15, 'network': 53},
        {'timestamp': 1003, 'cpu': 81, 'memory': 78, 'disk_io': 22, 'network': 61},
        {'timestamp': 1004, 'cpu': 69, 'memory': 70, 'disk_io': 13, 'network': 47},
        {'timestamp': 1005, 'cpu': 76, 'memory': 82, 'disk_io': 25, 'network': 67}
    ]

    # System thresholds - relevant configuration
    system_thresholds = {
        'critical_cpu': 80,
        'critical_memory': 80,
        'high_disk_io': 20,
        'elevated_network': 60
    }

    # Dead code branch - looks important but unused
    backup_config = {
        'sampling_rate': 100,
        'buffer_limit': 1024,
        'retry_attempts': 3,
        'timeout_ms': 500
    }

    # Irrelevant data transformation chain
    timestamps = [entry['timestamp'] for entry in log_entries]
    cpu_readings = [entry['cpu'] for entry in log_entries]
    memory_readings = [entry['memory'] for entry in log_entries]
    disk_readings = [entry['disk_io'] for entry in log_entries]
    network_readings = [entry['network'] for entry in log_entries]

    # Apply irrelevant sliding window analysis
    smoothed_cpu = analyze_sequence(cpu_readings, 2)
    smoothed_mem = analyze_sequence(memory_readings, 2)

    # Fake entropy calculation - red herring
    cpu_entropy = compute_entropy(cpu_readings)
    mem_entropy = compute_entropy(memory_readings)

    # Distractor: zipping unrelated sequences
    paired_metrics = list(zip(smoothed_cpu, smoothed_mem))
    index_offset = list(enumerate(paired_metrics))

    # Real processing begins here - buried among distractions
    high_cpu_events = [e for e in log_entries if e['cpu'] >= system_thresholds['critical_cpu']]
    high_memory_events = [e for e in log_entries if e['memory'] >= system_thresholds['critical_memory']]
    high_disk_events = [e for e in log_entries if e['disk_io'] >= system_thresholds['high_disk_io']]
    high_network_events = [e for e in log_entries if e['network'] >= system_thresholds['elevated_network']]

    def process_metrics(entries, thresholds):
        # Core logic hidden in nested structure
        alert_flags = 0
        severity_weights = {
            'cpu': 4,
            'memory': 3,
            'disk_io': 2,
            'network': 1
        }
        
        # Use of conditional expression and itertools.chain
        all_high = list(itertools.chain(
            [('cpu', e['timestamp']) for e in high_cpu_events],
            [('memory', e['timestamp']) for e in high_memory_events]
        ))
        
        # Additional filtering with misleading early return possibility
        if not all_high:
            return -1  # Dead path - won't execute
            
        # Real computation: count cross-resource correlations
        critical_coincidence = 0
        for entry in entries:
            resource_count = 0
            if entry['cpu'] >= thresholds['critical_cpu']:
                resource_count += 1
            if entry['memory'] >= thresholds['critical_memory']:
                resource_count += 1
            if entry['disk_io'] >= thresholds['high_disk_io']:
                resource_count += 1
            if entry['network'] >= thresholds['elevated_network']:
                resource_count += 1
            
            # Only count if multiple thresholds are crossed
            if resource_count >= 2:
                critical_coincidence += resource_count

        # Final diagnostic score built from weighted patterns
        base_score = len(high_cpu_events) * severity_weights['cpu']
        base_score += len(high_memory_events) * severity_weights['memory']
        base_score += len(high_disk_events) * severity_weights['disk_io']
        base_score += len(high_network_events) * severity_weights['network']
        
        # Apply coincidence multiplier only if co-occurrence exists
        multiplier = 2 if critical_coincidence > 0 else 1
        final_score = base_score * multiplier
        
        # One last conditional adjustment
        final_score = final_score + 10 if any(e['disk_io'] > 24 for e in log_entries) else final_score - 5
        
        return final_score

    # Key statement containing the target variable
    final_diagnostic = process_metrics(log_entries, system_thresholds)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")
    
    # Return for potential future use (not used)
    return {
        'diagnostic_code': final_diagnostic,
        'anomaly_count': len(high_cpu_events) + len(high_memory_events),
        'raw_entropy': cpu_entropy + mem_entropy
    }

if __name__ == '__main__':
    main_pipeline()