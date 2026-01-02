from collections import defaultdict, Counter
import math

# Simulated system log analyzer with diagnostic computation

def preprocess_logs(raw):
    processed = []
    for entry in raw:
        if 'ERROR' in entry['type']:
            processed.append({'id': entry['id'], 'severity': len(entry['msg']), 'timestamp': entry['ts']})
    return processed

def generate_checksum(data):
    # Irrelevant checksum function (dead code path)
    chk = 0
    for i, d in enumerate(data):
        chk ^= (d['severity'] + i) * 37
    return chk % 1000

def filter_noisy_data(entries):
    # Real but indirect preprocessing step
    filtered = []
    for e in entries:
        if e['severity'] > 3:
            filtered.append(e)
    return filtered

def count_temporal_gaps(timestamps):
    # Distractor: computes time gaps but not used in final result
    gaps = []
    for i in range(1, len(timestamps)):
        gaps.append(timestamps[i] - timestamps[i-1])
    avg_gap = sum(gaps) / len(gaps) if gaps else 0
    return round(avg_gap, 3)

def compute_entropy(values):
    # Red herring: looks important but unused
    counts = defaultdict(int)
    for v in values:
        counts[v] += 1
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def extract_signatures(logs):
    # Extracts signature patterns — partially relevant
    sigs = []
    for log in logs:
        sig = (log['id'] % 10, log['severity'] % 5)
        sigs.append(sig)
    return sigs

def evaluate_signature_complexity(signatures):
    # Counts unique signatures — this contributes to final answer
    return len(set(signatures))

def track_flag_sequence(flags):
    # Unused analysis of flag transitions
    transitions = 0
    for i in range(1, len(flags)):
        if flags[i] != flags[i-1]:
            transitions += 1
    return transitions

def correlate_flag_with_severity(logs, flags):
    # Real correlation logic, but only one component is used
    severity_sum = 0
    for i, log in enumerate(logs):
        if i < len(flags) and flags[i]:
            severity_sum += log['severity']
    return severity_sum

def analyze_pattern(log_entries, system_flags):
    # Main analysis pipeline
    cleaned = preprocess_logs(log_entries)
    relevant = filter_noisy_data(cleaned)
    
    # Extract features
    signatures = extract_signatures(relevant)
    complexity_score = evaluate_signature_complexity(signatures)
    
    # Key intermediate values
    base_severity = correlate_flag_with_severity(relevant, system_flags)
    temporal_marks = [e['timestamp'] for e in relevant]
    
    # Distractor computations (not affecting final result)
    _ = count_temporal_gaps(temporal_marks)
    _ = compute_entropy(temporal_marks)
    _ = track_flag_sequence(system_flags)
    
    # Final diagnostic formula (only this matters)
    adjustment_factor = 1 if len(relevant) > 5 else 0.8
    raw_diagnostic = base_severity * complexity_score
    final_diagnostic = int(raw_diagnostic * adjustment_factor)
    
    return final_diagnostic

# Simulated input data
log_data = [
    {'id': 101, 'type': 'INFO', 'msg': 'System boot', 'ts': 1000},
    {'id': 102, 'type': 'ERROR', 'msg': 'Disk fail', 'ts': 1005},
    {'id': 103, 'type': 'ERROR', 'msg': 'Net timeout long message', 'ts': 1010},
    {'id': 104, 'type': 'ERROR', 'msg': 'Sensor', 'ts': 1015},
    {'id': 105, 'type': 'ERROR', 'msg': 'Critical failure detected early', 'ts': 1020},
    {'id': 106, 'type': 'ERROR', 'msg': 'Buffer overflow', 'ts': 1025},
    {'id': 107, 'type': 'ERROR', 'msg': 'Authentication retry', 'ts': 1030},
    {'id': 108, 'type': 'WARNING', 'msg': 'High memory', 'ts': 1035}
]

system_monitor_flags = [True, False, True, True, False, True, True, False]

# Execute main analysis
clean_logs = preprocess_logs(log_data)
filtered_logs = filter_noisy_data(clean_logs)
signatures = extract_signatures(filtered_logs)
_ = generate_checksum(filtered_logs)  # Dead call
_ = compute_entropy([s[0] for s in signatures])  # More distraction

final_diagnostic = analyze_pattern(log_entries=log_data, system_flags=system_monitor_flags)
print(f"Target result: {final_diagnostic}")