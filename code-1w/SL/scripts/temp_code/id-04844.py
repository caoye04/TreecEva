from collections import defaultdict, Counter
import math

# Simulated system log analysis with diagnostic scoring

def preprocess_logs(raw_logs):
    processed = []
    for entry in raw_logs:
        parts = entry.split('|')
        if len(parts) < 3:
            continue
        timestamp, level, msg = parts[0], parts[1], '|'.join(parts[2:])
        severity = 1 if level == 'WARN' else (2 if level == 'ERROR' else 0)
        processed.append({'time': timestamp, 'severity': severity, 'msg': msg, 'length': len(msg)})
    return processed

# Irrelevant helper - distractor function
def calculate_entropy(data):
    if not data:
        return 0.0
    counts = Counter(data)
    total = len(data)
    entropy = -sum((count / total) * math.log2(count / total) for count in counts.values())
    return round(entropy, 4)

# Decoy pattern matcher - never actually used in final computation
def detect_attack_patterns(entries):
    patterns = defaultdict(int)
    for e in entries:
        if 'exploit' in e['msg']:
            patterns['exploit'] += 1
        if 'port scan' in e['msg']:
            patterns['scan'] += 1
    return dict(patterns)

# Core logic: score anomaly based on message repetition and severity timeline

def compute_anomaly_score(entries):
    if not entries:
        return 0
    
    # Track repeating messages
    message_count = Counter(e['msg'] for e in entries)
    repeat_bonus = sum(1 for count in message_count.values() if count > 2)
    
    # Analyze severity progression
    high_severity_spikes = 0
    prev_sev = 0
    for e in entries:
        if e['severity'] > prev_sev:
            high_severity_spikes += 1
        prev_sev = e['severity']
    
    # Compute base anomaly using character distribution oddity (real but subtle)
    all_chars = ''.join(e['msg'] for e in entries)
    char_freq = Counter(all_chars)
    rare_chars = sum(1 for f in char_freq.values() if f < 2)
    
    return (repeat_bonus * 7) + (high_severity_spikes * 3) + (rare_chars // 5)

# Unused recursive counter - red herring

def recursive_counter(n, acc=0):
    if n <= 0:
        return acc
    return recursive_counter(n - 2, acc + (n % 3))

# Main analyzer combining multiple factors

def analyze_pattern(entries, flags):
    base_score = compute_anomaly_score(entries)
    
    # Distractor variables
    temp_debug = [x for x in range(len(entries)) if x % 7 == 0]
    dummy_map = {i: chr(97 + (i * 3) % 26) for i in range(15)}
    
    # Real modifier: check system flags
    flag_multiplier = 1
    if 'DEBUG_MODE' in flags:
        flag_multiplier += 0.5
    if 'VERBOSE_LOGGING' in flags and len(entries) > 10:
        flag_multiplier += 0.3
    
    # Hidden dependency: longest message affects stability
    max_length = max((e['length'] for e in entries), default=0)
    stability_penalty = max(0, 5 - (max_length // 50))
    
    # Final diagnostic calculation (this is what matters)
    intermediate = base_score * flag_multiplier
    final_diagnostic = int(intermediate - stability_penalty + 11)
    
    # Dead code path - misleading print
    if False:
        print(f'Debug scores: base={base_score}, flag_x={flag_multiplier}')
    
    return final_diagnostic

# Simulated input data
raw_log_data = [
    '12:01|INFO|System initialized',
    '12:02|INFO|Network interface up',
    '12:03|WARN|High latency detected',
    '12:04|WARN|High latency detected',
    '12:05|WARN|High latency detected',
    '12:06|ERROR|Connection timeout',
    '12:07|ERROR|Connection timeout',
    '12:08|INFO|Retrying connection',
    '12:09|INFO|Retrying connection',
    '12:10|INFO|Retrying connection',
    '12:11|ERROR|Authentication failed',
    '12:12|ERROR|Authentication failed',
    '12:13|ERROR|Authentication failed',
    '12:14|WARN|Session expired',
    '12:15|INFO|User logout'
]

system_diagnostics = {'BOOT_SEQUENCE': True, 'DEBUG_MODE': True, 'FIREWALL_ACTIVE': True}

# Preprocess logs
log_entries = preprocess_logs(raw_log_data)

# Extract flag set for analysis
system_flags = set(key for key, val in system_diagnostics.items() if val)

# Execute main analysis
final_diagnostic = analyze_pattern(log_entries, system_flags)

# Output result
print(f"Result: {final_diagnostic}")