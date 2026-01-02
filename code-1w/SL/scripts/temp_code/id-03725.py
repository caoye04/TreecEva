from collections import defaultdict, Counter

def analyze_node_health(sensor_data, thresholds):
    health_flags = []
    temp_alerts = 0
    for entry in sensor_data:
        node_id = entry['id']
        temperature = entry['temp']
        voltage = entry['voltage']
        timestamp = entry['ts']
        
        # Irrelevant computation: power cycle counter (unused)
        cycle_counter = (timestamp // 3600) % 24
        
        if temperature > thresholds['overheat']:
            health_flags.append((node_id, 'CRITICAL'))
            temp_alerts += 1
        elif temperature > thresholds['warning']:
            health_flags.append((node_id, 'WARNING'))
        else:
            health_flags.append((node_id, 'OK'))
    
    # Dead code path: never accessed
    def unused_diagnostic():
        return sum(temp_alerts * 2 for _ in range(3))
    
    return health_flags

def compute_stability_index(events):
    event_count = defaultdict(int)
    severity_score = 0
    
    for e in events:
        event_count[e['type']] += 1
    
    for typ, cnt in event_count.items():
        if typ == 'ERROR':
            severity_score += cnt * 10
        elif typ == 'WARN':
            severity_score += cnt * 3
    
    # Distractor: irrelevant normalization
    total = sum(event_count.values())
    if total > 0:
        normalized = severity_score / total
    else:
        normalized = 0
    
    # This value is misleading but not used in final result
    stability_index = 100 - min(severity_score, 95)
    return stability_index

def evaluate_response_time(latencies):
    sorted_latencies = sorted(latencies)
    n = len(sorted_latencies)
    if n == 0:
        return 0.0
    median = sorted_latencies[n // 2]
    avg = sum(latencies) / n
    peak = max(latencies)
    
    # Decoy calculation
    jitter = (peak - min(latencies)) * 0.5
    
    # Only this is actually returned and used
    return avg * 0.8 + median * 0.2

def aggregate_metrics(scores, load):
    base = sum(scores)
    adjustment = 0
    
    if load > 80:
        adjustment = -15
    elif load > 60:
        adjustment = -5
    else:
        adjustment = 3
    
    # Complex logic chain step 1
    weighted_sum = base * 1.1 + adjustment
    
    # Step 2
    if weighted_sum > 120:
        weighted_sum = 120
    
    # Step 3
    weighted_sum = max(weighted_sum, 10)
    
    # Step 4: apply decay factor (not arbitrary)
    decay_factor = 0.93
    final_value = int(weighted_sum * decay_factor)
    
    # Step 5: parity correction
    if final_value % 2 == 0:
        final_value -= 1
    
    # Step 6: floor at minimum operational threshold
    final_value = max(final_value, 15)
    
    return final_value

def main():
    # Simulated sensor inputs (real data)
    sensor_readings = [
        {'id': 'N01', 'temp': 78, 'voltage': 3.2, 'ts': 1623456780},
        {'id': 'N02', 'temp': 85, 'voltage': 3.3, 'ts': 1623456781},
        {'id': 'N03', 'temp': 73, 'voltage': 3.1, 'ts': 1623456782},
        {'id': 'N04', 'temp': 91, 'voltage': 3.4, 'ts': 1623456783},
        {'id': 'N05', 'temp': 69, 'voltage': 3.0, 'ts': 1623456784}
    ]
    
    # Event logs with severity levels
    system_events = [
        {'type': 'INFO', 'code': 1001},
        {'type': 'WARN', 'code': 2003},
        {'type': 'ERROR', 'code': 5001},
        {'type': 'ERROR', 'code': 5002},
        {'type': 'WARN', 'code': 2005},
        {'type': 'WARN', 'code': 2001}
    ]
    
    # Network performance data
    response_latencies = [120, 89, 95, 134, 76, 110, 98, 105]
    
    # Threshold settings
    limits = {
        'overheat': 80,
        'warning': 75,
        'voltage_min': 3.0
    }
    
    # Irrelevant counters
    diagnostic_run_id = hash('diagnostics_2023') % 10000
    audit_token = bin(diagnostic_run_id ^ 0xABCD)
    
    # Step 1: Health analysis
    node_statuses = analyze_node_health(sensor_readings, limits)
    
    # Step 2: Extract reliability indicators
    reliability_counter = Counter(status for _, status in node_statuses)
    reliable_nodes = reliability_counter['OK']
    warning_nodes = reliability_counter['WARNING']
    critical_nodes = reliability_counter['CRITICAL']
    
    # Step 3: Compute derived metrics (only some are used)
    system_health_score = 50 + (reliable_nodes * 5) - (warning_nodes * 2) - (critical_nodes * 8)
    
    # Step 4: Stability from event logs
    raw_stability = compute_stability_index(system_events)
    
    # Step 5: Performance metric
    avg_response = evaluate_response_time(response_latencies)
    performance_bonus = 10 if avg_response < 100 else 0
    
    # Step 6: Load factor (simulated)
    system_load = 68  # Between 60-80 → small penalty
    
    # Step 7: Build reliability scores list (key input)
    reliability_scores = [
        system_health_score,           # from node health
        raw_stability,                # from event analysis
        45,                           # placeholder calibration constant
        performance_bonus             # from latency
    ]
    
    # Step 8: Aggregate metrics — key execution point
    final_diagnostic = aggregate_metrics(reliability_scores, system_load)
    
    # Irrelevant post-processing
    report_hash = ''.join([str(final_diagnostic % 10) for _ in range(5)])
    metadata_trace = {"version": "v2.3", "nodes": 5, "final": final_diagnostic + 1000}  # decoy
    
    # Correct output format
    print(f"Target result: {final_diagnostic}")

if __name__ == "__main__":
    main()