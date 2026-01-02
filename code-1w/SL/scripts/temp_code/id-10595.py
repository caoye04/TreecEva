def analyze_system_health(raw_logs, config):
    # Irrelevant preprocessing (distractor)
    cleaned = [line.strip().lower() for line in raw_logs if 'debug' not in line]
    temp_buffer = []
    for i, line in enumerate(cleaned):
        if i % 3 == 0:
            temp_buffer.append(line[:10])

    # Real data extraction (relevant)
    log_entries = []
    for line in raw_logs:
        parts = line.split('|')
        if len(parts) > 2 and parts[1].isdigit():
            timestamp = int(parts[1])
            level = parts[2].strip()
            log_entries.append({'time': timestamp, 'level': level})

    # Misleading statistical aggregation (distractor)
    avg_time = sum(e['time'] for e in log_entries) / len(log_entries) if log_entries else 0
    time_variance = sum((e['time'] - avg_time) ** 2 for e in log_entries) / len(log_entries) if log_entries else 0

    # System state initialization (relevant)
    system_state = {
        'status_flag': 0b1010,
        'active_nodes': [1, 0, 1, 1],
        'threshold': config.get('critical_level', 75),
        'fail_count': 0
    }

    # Dead code path - never executed (red herring)
    def legacy_repair():
        nonlocal system_state
        system_state['status_flag'] ^= 0b1111

    # Auxiliary function with decoy logic
    def validate_node(index, node_id):
        return (index ^ node_id) & 0b110 != 0  # Unused result

    # Real processing function
    def evaluate_health(events, state):
        critical_events = 0
        recent_times = []

        # Nested filtering and transformation
        for idx, event in enumerate(events):
            if event['level'] == 'CRITICAL':
                critical_events += 1
                recent_times.append(event['time'])

            # Distractor: irrelevant string analysis
            if 'error' in event['level'].lower():
                chars = [c for c in event['level'] if c.isalpha()]
                shuffled = ''.join([chars[-i] for i in range(1, len(chars)+1, 2)])

        # Bit manipulation for status synthesis (relevant)
        base_flag = state['status_flag']
        fail_score = critical_events * 17
        dynamic_mask = len(recent_times) << 2
        combined = (base_flag ^ fail_score) & dynamic_mask

        # Conditional override based on logical chain
        if critical_events > 2 and len(recent_times) >= 2:
            interval_diff = recent_times[-1] - recent_times[0]
            if interval_diff < state['threshold']:
                combined |= 0b100000

        # More decoy computations
        dummy_map = {i: (i**2 + 3*i + 1) % 100 for i in range(15)}
        checksum = sum(dummy_map[k] for k in dummy_map if k % 4 == 0)

        return combined + (state['active_nodes'].count(1) * 3)

    # Another unused helper (dead code)
    def generate_report(data):
        return '|'.join(f'{k}:{v}' for k, v in data.items())

    # Key variable construction (relevant)
    health_code = evaluate_health(log_entries, system_state)

    # Complex string-based state encoding (partially relevant)
    state_summary = []
    for i, (node_val, flag_bit) in enumerate(zip(system_state['active_nodes'], bin(system_state['status_flag'])[2:][::-1])):
        bit_val = int(flag_bit) if i < len(bin(system_state['status_flag'])[2:]) else 0
        encoded = (node_val << 1) | bit_val
        state_summary.append(encoded)

    # Final metric computation (relevant)
    raw_metric = health_code * 2 + sum(state_summary)

    # Decoy normalization (looks important but unused)
    normalized = round(raw_metric / (1 + time_variance), 4) if time_variance else raw_metric

    # Final diagnostic calculation (target)
    final_diagnostic = raw_metric - (system_state['fail_count'] << 3)

    # Print required output
    print(f"Result: {final_diagnostic}")

    return final_diagnostic

# Simulated input data
simulated_logs = [
    "LOG|100|INFO",
    "ERR|105|CRITICAL",
    "DBG|110|WARNING",
    "LOG|115|CRITICAL",
    "LOG|120|CRITICAL"
]
system_config = {"critical_level": 25}

# Execute main function
analyze_system_health(simulated_logs, system_config)