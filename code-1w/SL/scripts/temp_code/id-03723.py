from collections import defaultdict, Counter

# Simulated system telemetry data
timestamps = [1623456780, 1623456789, 1623456795, 1623456801, 1623456810]
raw_events = ['login', 'data_read', 'data_write', 'login', 'heartbeat']
error_codes = [0, 0, 2, 0, 5]
user_ids = ['U7890', 'U1234', 'U1234', 'U7890', 'U5555']

# Distractor: unused error mapping
decoy_error_meaning = {1: 'timeout', 2: 'corruption', 3: 'auth', 4: 'retry', 5: 'hw_fail'}

# Irrelevant network stats (dead code path)
network_stats = defaultdict(lambda: 0)
for event in raw_events:
    if 'data' in event:
        network_stats['transfers'] += 1
    elif event == 'heartbeat':
        network_stats['pings'] += 1

# Initialize system state
system_flags = {
    'secure_mode': True,
    'debug_trace': False,
    'audit_active': True
}

# Misleading intermediate calculation (unused later)
shadow_score = 0
for code in error_codes:
    if code > 0:
        shadow_score += (code ** 2) % 3

# Real processing begins: build log entries
log_entries = []
for i, event in enumerate(raw_events):
    entry = {
        'ts': timestamps[i],
        'event': event,
        'err': error_codes[i],
        'user': user_ids[i]
    }
    log_entries.append(entry)

# Distractor: character frequency analysis with no impact
char_counter = Counter()
for entry in log_entries:
    for char in entry['event']:
        char_counter[char] += 1
unused_entropy = sum(f * f for f in char_counter.values())

# Auxiliary function that appears important but is never called
def analyze_user_patterns(logs):
    user_activity = defaultdict(list)
    for log in logs:
        user_activity[log['user']].append(log['ts'])
    return {u: len(t) for u, t in user_activity.items()}

# Another decoy function with complex logic but zero usage
def compute_event_coherence(events):
    coherence = 1.0
    for i in range(1, len(events)):
        if events[i] == events[i-1]:
            coherence *= 0.9
        elif 'data' in events[i] and 'login' in events[i-1]:
            coherence *= 1.1
    return round(coherence, 4)

# Core logic: used function with nested conditions and bit manipulation
def evaluate_stability(metrics):
    base = len(metrics)
    errors = sum(1 for m in metrics if m['err'] > 0)
    criticals = sum(1 for m in metrics if m['err'] in [2, 5])
    
    # Bitwise interference pattern
    signature = 0xABCDE
    for m in metrics:
        if m['err'] > 0:
            signature ^= (m['ts'] & 0xFF)
    
    # Complex conditional weight
    if errors == 0:
        penalty = 0
    elif system_flags['audit_active']:
        penalty = (errors * 3) + (criticals * 5)
    else:
        penalty = errors * 2
    
    return (base * 100) - (penalty * 10), signature

# Secondary processor with zip and enumerate (actual relevant use)
def extract_user_signals(entries):
    signals = []
    for idx, (a, b) in enumerate(zip(entries, entries[1:])):
        if a['user'] == b['user'] and 'data' in b['event']:
            delta_t = b['ts'] - a['ts']
            # XOR-based anomaly flag
            anomaly_flag = (a['err'] | b['err']) ^ 1
            signals.append(delta_t * (1 + anomaly_flag))
    return sum(signals)

# Main processing function
def process_metrics(logs, flags):
    # Step 1: basic count
    n_logs = len(logs)
    
    # Step 2: stability evaluation (returns tuple)
    stability_score, sig = evaluate_stability(logs)
    
    # Step 3: signal extraction
    dynamic_signal = extract_user_signals(logs)
    
    # Step 4: conditional override check (never triggers due to secure_mode)
    if not flags['secure_mode'] and flags['debug_trace']:
        override = (stability_score // 10) + dynamic_signal
        return override
    
    # Step 5: destructuring assignment from zip
    users = [entry['user'] for entry in logs]
    events = [entry['event'] for entry in logs]
    for u, e in zip(users, events):
        if u == 'U1234' and 'write' in e:
            write_initiator = u  # captured but unused
    
    # Step 6: final computation chain
    temp_result = stability_score + dynamic_signal
    
    # Step 7: apply bitwise adjustment based on signature's parity
    if sig & 1:
        temp_result -= 50
    else:
        temp_result += 25
    
    # Step 8: final diagnostic value
    final_diagnostic = max(100, min(temp_result, 999))  # clamped result
    
    # Output required for execution trace
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execution point of interest
final_diagnostic = process_metrics(log_entries, system_flags)