from collections import defaultdict, Counter

# Simulated system telemetry data
technical_logs = [
    {'timestamp': 1001, 'event': 'read', 'sector': 5, 'duration_ms': 12},
    {'timestamp': 1003, 'event': 'write', 'sector': 7, 'duration_ms': 18},
    {'timestamp': 1006, 'event': 'read', 'sector': 5, 'duration_ms': 11},
    {'timestamp': 1009, 'event': 'write', 'sector': 6, 'duration_ms': 22},
    {'timestamp': 1012, 'event': 'read', 'sector': 8, 'duration_ms': 13}
]

# Irrelevant telemetry (distractor)
irrelevant_sensors = [1.2, 0.9, 1.5, 2.1, 1.8]
avg_sensor = sum(irrelevant_sensors) / len(irrelevant_sensors)
sensor_alert = avg_sensor > 1.0  # Red herring

# System flags with mixed relevance
system_flags = {
    'overclock': True,
    'safe_mode': False,
    'cache_enabled': True,
    'debug_trace': True  # Unused in logic
}

# Misleading pre-processing (dead path)
def analyze_pattern(logs):
    pattern_count = defaultdict(int)
    for log in logs:
        key = (log['event'], log['sector'] % 2)
        pattern_count[key] += 1
    return dict(pattern_count)  # Computed but not used

# Distractor function: looks important but unused
def compute_health_score(entries):
    durations = [e['duration_ms'] for e in entries]
    return 100 - (sum(durations) / len(durations))

# Core logic disguised among noise
def extract_read_trends(logs):
    read_times = []
    sector_load = defaultdict(int)
    
    for i, entry in enumerate(logs):
        if entry['event'] == 'read':
            read_times.append(entry['duration_ms'])
            sector_load[entry['sector']] += 1
            
            # Nested logic red herring
            if i > 0 and logs[i-1]['event'] == 'write':
                read_times[-1] += 2  # Artificial inflation (distraction)
    
    avg_read = sum(read_times) / len(read_times) if read_times else 0
    max_replicated = max(sector_load.values()) if sector_load else 0
    
    # Real signal: ratio of average read time to most accessed sector
    return avg_read, max_replicated

# Another decoy transformation
zipped_data = list(zip([x['timestamp'] for x in technical_logs], [x['duration_ms'] for x in technical_logs]))
timestamp_shifts = [zipped_data[i+1][0] - zipped_data[i][0] for i in range(len(zipped_data)-1)]
median_shift = sorted(timestamp_shifts)[len(timestamp_shifts)//2]  # Not used

# Actual relevant preprocessing
def filter_critical_events(logs):
    critical = []
    for log in logs:
        if log['duration_ms'] > 15:
            critical.append(log)
    return critical

# Main processing with multiple concepts
def process_metrics(log_entries, flags):
    # Step 1: Extract high-latency operations
    long_ops = filter_critical_events(log_entries)
    
    # Step 2: Get read access patterns
    avg_read_time, peak_sector = extract_read_trends(log_entries)
    
    # Step 3: Compute operation entropy (bit manipulation red herring)
    event_types = [1 if e['event'] == 'write' else 0 for e in log_entries]
    xor_fingerprint = 0
    for val in event_types:
        xor_fingerprint ^= (val << 2)  # Looks cryptographic, isn't used
    
    # Step 4: Weighted diagnostic score (actual answer source)
    latency_penalty = len(long_ops) * 15
    sector_bias = peak_sector * 7
    base_efficiency = int(avg_read_time * 3)
    
    # Step 5: Conditional multiplier (depends on real flag)
    mode_factor = 2 if flags['overclock'] and not flags['safe_mode'] else 1
    
    # Step 6: Irrelevant bit shifting distraction
    temp_flag = (latency_penalty << 1) & 0xFF
    temp_flag = temp_flag ^ 0xAA  # More misdirection
    
    # Step 7: Real computation (answer path)
    raw_diagnostic = base_efficiency + sector_bias - latency_penalty
    final_diagnostic = raw_diagnostic * mode_factor
    
    # Step 8: Print for traceability (required output)
    print(f"Result: {final_diagnostic}")
    
    return final_diagnostic

# Execution flow with hidden critical point
log_entries = technical_logs  # Alias to obscure relevance

# Dead code path invocation (increases interference)
dummy_analysis = analyze_pattern(technical_logs)
health_score = compute_health_score(technical_logs)  # Unused result

# Critical execution point — answer determined here
final_diagnostic = process_metrics(log_entries, system_flags)
