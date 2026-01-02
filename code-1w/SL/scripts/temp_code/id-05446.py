import itertools

# Simulated system telemetry and health monitoring with distractors
def collect_telemetry():
    raw_signals = [0.88, 0.72, 0.91, 0.67, 0.75]
    weights = [0.2, 0.3, 0.1, 0.25, 0.15]
    weighted_avg = sum(s * w for s, w in zip(raw_signals, weights))

    # Irrelevant signal smoothing (dead path)
    smoothed = []
    for i in range(len(raw_signals)):
        if i == 0:
            smoothed.append(raw_signals[i])
        else:
            smoothed.append(0.7 * raw_signals[i] + 0.3 * smoothed[i-1])

    # Unused transformation
    transformed = list(map(lambda x: x ** 2 + 0.1, raw_signals))

    # Actual returned value (only weighted_avg matters)
    return {'average': weighted_avg, 'count': len(raw_signals)}


def encrypt_key(base: int) -> int:
    # Bit manipulation red herring
    key = base ^ 255
    key = (key << 2) & 0xFF
    key = key | (base >> 1)
    return key  # Never used in critical path

# Misleading diagnostic chain
def analyze_events(events):
    event_code_sum = 0
    for e in events:
        if 'ERROR' in e:
            event_code_sum += 3
        elif 'WARN' in e:
            event_code_sum += 1
    
    # Complex but irrelevant scoring model
    adjustment = 0
    for i, e in enumerate(events):
        adjustment += (i + 1) * (hash(e) % 5)
    
    final_score = event_code_sum * 10 - adjustment  # Dead end
    return final_score

# Real processing function
def aggregate_logs(entries):
    severity_map = {'INFO': 1, 'WARN': 2, 'ERROR': 3, 'CRITICAL': 4}
    total_severity = 0
    error_count = 0
    timestamps = []  # Collected but unused

    for entry in entries:
        level = entry['level']
        ts = entry['timestamp']
        timestamps.append(ts)
        if level in severity_map:
            total_severity += severity_map[level]
        if level == 'ERROR' or level == 'CRITICAL':
            error_count += 1

    # Compute diagnostic ratio
    if len(entries) > 0:
        ratio = total_severity / len(entries)
    else:
        ratio = 0.0

    return ratio, error_count

# Core state processor (uses dictionary and itertools)
def build_context(state):
    context = {}
    
    # Real computation
    cpu_load = state.get('cpu', 0)
    mem_usage = state.get('memory', 0)
    disk_io = state.get('disk_io', [])

    # Distractor: complex iterator over unused I/O ops
    if disk_io:
        flattened = list(itertools.chain.from_iterable(
            [chunk['ops'] for chunk in disk_io if chunk['active']]
        ))
        avg_op_time = sum(flattened) / len(flattened) if flattened else 0
        context['avg_op_time'] = avg_op_time  # Stored but not used later

    # Real metric
    load_factor = (cpu_load * 0.6) + (mem_usage * 0.4)
    context['load_factor'] = load_factor

    # Fake correlation index
    fake_index = 0
    for k, v in state.items():
        fake_index ^= hash(str(v)) & 0xFFFF
    context['correlation_hash'] = fake_index  # Red herring

    return context

# Final integration function
def process_metrics(logs, sys_state):
    # Real logic begins here
    log_ratio, errors = aggregate_logs(logs)
    ctx = build_context(sys_state)
    base_score = log_ratio * 100

    # Additional real input
    load_factor = ctx['load_factor']
    system_risk = base_score + (load_factor * 10)

    # Distractor: cryptographic checksum (never affects result)
    secret_salt = 123
    raw_data = [len(logs), errors, int(load_factor * 100)]
    checksum = 0
    for val in raw_data:
        checksum = (checksum ^ encrypt_key(val + secret_salt)) & 0x7FFFFFFF

    # Another distraction: combinatorics on log types
    levels = [entry['level'] for entry in logs]
    unique_pairs = list(itertools.combinations(set(levels), 2))
    diversity_index = len(unique_pairs)  # Computed but unused

    # Critical decision path
    if errors > 5:
        multiplier = 1.5
    elif errors > 2:
        multiplier = 1.2
    else:
        multiplier = 1.0  # Correct path: only 2 errors

    # Final calculation
    intermediate = system_risk * multiplier
    
    # Apply decay function (real)
    decayed = intermediate * (0.9 ** errors)  # 0.9^2 = 0.81

    # Round to nearest integer
    final_diagnostic = int(round(decayed))

    return final_diagnostic

# --- EXECUTION ENTRY POINT ---
if __name__ == "__main__":
    # Simulated log entries
    log_entries = [
        {'timestamp': 1001, 'level': 'INFO', 'msg': 'System boot'},
        {'timestamp': 1005, 'level': 'INFO', 'msg': 'Service started'},
        {'timestamp': 1010, 'level': 'WARN', 'msg': 'High latency detected'},
        {'timestamp': 1015, 'level': 'ERROR', 'msg': 'Timeout on DB'},
        {'timestamp': 1020, 'level': 'INFO', 'msg': 'Retry successful'},
        {'timestamp': 1025, 'level': 'WARN', 'msg': 'Disk space low'},
        {'timestamp': 1030, 'level': 'ERROR', 'msg': 'Write failure'},
        {'timestamp': 1035, 'level': 'INFO', 'msg': 'Fallback activated'}
    ]

    # System state with relevant and irrelevant fields
    system_state = {
        'cpu': 75.0,
        'memory': 88.0,
        'uptime': 3600,
        'users': 42,
        'network': {'in': 1200, 'out': 950},
        'disk_io': [
            {'active': True, 'ops': [12, 15, 14]},
            {'active': False, 'ops': [20, 18]},
            {'active': True, 'ops': [10, 11, 13, 12]}
        ]
    }

    # Telemetry collection (irrelevant call)
    telem = collect_telemetry()  # Used nowhere

    # Event analysis (red herring)
    events_list = ['STATUS_OK', 'WARN_DISK', 'ERROR_DB_TIMEOUT', 'INFO_RETRY']
    dummy_analysis = analyze_events(events_list)  # Dead code

    # Key execution point
    final_diagnostic = process_metrics(log_entries, system_state)

    # Output result
    print(f"Target result: {final_diagnostic}")