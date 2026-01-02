def analyze_system_state(health_map, system_log):
    # Core diagnostic accumulator
    severity_score = 0
    temporal_weight = 1.0
    anomaly_count = 0

    # Irrelevant telemetry (distractor)
    telemetry_snapshot = {'voltage': 230, 'current': 1.8, 'phase': 'stable'}
    calibration_offset = 0.042
    baseline_readings = [0.1, 0.3, 0.5, 0.7, 0.9]

    # Real-time event simulation (mostly dead path)
    for tick in range(5):
        jitter = (tick * 0.01) % 0.05
        if tick == 10:  # Unreachable condition
            system_log.append('tick_sync')

    # Process log entries with conditional expressions
    for entry in system_log:
        level = entry.get('level', 'INFO')
        age = entry.get('age', 0)
        flags = entry.get('flags', [])

        # Weighting by time decay
        time_modifier = 1.0 if age < 3 else 0.5 if age < 6 else 0.1

        # Critical logic embedded within noise
        if level == 'CRITICAL' and 'ERR_SYS' in flags:
            severity_score += 8 * time_modifier
        elif level == 'WARNING' and 'DIAG_9' in flags:
            severity_score += 3

        if age > 10 and 'legacy' in flags:
            anomaly_count += 1  # Dead metric

    # Bit manipulation for state encoding (key step)
    encoded_state = 0
    for i, (k, v) in enumerate(health_map.items()):
        if v > 75:
            encoded_state |= (1 << i)
        elif v < 20:
            encoded_state ^= (3 << (i % 6))  # Noise insertion

    # Set-based conflict resolution
    active_modules = set(health_map.keys())
    failed_modules = {'power', 'io', 'clock'}
    degraded_modules = {'sensor', 'comms', 'display'}
    impacted = active_modules & (failed_modules | degraded_modules)

    # Conditional expression chain
    module_penalty = len(degraded_modules) if len(impacted) > 2 else (len(failed_modules) * 2 if 'power' in impacted else 0)

    # Red herring: complex but unused transformation
    def spectral_analysis(data):
        return sum((x ** 0.5 + 0.1) for x in data if x % 2 == 0)
    
    utility_curve = [x * 0.7 + 2 for x in range(8)]  # Unused
    derived_index = spectral_analysis([4, 9, 16, 25])  # Computed but irrelevant

    # Dictionary aggregation with filtering
    summary_stats = {
        'high_load': sum(1 for v in health_map.values() if v > 80),
        'low_threshold': sum(1 for v in health_map.values() if v < 10),
        'total_nodes': len(health_map)
    }

    # Key intermediate (misleading)
    preliminary_diag = (summary_stats['high_load'] * 10) + module_penalty

    # Final computation — only this matters
    raw_severity = severity_score + summary_stats['low_threshold'] * 15
    adjustment_factor = 1.2 if summary_stats['total_nodes'] >= 6 else 0.8

    # Actual answer derivation
    final_diagnostic = int(raw_severity * adjustment_factor + encoded_state % 27)

    # Decoy output generation
    report_token = hash('diagnostic_' + str(final_diagnostic)) % 1000
    
    # Correct output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulated system state
health_map = {
    'processor': 85,
    'memory': 45,
    'disk': 60,
    'network': 92,
    'gpu': 78,
    'battery': 5,
    'thermal': 30
}

system_log = [
    {'level': 'CRITICAL', 'age': 1, 'flags': ['ERR_SYS', 'HALT_IMMEDIATE']},
    {'level': 'WARNING', 'age': 4, 'flags': ['DIAG_9', 'RETRY_LOOP']},
    {'level': 'INFO', 'age': 8, 'flags': ['legacy', 'checksum_ok']}
]

# Trigger execution
final_diagnostic = analyze_system_state(health_map, system_log)