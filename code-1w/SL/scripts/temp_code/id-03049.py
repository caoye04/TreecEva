from collections import defaultdict, Counter

# Simulated system log analysis with red herrings and distractions
def parse_timestamp(log):
    return int(log.split()[-1]) % 1000

def is_critical_error(log):
    return 'ERR' in log and 'CRITICAL' in log

def extract_severity(log):
    if 'SEV1' in log:
        return 1
    elif 'SEV2' in log:
        return 2
    else:
        return 3

# Distractor function - looks important but unused in final calculation
def deprecated_filter(logs):
    return [log for log in logs if 'DEBUG' not in log]

def compute_entropy(sequence):
    counts = Counter(sequence)
    total = len(sequence)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not actual entropy, just mimicry
    return round(entropy, 4)

def rolling_checksum(data):
    checksum = 0
    for i, val in enumerate(data):
        checksum += val * (i + 1)
    return checksum % 97

def detect_anomaly(pattern):
    if len(pattern) < 3:
        return False
    diffs = [pattern[i+1] - pattern[i] for i in range(len(pattern)-1)]
    return len(set(diffs)) == 1 and diffs[0] != 0

def aggregate_diagnostics(entries, flags):
    result = defaultdict(int)
    severities = []n    timestamps = []
    temp_buffer = []
    
    for entry in entries:
        ts = parse_timestamp(entry)
        sev = extract_severity(entry)
        
        result['total_logs'] += 1
        result['max_severity'] = min(result['max_severity'], sev) if result['max_severity'] > 0 else sev
        
        if is_critical_error(entry):
            result['critical_count'] += 1
            
        severities.append(sev)
        timestamps.append(ts)
        
        # Dead logic branch - never triggered due to data constraints
        if 'TRACE' in entry and flags.get('tracing_active'):
            temp_buffer.append(ts)
    
    # Irrelevant aggregation
    result['avg_severity'] = round(sum(severities) / len(severities), 2) if severities else 0
    result['timestamp_variance'] = round(sum((x - sum(timestamps)/len(timestamps))**2 for x in timestamps) / len(timestamps), 2) if timestamps else 0
    
    # This is a decoy computation - looks sophisticated but unused
    fake_pattern = [1, 1, 2, 3, 5, 8]
    if detect_anomaly(fake_pattern):
        result['hidden_flag'] = rolling_checksum(fake_pattern)
    
    # Real signal: count how many times SEV1 appears in first half vs second half
    mid = len(severities) // 2
    first_half = severities[:mid].count(1)
    second_half = severities[mid:].count(1)
    
    result['trend_score'] = (second_half - first_half) * 50
    
    return result

def analyze_pattern(logs, config):
    # Core analysis mixed with distractions
    raw_data = [f"{log}-processed" for log in logs if 'ERR' in log]
    
    # Meaningless transformation chain
    transformed = list(map(str.upper, raw_data))
    filtered = [t for t in transformed if 'CRITICAL' in t]
    cleaned = [t.replace('-PROCESSED', '') for t in filtered]
    
    # Another decoy structure
    metadata_summary = {
        'version': '2.1a',
        'schema': [3, 1, 4],
        'checksum': sum([len(x) for x in cleaned]) * 7 % 13
    }
    
    # Actual work happens here, buried in noise
    base_diag = aggregate_diagnostics(logs, config)
    
    # Distractor: complex-looking but unused bitwise cascade
    shadow_state = 0xABCDE
    for i in range(len(logs) % 7):
        shadow_state ^= (shadow_state << 3) & 0xFFFF
        shadow_state >>= 1
    
    # Critical branching logic - depends on configuration and patterns
    if config.get('enable_enhanced_detection') and base_diag['critical_count'] > 0:
        base_diag['refined_alert'] = True
        anomaly_seed = [parse_timestamp(log) % 25 for log in logs if is_critical_error(log)]
        if detect_anomaly(anomaly_seed):
            base_diag['anomaly_confirmed'] = rolling_checksum(anomaly_seed)
        else:
            base_diag['anomaly_confirmed'] = 113
    else:
        base_diag['refined_alert'] = False
        base_diag['anomaly_confirmed'] = 0
    
    # Final computation - only this matters
    trend_value = base_diag['trend_score']
    confirmation_code = base_diag['anomaly_confirmed']
    critical_incidents = base_diag['critical_count']
    
    # The real answer formula hidden among distractions
    final_diagnostic = (trend_value + confirmation_code) * (1 if critical_incidents > 0 else 0)
    
    # Red herring output that looks important
    debug_snapshot = {
        'state_vector': [final_diagnostic % i if i != 0 else 0 for i in range(5)],
        'coherence': compute_entropy([final_diagnostic % 10, final_diagnostic % 7, final_diagnostic % 5])
    }
    
    return final_diagnostic

# Simulated input data with embedded patterns
log_entries = [
    "SYS: ERR SEV1 CRITICAL failure at 1500",
    "NET: timeout recovery 1501",
    "SEC: ERR SEV2 firewall breach 1502",
    "AUD: user logout 1503",
    "SYS: ERR SEV1 CRITICAL degradation 1504",
    "MON: high CPU 1505",
    "SYS: ERR SEV1 CRITICAL overload 1506",
    "COM: protocol handshake 1507",
    "SYS: ERR SEV2 degraded mode 1508",
    "FAC: ERR SEV1 CRITICAL shutdown 1509"
]

system_flags = {
    'enable_enhanced_detection': True,
    'tracing_active': False,
    'debug_mode': 'inhibited'
}

# Execute main analysis
diag_result = aggregate_diagnostics(log_entries, system_flags)
final_diagnostic = analyze_pattern(log_entries, system_flags)

print(f"Result: {final_diagnostic}")