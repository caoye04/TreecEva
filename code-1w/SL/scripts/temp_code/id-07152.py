import itertools

def parse_log_entry(entry):
    parts = entry.split('|')
    timestamp = int(parts[0])
    level = parts[1]
    module = parts[2]
    msg = parts[3]
    return {
        'time': timestamp,
        'level': level,
        'module': module,
        'msg': msg,
        'is_error': level in ['ERROR', 'CRITICAL'],
        'severity': 1 if level == 'WARNING' else (5 if level == 'ERROR' else (10 if level == 'CRITICAL' else 0))
    }

def filter_relevant_logs(logs, target_module=None, min_severity=0):
    filtered = []
    for log in logs:
        if log['severity'] >= min_severity:
            if target_module is None or log['module'] == target_module:
                filtered.append(log)
    return filtered

def compute_diagnostics(logs):
    error_count = sum(1 for log in logs if log['is_error'])
    warning_count = sum(1 for log in logs if log['level'] == 'WARNING')
    total_entries = len(logs)
    avg_severity = sum(log['severity'] for log in logs) / max(total_entries, 1)
    peak_load_moment = max(log['time'] for log in logs) if logs else 0
    
    # Distractor: irrelevant statistical computation
    squared_errors = [log['severity']**2 for log in logs if log['level'] == 'ERROR']
    mse_proxy = sum(squared_errors) / max(len(squared_errors), 1) if squared_errors else 0
    
    # More distractions: unused transformations
    time_gaps = [logs[i+1]['time'] - logs[i]['time'] for i in range(len(logs)-1)]
    burst_factor = max(time_gaps) / (sum(time_gaps) / len(time_gaps)) if time_gaps else 0
    
    return {
        'errors': error_count,
        'warnings': warning_count,
        'total': total_entries,
        'average_severity': avg_severity,
        'peak_time': peak_load_moment
    }

def evaluate_module_stability(diag):
    base_score = 100
    base_score -= diag['errors'] * 8
    base_score -= diag['warnings'] * 3
    base_score -= max(0, diag['average_severity'] - 2) * 4
    if diag['average_severity'] > 5:
        base_score -= 10
    return max(1, base_score)

def generate_synthetic_metrics(stability, diagnostics):
    # Irrelevant synthetic data generation
    time_series = [stability * (1 + i * 0.05) for i in range(10)]
    smoothed = sum(time_series) / len(time_series)
    volatility = max(time_series) - min(time_series)
    return {'smoothed': smoothed, 'volatility': volatility}

def assess_system_health(logs_by_module):
    scores = {}
    all_logs = list(itertools.chain.from_iterable(logs_by_module.values()))
    global_diag = compute_diagnostics(all_logs)
    
    for module, mod_logs in logs_by_module.items():
        diag = compute_diagnostics(mod_logs)
        score = evaluate_module_stability(diag)
        synthetic = generate_synthetic_metrics(score, diag)
        scores[module] = {
            'raw_score': score,
            'adjusted': score * (0.95 if diag['peak_time'] > 1000 else 1.0),
            'meta': synthetic
        }
    
    # Dead code path - never executed due to condition
    if False and len(all_logs) > 1000:
        fallback = sum(s['raw_score'] for s in scores.values()) / len(scores)
        return {'system_status': 'overloaded', 'score': fallback}
    
    return scores

def aggregate_performance(log_entries, system_flags):
    parsed_logs = [parse_log_entry(e) for e in log_entries]
    
    # Group logs by module using dictionary operation
    logs_by_module = {}
    for log in parsed_logs:
        mod = log['module']
        if mod not in logs_by_module:
            logs_by_module[mod] = []
        logs_by_module[mod].append(log)
    
    health_scores = assess_system_health(logs_by_module)
    
    # Extract scores and apply weighting based on system flags
    weights = {
        'network': 1.2,
        'storage': 1.1,
        'compute': 0.9,
        'security': 1.5
    }
    
    final_parts = []
    for module, data in health_scores.items():
        weight = weights.get(module, 1.0)
        adjusted = data['adjusted']
        contribution = adjusted * weight
        final_parts.append(contribution)
    
    raw_final = sum(final_parts)
    
    # Apply conditional adjustment based on flag
    emergency_mode = system_flags.get('emergency_override', False)
    final_score = raw_final * (0.7 if emergency_mode else 1.0)
    
    # Red herring: unrelated post-processing
    outlier_scores = [s for s in final_parts if s > 150]
    if outlier_scores:
        correction_factor = sum(outlier_scores) / 100
        dummy_adjustment = raw_final - correction_factor  # unused
    
    # Another distraction: bit manipulation with no impact
    flag_bits = 0
    for key in system_flags:
        flag_bits ^= hash(key) & 0xF
    debug_checksum = flag_bits << 2  # unused
    
    return final_score

# Simulated input data
log_data = [
    "100|INFO|network|Connection established",
    "150|WARNING|network|Latency spike detected",
    "200|ERROR|network|Packet loss occurred",
    "250|INFO|storage|Disk write OK",
    "300|CRITICAL|storage|Array failure imminent",
    "350|WARNING|storage|High IOPS latency",
    "400|INFO|compute|Job completed",
    "450|WARNING|compute|Memory pressure",
    "500|INFO|security|Access granted",
    "550|CRITICAL|security|Intrusion detected"
]

flags = {
    'maintenance_window': True,
    'trace_logging': False,
    'debug_mode': True
}

# Key execution point
final_score = aggregate_performance(log_data, flags)
print(f"Target result: {final_score}")