from collections import defaultdict, Counter

# Simulated system telemetry data with mixed signal types
def collect_signals():
    signals = []
    for i in range(150):
        phase = i % 4
        if phase == 0:
            signals.append(('voltage', (i * 0.7) % 5 + (i % 3)))
        elif phase == 1:
            signals.append(('current', (i * 0.3) % 4))
        elif phase == 2:
            signals.append(('temp', (i * 0.1) % 60 + 20))
        else:
            signals.append(('noise', (i * 1.1) % 10))
    return signals

# Parse raw signals into structured log entries
def parse_logs(raw_signals):
    logs = defaultdict(list)
    for typ, val in raw_signals:
        logs[typ].append(round(val, 2))
    return logs

# Legacy function - unused but looks relevant
def analyze_stability(logs):
    stability_score = 0
    for key in logs:
        if len(logs[key]) > 1:
            variance = sum((a - b) ** 2 for a, b in zip(logs[key], logs[key][1:]))
            stability_score += variance / len(logs[key])
    return stability_score

# Secondary processing: extract diagnostic windows
def extract_windows(data, window_size=10):
    windows = []
    flat_data = sorted([item for sublist in data.values() for item in sublist])
    for i in range(0, len(flat_data) - window_size + 1, window_size // 2):
        windows.append(flat_data[i:i + window_size])
    return windows

# Checksum validation (bit manipulation red herring)
def validate_checksum(sequence):
    checksum = 0
    for val in sequence:
        truncated = int(val) & 0xFF
        checksum ^= truncated
        checksum = (checksum << 1) | (checksum >> 7)
        checksum &= 0xFF
    return checksum == 0x5A

# Core metric processor - only some paths are actually used
def compute_health_index(windows):
    index_values = []
    for win in windows:
        avg = sum(win) / len(win)
        mid = win[len(win)//2]
        # Only this condition contributes to final result
        if avg > 25.0 and validate_checksum(win):  # Rarely true
            index_values.append(avg * 1.5)
        elif len([x for x in win if x > 30]) > 3:
            index_values.append(avg * 0.8)
        else:
            index_values.append(avg)
    return sum(index_values) / len(index_values) if index_values else 0

# System state tracker with irrelevant flags
def get_system_state():
    state = {
        'power_mode': 'high',
        'cache_level': 3,
        'overclock': False,
        'debug_trace': True,
        'audit_log': [],
        'version': '2.1.8'
    }
    # Unused derived values that look important
    state['mode_flag'] = (len(state['version']) << 2) ^ 17
    state['diagnostic_key'] = sum(ord(c) for c in state['version']) % 100
    return state

# Main processing pipeline
def process_metrics(log_entries, sys_state):
    # Extract voltage and temp only - others ignored
    relevant_types = ['voltage', 'temp']
    filtered_data = {k: v for k, v in log_entries.items() if k in relevant_types}

    # Compute aggregate statistics (some used, some not)
    stats = defaultdict(float)
    all_vals = [val for sublist in filtered_data.values() for val in sublist]
    stats['global_mean'] = sum(all_vals) / len(all_vals)
    stats['peak'] = max(all_vals)
    stats['range'] = stats['peak'] - min(all_vals)
    
    # Generate windows for analysis
    windows = extract_windows(filtered_data, window_size=8)
    
    # Compute health index (only this matters)
    health_index = compute_health_index(windows)
    
    # Distractor computation chain - looks important but unused
    anomaly_count = 0
    for typ, vals in log_entries.items():
        count_above = sum(1 for v in vals if v > (40 if typ == 'temp' else 10))
        if count_above > 5:
            anomaly_count += 1
    baseline_reference = (stats['global_mean'] * 0.95) + (anomaly_count * 2.1)
    
    # Final diagnostic calculation - depends only on health_index and system mode
    adjustment = 1.1 if sys_state['power_mode'] == 'high' else 0.9
    intermediate = health_index * adjustment
    
    # Additional decoy logic
    if sys_state['debug_trace']:
        snapshot = all_vals[::15]  # never used
        compression_ratio = len(snapshot) / len(all_vals) if all_vals else 0
    
    # Critical assignment - this is the answer
    final_diagnostic = round(intermediate + 17.3, 4)
    
    # Dead code path - unreachable but plausible
    if False:
        fallback = sum(stats.values()) / 1000
        final_diagnostic = fallback
    
    return final_diagnostic

# Execution flow
if __name__ == '__main__':
    raw = collect_signals()
    parsed_logs = parse_logs(raw)
    system_state = get_system_state()
    final_diagnostic = process_metrics(parsed_logs, system_state)
    print(f"Result: {final_diagnostic}")