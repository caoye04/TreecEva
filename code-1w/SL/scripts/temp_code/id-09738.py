def analyze_event_sequence(raw_logs):
    event_codes = [int(x.split('-')[1]) for x in raw_logs if x.startswith('E')]
    severity_map = {1: 'LOW', 2: 'MEDIUM', 3: 'HIGH'}
    filtered_severity = [code for code in event_codes if code % 3 == 1]
    normalized = [abs((c - 1) // 3) for c in filtered_severity]
    return sum(normalized)


def compute_health_score(timestamps):
    intervals = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]
    avg_interval = sum(intervals) / len(intervals) if intervals else 0
    score = 100 - (avg_interval * 0.5)
    return max(score, 0)


def extract_diagnostics(meta_strings):
    char_count = 0
    unique_chars = set()
    for s in meta_strings:
        cleaned = s.strip().lower().replace('_', '').replace('-', '')
        char_count += len(cleaned)
        unique_chars.update(cleaned)
    redundancy_factor = char_count / len(unique_chars) if unique_chars else 0
    return char_count, len(unique_chars), redundancy_factor


def validate_integrity(checksums):
    total = 0
    for cs in checksums:
        total ^= int(cs, 16)  
    parity = bin(total).count('1') % 2
    return total if parity == 0 else total >> 1


def aggregate_metrics(log_entries, system_flags):
    temp_debug_1 = len([x for x in log_entries if 'ERROR' in x])
    temp_debug_2 = ''.join([x[0] for x in system_flags if len(x) > 1])
    decoy_sum = sum([len(flag) for flag in system_flags]) * 2
    
    # Critical path begins
    base_events = [e for e in log_entries if e.startswith('SYS')]
    raw_timestamps = [int(e.split(':')[1]) for e in base_events]
    health_score = compute_health_score(raw_timestamps)
    
    diagnostic_parts = [e for e in log_entries if 'META' in e]
    char_total, uniq, factor = extract_diagnostics(diagnostic_parts)
    
    error_events = [e for e in log_entries if 'ERR' in e]
    error_numeric = [int(e.split('ERR')[1].split(';')[0]) for e in error_events if e.split('ERR')[1].isdigit()]
    error_magnitude = sum([e**2 for e in error_numeric]) if error_numeric else 0
    
    flag_values = [hash(f) % 100 for f in system_flags]
    adjusted_flags = [f if f > 10 else f * 3 for f in flag_values]
    flag_entropy = sum([f % 7 for f in adjusted_flags])
    
    # Irrelevant cryptographic red herring
    crypto_buffer = []
    for f in system_flags:
        transformed = ''.join([chr((ord(c) + len(f)) % 26 + 97) for c in f.lower()])
        crypto_buffer.append(transformed)
    
    # Main aggregation logic (affected only by specific components)
    focus_metrics = [
        health_score,
        char_total * 0.1,
        error_magnitude * 0.01,
        flag_entropy
    ]
    
    final_diagnostic = int(sum(focus_metrics) + 0.5)
    return final_diagnostic

# Simulated input data
log_data = [
    'SYS-1000:1684302000', 'SYS-1001:1684302060', 'SYS-1002:1684302125',
    'META-CTRL:ax7_', 'META-DATA:z__k', 'META-CFG:pp--',
    'E-123', 'E-456', 'W-789',
    'ERR4;SRC=A', 'ERR5;SRC=B', 'INFO:READY'
]
system_diagnostics = ['DBG', 'NET_OK', 'DISK_FULL', 'SEC']

# Dead function - unused but plausible
def legacy_calibrate(x): return (x * 0.987) + 1.2

# Unused variables as distractors
decoys = {'a': 1, 'b': [x**3 for x in range(10)], 'c': set('xyz')}
intermediate_result = analyze_event_sequence(log_data)

# Key execution point
final_diagnostic = aggregate_metrics(log_data, system_diagnostics)
print(f"Target result: {final_diagnostic}")