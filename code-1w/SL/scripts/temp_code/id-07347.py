def process_logs(raw_data):
    # Irrelevant preprocessing: timestamp normalization (distractor)
    normalized_times = [entry['ts'] - 1600000000 for entry in raw_data if 'ts' in entry]
    avg_time_offset = sum(normalized_times) / len(normalized_times) if normalized_times else 0

    # Red herring: security flag computation (unused later)
    security_flags = []
    for entry in raw_data:
        if 'error' in entry.get('type', '').lower():
            flag = (hash(entry['msg']) % 13 == 0)
            security_flags.append(flag)

    # Distractor: nested helper with dead logic
    def decode_signal(x):
        return (x ^ 255) & 127  # Never actually used

    # Core data extraction (relevant)
    log_entries = []
    for item in raw_data:
        code = item.get('code', 0)
        severity = len(item.get('msg', '')) % 5
        active = item.get('active', False)
        if active:
            log_entries.append({'code': code, 'severity': severity})

    # Misleading aggregation (looks important but irrelevant)
    total_severity = sum(le['severity'] for le in log_entries)
    max_code = max((le['code'] for le in log_entries), default=0)
    entropy_proxy = total_severity ^ max_code

    # Real analysis function (uses lambda as required)
    analyze_pattern = lambda logs: (
        sum(
            (log['code'] * 3 + log['severity'] ** 2) 
            for log in logs 
            if log['code'] > 10
        ) - 150
    )

    # Key statement
    final_diagnostic = analyze_pattern(log_entries)

    # Dead code path (decoy)
    if entropy_proxy < 0:
        final_diagnostic *= -1
    elif entropy_proxy > 1000:
        final_diagnostic = abs(final_diagnostic)

    # Output result
    print(f"Target result: {final_diagnostic}")
    return final_diagnostic

# Simulated input data
input_logs = [
    {'ts': 1600000123, 'type': 'INFO', 'msg': 'System boot', 'code': 5, 'active': True},
    {'ts': 1600000124, 'type': 'WARN', 'msg': 'Disk low', 'code': 12, 'active': True},
    {'ts': 1600000125, 'type': 'ERROR', 'msg': 'Connection failed', 'code': 18, 'active': True},
    {'ts': 1600000126, 'type': 'DEBUG', 'msg': 'Retrying...', 'code': 15, 'active': True},
    {'ts': 1600000127, 'type': 'INFO', 'msg': 'Cleanup', 'code': 8, 'active': False},  # inactive
    {'ts': 1600000128, 'type': 'ALERT', 'msg': 'High latency', 'code': 22, 'active': True},
    {'ts': 1600000129, 'type': 'INFO', 'msg': 'Normal ops', 'code': 7, 'active': True}
]

# Execute
process_logs(input_logs)