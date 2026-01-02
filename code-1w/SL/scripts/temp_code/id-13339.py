import itertools

def analyze_sequence(data, threshold):
    count = 0
    temp_sum = 0
    for i, val in enumerate(data):
        if val > threshold:
            count += 1
            temp_sum += val
    return count * temp_sum

def compute_health_score(records):
    scores = []
    for r in records:
        base = r.get('cpu', 0) + r.get('mem', 0)
        adjusted = base * (1 + r.get('io_wait', 0))
        scores.append(adjusted)
    return sum(scores) / len(scores) if scores else 0

def filter_critical_events(events):
    critical = []
    for e in events:
        if e['severity'] == 'CRITICAL' and e['confirmed']:
            critical.append(e)
    return critical

def extract_timestamps(logs):
    timestamps = []
    for log in logs:
        if 'timestamp' in log:
            timestamps.append(log['timestamp'])
    return timestamps

def detect_anomalies(values, window=3):
    anomalies = []
    for i in range(len(values)):
        window_start = max(0, i - window // 2)
        window_end = min(len(values), i + window // 2 + 1)
        local_window = values[window_start:window_end]
        local_avg = sum(local_window) / len(local_window)
        if abs(values[i] - local_avg) > 0.5 * local_avg:
            anomalies.append(i)
    return anomalies

def calculate_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * __import__('math').log2(p)
    return entropy

def merge_configs(*configs):
    result = {}
    for cfg in configs:
        result.update(cfg)
    return result

def simulate_load(levels):
    simulated = []
    for lvl in levels:
        simulated.append(lvl * 1.2 + 5)
    return simulated

def generate_report_summary(entries):
    summary = {
        'total': len(entries),
        'errors': len([e for e in entries if e.get('level') == 'ERROR']),
        'warnings': len([e for e in entries if e.get('level') == 'WARNING'])
    }
    summary['ratio'] = summary['errors'] / summary['total'] if summary['total'] > 0 else 0
    return summary

def process_metrics(log_entries, thresholds):
    # Core logic begins
    cpu_readings = [entry['metrics']['cpu'] for entry in log_entries if 'metrics' in entry]
    mem_readings = [entry['metrics']['memory'] for entry in log_entries if 'metrics' in entry]
    
    high_cpu = [c for c in cpu_readings if c > thresholds['cpu']]
    high_mem = [m for m in mem_readings if m > thresholds['memory']]
    
    # Compute interaction zones using zip
    combined_load = []
    for cpu, mem in zip(cpu_readings, mem_readings[:len(cpu_readings)]):
        combined_load.append(cpu * 0.7 + mem * 0.3)
    
    spike_indices = detect_anomalies(combined_load)
    
    # Use itertools to group consecutive spikes
    sorted_spikes = sorted(spike_indices)
    groups = [list(group) for k, group in itertools.groupby(sorted_spikes, key=lambda x: x - sorted_spikes.index(x))]
    burst_count = len([g for g in groups if len(g) >= 2])
    
    # Calculate baseline statistics
    avg_cpu = sum(cpu_readings) / len(cpu_readings) if cpu_readings else 0
    avg_mem = sum(mem_readings) / len(mem_readings) if mem_readings else 0
    
    # Distractor: irrelevant health score computation
    fake_records = [{'cpu': c, 'mem': m} for c, m in zip(cpu_readings, mem_readings)]
    _ = compute_health_score(fake_records)
    
    # Key metric: stability index
    stability = 0
    for i in range(1, len(cpu_readings)):
        stability += abs(cpu_readings[i] - cpu_readings[i-1])
    stability /= len(cpu_readings) if len(cpu_readings) > 1 else 1
    
    # Secondary distractor: entropy of memory readings
    _ = calculate_entropy([int(m) for m in mem_readings])
    
    # Final diagnostic calculation
    severity_score = len(high_cpu) * 1.5 + len(high_mem) * 1.2 + burst_count * 2
    normalizing_factor = (avg_cpu + avg_mem) / 200 + 1
    final_diagnostic = int((severity_score / normalizing_factor) * 100)
    
    # Irrelevant simulation path (dead code)
    if False:
        load_levels = [10, 20, 30]
        _ = simulate_load(load_levels)
    
    return final_diagnostic

# Main execution block
if __name__ == '__main__':
    # Simulated log data
    log_data = [
        {'timestamp': 1001, 'level': 'INFO', 'metrics': {'cpu': 65.0, 'memory': 45.0, 'io_wait': 0.05}},
        {'timestamp': 1002, 'level': 'WARNING', 'metrics': {'cpu': 70.0, 'memory': 50.0, 'io_wait': 0.08}},
        {'timestamp': 1003, 'level': 'INFO', 'metrics': {'cpu': 95.0, 'memory': 85.0, 'io_wait': 0.1}},
        {'timestamp': 1004, 'level': 'ERROR', 'metrics': {'cpu': 98.0, 'memory': 88.0, 'io_wait': 0.15}},
        {'timestamp': 1005, 'level': 'INFO', 'metrics': {'cpu': 30.0, 'memory': 20.0, 'io_wait': 0.02}},
        {'timestamp': 1006, 'level': 'INFO', 'metrics': {'cpu': 92.0, 'memory': 83.0, 'io_wait': 0.12}},
        {'timestamp': 1007, 'level': 'WARNING', 'metrics': {'cpu': 60.0, 'memory': 40.0, 'io_wait': 0.04}},
    ]
    
    thresholds = {'cpu': 90.0, 'memory': 80.0}
    
    # Distractor: unused event filtering
    events = [
        {'severity': 'CRITICAL', 'confirmed': True},
        {'severity': 'WARNING', 'confirmed': True},
        {'severity': 'CRITICAL', 'confirmed': False}
    ]
    _ = filter_critical_events(events)
    
    # Distractor: unused timestamp extraction
    _ = extract_timestamps(log_data)
    
    # Distractor: configuration merge (irrelevant)
    config_a = {'timeout': 30, 'retries': 3}
    config_b = {'timeout': 45}
    _ = merge_configs(config_a, config_b)
    
    # Distractor: report generation (not used)
    _ = generate_report_summary(log_data)
    
    # Key execution point
    final_diagnostic = process_metrics(log_entries=log_data, system_thresholds=thresholds)
    
    print(f"Target result: {final_diagnostic}")