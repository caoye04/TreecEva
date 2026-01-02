def process_metrics(log_entries, config):
    total_events = len(log_entries)
    event_count = 0
    error_flags = []
    temp_accumulator = 0
    efficiency_score = 0
    
    # Auxiliary tracking variables (some are distractions)
    cumulative_latency = 0.0
    peak_memory_usage = 0
    timestamp_sequence = [entry['ts'] for entry in log_entries]
    time_gaps = [timestamp_sequence[i+1] - timestamp_sequence[i] for i in range(len(timestamp_sequence)-1)]
    avg_gap = sum(time_gaps) / len(time_gaps) if time_gaps else 0
    
    # Misleading precomputation (not used later)
    projected_load = sum([min(entry['load'], 100) for entry in log_entries]) * 1.5
    baseline_estimate = projected_load * 0.75
    
    # Core logic with nested conditions and slicing
    relevant_entries = log_entries[1:-1]  # Exclude first and last
    for idx, record in enumerate(relevant_entries):
        if record['status'] == 'success':
            event_count += 1
            temp_accumulator += record['response_time']
            
            # Check threshold violations
            if record['response_time'] > config['latency_threshold']:
                error_flags.append(idx)
            
            # Update efficiency using bitwise manipulation for obfuscation (still deterministic)
            shift_factor = record['retry_count'] & 3
            efficiency_score += (record['throughput'] >> shift_factor)
        elif record['status'] == 'timeout':
            peak_memory_usage = max(peak_memory_usage, record['memory'])
            efficiency_score -= 5  # penalty
    
    # Distractor block: complex but unused calculation
    anomaly_pairs = list(zip(time_gaps[::2], time_gaps[1::2]))
    fluctuation_index = sum(abs(a - b) for a, b in anomaly_pairs)
    derived_stability = fluctuation_index / (len(anomaly_pairs) + 1)
    
    # Final adjustment based on actual logic
    if len(error_flags) == 0 and temp_accumulator > 0:
        efficiency_score = efficiency_score // (temp_accumulator // 10 + 1)
    
    final_output = efficiency_score
    return final_output

# Input data
log_data = [
    {'ts': 100, 'load': 80, 'status': 'init', 'response_time': 15, 'throughput': 40, 'retry_count': 2, 'memory': 50},
    {'ts': 105, 'load': 120, 'status': 'success', 'response_time': 20, 'throughput': 60, 'retry_count': 3, 'memory': 60},
    {'ts': 110, 'load': 130, 'status': 'success', 'response_time': 25, 'throughput': 80, 'retry_count': 1, 'memory': 70},
    {'ts': 115, 'load': 90, 'status': 'success', 'response_time': 18, 'throughput': 70, 'retry_count': 2, 'memory': 65},
    {'ts': 120, 'load': 200, 'status': 'timeout', 'response_time': 0, 'throughput': 0, 'retry_count': 0, 'memory': 100},
    {'ts': 125, 'load': 110, 'status': 'success', 'response_time': 22, 'throughput': 50, 'retry_count': 0, 'memory': 58}
]

thresholds = {
    'latency_threshold': 21,
    'max_retries': 2
}

efficiency_score = 0
final_output = process_metrics(log_data, thresholds)
print(f"Result: {final_output}")