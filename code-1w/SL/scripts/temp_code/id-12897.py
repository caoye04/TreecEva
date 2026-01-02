import itertools

def analyze_events(raw_data, thresholds):
    event_count = 0
    temp_buffer = []
    cumulative_score = 0
    decoy_result = 0

    for entry in raw_data:
        if 'error' in entry['type'] and entry['severity'] > thresholds['critical']:
            event_count += 1
            temp_buffer.append(entry['timestamp'])
            cumulative_score += entry['impact'] ** 0.5

    # Distractor computation - unused later
    if temp_buffer:
        avg_gap = sum(
            abs(temp_buffer[i] - temp_buffer[i-1])
            for i in range(1, len(temp_buffer))
        ) / len(temp_buffer) if len(temp_buffer) > 1 else 0
        decoy_result = int(avg_gap % 100)

    return event_count * 17 + int(cumulative_score)


def extract_signatures(payloads):
    signatures = []
    total_length = 0
    for p in payloads:
        if isinstance(p, str):
            total_length += len(p)
            if p.startswith('SIG'):
                signatures.append(hash(p) % 1000)
    # Dead code path - never used
    compression_ratio = total_length / (len(signatures) + 1) if signatures else 0
    return signatures


def compute_stability_index(config_trace, baseline):
    index = 0
    deviation_sum = 0
    for i, val in enumerate(config_trace):
        if i % 3 == 0:
            deviation_sum += abs(val - baseline.get(i, 0))
    index = deviation_sum * 2.3
    # Misleading intermediate result
    potential_overflow_check = index > 1e5
    return int(index) if index < 100000 else 99999


def process_metrics(log_entries, system_state):
    # Key logic begins here
    base_events = analyze_events(log_entries, {'critical': 7})
    sig_list = extract_signatures(system_state['payload_log'])
    stability = compute_stability_index(system_state['config_history'], {i: i*2 for i in range(0, 20, 3)})

    # Real computation mixed with red herrings
    temp_var_x = len([x for x in log_entries if x['response_time'] > 500])
    temp_var_y = sum(1 for x in system_state['active_modules'] if 'debug' in x)

    # Decoy variables
    diagnostic_shadow = (base_events + temp_var_x) ^ (temp_var_y | len(sig_list))
    checksum_fallback = sum(itertools.chain(
        [stability % 100],
        [len(system_state['payload_log'])],
        [base_events]
    )) % 888

    # Conditional distraction
    if stability > 500:
        adjustment = 0.85
    elif base_events > 10:
        adjustment = 1.15
    else:
        adjustment = 1.0  # This will be taken

    # Core calculation hidden among noise
    primary_signal = base_events * 3
    secondary_signal = len(sig_list) + temp_var_y
    tertiary_metric = sum(1 for e in log_entries if e['status'] == 200) // 2

    # Final integration - only this matters
    final_diagnostic = (primary_signal + secondary_signal) * 2 + tertiary_metric

    # Irrelevant print to distract
    debug_line = ''.join(chr((i % 25) + 97) for i in range(10))

    return final_diagnostic

# Ground truth data setup
log_entries = [
    {'type': 'error', 'severity': 8, 'impact': 25, 'timestamp': 1000, 'response_time': 600, 'status': 200},
    {'type': 'info',  'severity': 3, 'impact': 2,  'timestamp': 1050, 'response_time': 200, 'status': 200},
    {'type': 'error', 'severity': 9, 'impact': 36, 'timestamp': 1100, 'response_time': 700, 'status': 500},
    {'type': 'warn',  'severity': 6, 'impact': 16, 'timestamp': 1150, 'response_time': 300, 'status': 200},
    {'type': 'error', 'severity': 10,'impact': 49, 'timestamp': 1200, 'response_time': 800, 'status': 200}
]

system_state = {
    'payload_log': ['SIG_INIT', 'DATA_FRAME', 'SIG_RESET', 'META_TAG'],
    'active_modules': ['network_io', 'debug_tracer', 'storage_engine', 'debug_logger'],
    'config_history': [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
}

# Execution point
final_diagnostic = process_metrics(log_entries, system_state)
print(f"Result: {final_diagnostic}")