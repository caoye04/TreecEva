def analyze_system_logs(raw_entries):
    # Irrelevant preprocessing: normalize timestamps (unused)
    normalized_times = [entry['timestamp'].replace('Z', '+00:00') for entry in raw_entries if 'timestamp' in entry]
    temp_offsets = [t[-6:-3] for t in normalized_times if t.endswith('+00:00')]
    offset_count = len(set(temp_offsets))  # Distractor: never used

    # Core data extraction
    error_codes = []
    warning_flags = []    
    heartbeat_intervals = []

    for entry in raw_entries:
        if entry.get('level') == 'ERROR':
            error_codes.append(entry['code'])
        elif entry.get('level') == 'WARNING':
            warning_flags.append(entry['flag'])
        
        if 'metrics' in entry:
            heartbeat_intervals.extend(entry['metrics'].get('heartbeats', []))

    # Distractor: complex but unused statistical transformation
    transformed_heartbeats = [round((x - min(heartbeat_intervals)) / (max(heartbeat_intervals) - min(heartbeat_intervals) + 1e-9) * 100) for x in heartbeat_intervals]
    histogram_bins = {}
    for val in transformed_heartbeats:
        bin_key = val // 10
        histogram_bins[bin_key] = histogram_bins.get(bin_key, 0) + 1
    
    # Another red herring: simulate predictive anomaly (not actually used)
    prediction_window = []
    for i in range(1, len(transformed_heartbeats)):
        if transformed_heartbeats[i] > transformed_heartbeats[i-1]:
            prediction_window.append(1)
        else:
            prediction_window.append(0)
    predicted_anomalies = sum(prediction_window)  # Dead end

    # Actual relevant logic begins here
    unique_errors = set(error_codes)
    critical_errors = {code for code in unique_errors if code % 7 == 0}  # Only multiples of 7 are critical
    
    # Simulated diagnostic thresholds
    base_score = 50
    penalty_per_critical = 8
    aggregate_score = base_score - (len(critical_errors) * penalty_per_critical)

    # String-based log analysis (required python feature: string methods)
    abnormal_logs = []
    for entry in raw_entries:
        msg = entry.get('message', '')
        if isinstance(msg, str):
            # Check for abnormal patterns using string methods
            if msg.strip().lower().startswith('corrupted') or 'timeout' in msg.lower() or msg.count('!') > 2:
                abnormal_logs.append(msg.strip())
    
    # Key statement with target variable
    final_diagnostic = aggregate_score + len(abnormal_logs)

    # Additional distractor: sort unrelated list
    sorted_warnings = sorted(warning_flags, reverse=True)
    cumulative_flag = 0
    for w in sorted_warnings:
        cumulative_flag = (cumulative_flag + w) % 100
    final_diagnostic += cumulative_flag  # Misleading: appears important but overwrites later

    # Reset final_diagnostic to break dependency on distractor
    final_diagnostic = aggregate_score + len(abnormal_logs)  # Actual final assignment

    # Print required output
    print(f"Result: {final_diagnostic}")

    return final_diagnostic

# Input data
logs = [
    {'level': 'ERROR', 'code': 14, 'message': 'Corrupted data stream!'},
    {'level': 'WARNING', 'flag': 5, 'message': 'High latency detected'},
    {'level': 'ERROR', 'code': 21, 'message': 'Timeout on node !!!!'},
    {'level': 'INFO', 'message': 'System heartbeat', 'metrics': {'heartbeats': [120, 140]}},
    {'level': 'ERROR', 'code': 13, 'message': 'Invalid request'},
    {'level': 'WARNING', 'flag': 3, 'message': 'corrupted frame received!'},
    {'level': 'ERROR', 'code': 28, 'message': 'Critical failure! Immediate restart!'}
]

# Execute
result = analyze_system_logs(logs)