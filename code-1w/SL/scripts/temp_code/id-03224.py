from collections import defaultdict, Counter

# Simulated system log analyzer with decoy computations and red herrings
def analyze_system_health():
    # Core data structures
    log_entries = [
        {'level': 'ERROR', 'module': 'auth', 'timestamp': 1712054400, 'duration_ms': 150},
        {'level': 'INFO', 'module': 'network', 'timestamp': 1712054401, 'duration_ms': 45},
        {'level': 'WARNING', 'module': 'storage', 'timestamp': 1712054402, 'duration_ms': 200},
        {'level': 'ERROR', 'module': 'auth', 'timestamp': 1712054403, 'duration_ms': 300},
        {'level': 'DEBUG', 'module': 'network', 'timestamp': 1712054404, 'duration_ms': 10},
        {'level': 'ERROR', 'module': 'storage', 'timestamp': 1712054405, 'duration_ms': 500}
    ]

    # Irrelevant statistical counters (distractors)
    total_entries = len(log_entries)
    debug_count = sum(1 for e in log_entries if e['level'] == 'DEBUG')
    info_count = sum(1 for e in log_entries if e['level'] == 'INFO')
    warning_count = sum(1 for e in log_entries if e['level'] == 'WARNING')
    duration_average = sum(e['duration_ms'] for e in log_entries) / total_entries

    # Unused transformation (dead code path)
    def unused_transform(data):
        return [d['duration_ms'] * 2 for d in data if d['level'] != 'DEBUG']

    # Misleading intermediate calculation (red herring)
    anomaly_score = 0
    for entry in log_entries:
        if entry['duration_ms'] > 100:
            anomaly_score += 1
    anomaly_score *= 10  # Looks important but not used in final result

    # Decoy function that looks relevant but isn't called
    def calculate_uptime(timestamps):
        return max(timestamps) - min(timestamps)

    # System thresholds (some are irrelevant)
    system_threshold = {
        'critical_duration': 250,
        'retry_limit': 3,
        'timeout_grace_period': 50,
        'max_concurrent_errors': 2
    }

    # Hidden diagnostic logic buried in multiple layers
    module_error_count = defaultdict(int)
    critical_durations = []

    for idx, entry in enumerate(log_entries):
        if entry['level'] == 'ERROR':
            module_error_count[entry['module']] += 1
            if entry['duration_ms'] > system_threshold['critical_duration']:
                critical_durations.append(entry['duration_ms'])

    # Complex conditional expression with distractors
    error_distribution = Counter([e['module'] for e in log_entries if e['level'] == 'ERROR'])
    has_critical_failure = any(count >= system_threshold['max_concurrent_errors'] 
                              for count in module_error_count.values())

    # Secondary irrelevant analysis (distractor)
    timestamp_gaps = [log_entries[i+1]['timestamp'] - log_entries[i]['timestamp'] 
                     for i in range(len(log_entries)-1)]
    avg_gap = sum(timestamp_gaps) / len(timestamp_gaps)

    # Key processing function with embedded logic
    def process_metrics(entries, config):
        # Local variables to increase cognitive load
        temp_results = []
        module_contributions = defaultdict(float)
        
        for i, record in enumerate(entries):
            weight = 1.0
            # Conditional expressions based on multiple factors
            if record['level'] == 'ERROR':
                weight *= 2.0
            if record['duration_ms'] > 100:
                weight *= 1.5
            if record['module'] == 'auth':
                weight *= 1.2  # Higher impact for auth module
            
            module_contributions[record['module']] += weight
            
            # Store intermediate weighted values (some never used)
            temp_results.append({'index': i, 'weight': weight, 'module': record['module']})
        
        # Real computation buried here
        base_score = 0
        for module, contribution in module_contributions.items():
            if module == 'auth':
                base_score += int(contribution * 100)
            elif module == 'storage':
                base_score += int(contribution * 80)
            else:
                base_score += int(contribution * 60)
        
        # Final adjustment using critical durations (only this affects output)
        penalty = 0
        for dur in critical_durations:  # This list defined outside!
            penalty += dur // 50
        
        # The actual answer derivation
        result = base_score - penalty
        
        # Dead code: alternative paths not taken
        if False:  # Simulate unreachable logic
            fallback = sum(module_contributions.values()) * 10
            result = int(fallback) if result < 0 else result
            
        return result

    # Red herring: another unused function
    def generate_report(data):
        return {"summary": "skipped", "status": "inactive"}

    # Critical execution point
    final_diagnostic = process_metrics(log_entries, system_threshold)

    # Print required for traceability
    print(f"Result: {final_diagnostic}")

    # Additional irrelevant cleanup (distraction)
    del module_error_count['auth']  # Looks like it matters

    return final_diagnostic

# Execute and capture result
analyze_system_health()