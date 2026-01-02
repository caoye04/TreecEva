def analyze_system_health():
    # Real-time telemetry data from distributed nodes
    node_signals = [0.88, 0.92, 0.76, 0.94, 0.81]
    signal_weights = [3, 5, 2, 6, 4]

    # Weighted average calculation (relevant)
    weighted_sum = sum(s * w for s, w in zip(node_signals, signal_weights))
    total_weight = sum(signal_weights)
    avg_signal = weighted_sum / total_weight if total_weight else 0

    # Irrelevant: Historical debug counters (dead code path)
    debug_counters = {f'debug_{i}': i * 23 for i in range(15)}
    temp_snapshot = [val % 7 for val in debug_counters.values() if val % 3 == 0]

    # System state flags (mixed relevant/irrelevant)
    system_state = {
        'active_nodes': 5,
        'overload_threshold': 0.85,
        'degraded_mode': False,
        'last_reset_cycle': 12,
        'maintenance_window': False
    }

    # Log entries with diagnostic codes (relevant input)
    log_entries = [
        {'code': 200, 'severity': 1, 'duration': 120},
        {'code': 404, 'severity': 3, 'duration': 10},
        {'code': 503, 'severity': 5, 'duration': 45},
        {'code': 200, 'severity': 1, 'duration': 200},
        {'code': 503, 'severity': 5, 'duration': 30}
    ]

    # Decoy function: looks important but unused
    def compute_entropy(data):
        from math import log
        freq = {}
        for d in data:
            freq[d] = freq.get(d, 0) + 1
        entropy = 0
        for count in freq.values():
            p = count / len(data)
            entropy -= p * log(p)
        return entropy

    # Unused transformation chain (distractor)
    transformed_logs = []
    for entry in log_entries:
        transformed = {
            'hash': (entry['code'] * 7 + entry['severity']) % 1000,
            'flagged': entry['duration'] > 25 and entry['severity'] > 2,
            'legacy_id': f"LX-{entry['code']}-{entry['duration'] % 10}"
        }
        transformed_logs.append(transformed)

    # Conditional processing branches (some irrelevant)
    emergency_override = False
    if system_state['active_nodes'] < 3:
        emergency_override = True
    elif avg_signal > 0.8:
        emergency_override = False  # Red herring override reset

    # Diagnostic accumulator (critical intermediate)
    diagnostics = []
    for i, entry in enumerate(log_entries):
        if entry['code'] == 503 and entry['duration'] > 20:
            penalty = entry['severity'] * entry['duration'] * 0.1
            diagnostics.append((i, penalty))

    # Secondary filter (relevant)
    filtered_diagnostics = [p for idx, p in diagnostics if p > 3.0]

    # Auxiliary noise: fake correlation matrix
    correlation_matrix = [[0]*len(log_entries) for _ in range(len(log_entries))]
    for i in range(len(log_entries)):
        for j in range(len(log_entries)):
            correlation_matrix[i][j] = (log_entries[i]['code'] ^ log_entries[j]['code']) & 7

    # Core logic: process metrics to determine final diagnostic score
    def process_metrics(logs, state):
        base_score = 100.0
        overload = state['overload_threshold']

        # Accumulate severity impact
        for log in logs:
            if log['severity'] >= 5:
                impact = (log['duration'] / 60.0) * 15
                base_score -= impact

        # Adjust for signal quality
        nonlocal avg_signal
        if avg_signal < overload:
            base_score -= 12.5

        # Bonus for recovery patterns
        recovery_count = sum(1 for i in range(1, len(logs)) 
                           if logs[i]['code'] == 200 and logs[i-1]['code'] != 200)
        base_score += recovery_count * 8.0

        # Final clamp and transform
        base_score = max(10.0, min(100.0, base_score))
        return round(base_score * 2.5, 4)  # Scale to specialized metric

    # Execution point of interest
    final_diagnostic = process_metrics(log_entries, system_state)

    # Dead code: post-processing that doesn't affect result
    if final_diagnostic > 200:
        final_diagnostic *= 0.9
    elif final_diagnostic < 50:
        adjustment_map = {i: i*1.1 for i in range(10)}
        for k in adjustment_map:
            adjustment_map[k] *= 0.95

    # Print required output
    print(f"Result: {final_diagnostic}")

    # Return nothing; value captured via print and assignment
    return

# Execute the function
analyze_system_health()