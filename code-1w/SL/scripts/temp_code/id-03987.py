def analyze_sequence(seq):
    return sum(x ** 2 for x in seq if x % 2 == 1)

# Irrelevant helper function (dead code path)
def decrypt_key(key_str):
    return ''.join(chr(ord(c) - 1) for c in key_str[::-1])

# Unused cryptographic constant (red herring)
crypto_salt = [0xabc, 0xdef, 0x123, 0x456]

# Simulated system telemetry with mixed data types
raw_telemetry = [
    'node_A:up', 'node_B:down', 'node_C:up',
    'power_87%', 'temp_42C', 'load_0.65'
]

# Extract numeric statuses using string methods
system_status = {}
for entry in raw_telemetry:
    if 'node_' in entry:
        node, status = entry.split(':')
        system_status[node] = 1 if status == 'up' else 0
    elif 'power_' in entry:
        power_val = int(entry.strip('power_%'))
    elif 'temp_' in entry:
        temp_val = int(entry.strip('temp_C'))
    elif 'load_' in entry:
        load_val = float(entry.strip('load_'))

# Decoy data structure (distractor)
security_audit = {
    'hash': 'a1b2c3d4',
    'verified': False,
    'timestamp': 1678886400,
    'anomaly_score': 0.88
}

# Real operational log with embedded counts
log_data = [
    {'event': 'START', 'code': 100, 'meta': 'init'},
    {'event': 'READ', 'code': 205, 'meta': 'data_fetch'},
    {'event': 'READ', 'code': 205, 'meta': 'data_fetch'},
    {'event': 'WRITE', 'code': 301, 'meta': 'commit'},
    {'event': 'ERROR', 'code': 500, 'meta': 'server_fault'},
    {'event': 'RETRY', 'code': 205, 'meta': 'retry_fetch'},
    {'event': 'WRITE', 'code': 301, 'meta': 'commit'},
    {'event': 'END', 'code': 101, 'meta': 'cleanup'}
]

# Auxiliary transformation (partially relevant)
event_counts = {}
for log in log_data:
    evt = log['event']
    event_counts[evt] = event_counts.get(evt, 0) + 1

# Bit manipulation decoy (irrelevant computation)
shadow_flag = 0
for i in range(4):
    shadow_flag ^= (i * 2 + 1) << i

# Unused complex expression (misleading intermediate)
baseline_score = (analyze_sequence([3, 5, 7, 9]) + 42) / 2

# System state derived from status map
system_state = sum(system_status.values())  # Number of up nodes

# Distractor: fake entropy calculation (never used)
entropy_pool = [abs(hash(str(i)) % 100) for i in range(5)]
entropy_score = sum(entropy_pool) / len(entropy_pool)

# Core logic disguised among noise
threshold_met = system_state >= 2
error_occurred = any(log['code'] == 500 for log in log_data)
retry_count = event_counts.get('RETRY', 0)
write_count = event_counts.get('WRITE', 0)

# Conditional expression chain with accumulation
if threshold_met and error_occurred:
    if retry_count > 0:
        adjusted_writes = write_count + retry_count // 2
    else:
        adjusted_writes = max(write_count - 1, 0)
    
    # Nested condition with string processing distraction
    recovery_tag = "R" + str(retry_count)
    recovery_code = sum(ord(c) for c in recovery_tag) % 100
    
    # Key accumulation step buried in logic
    diagnostic_base = adjusted_writes * 1000 + recovery_code
    
    # Red herring: unused bit operation
    diagnostic_base |= (1 << 3)
    
    # Final adjustment based on event pattern
    read_events = [l for l in log_data if l['event'] == 'READ']
    if all('fetch' in l['meta'].lower() for l in read_events):
        diagnostic_base += 50
    
    final_diagnostic = diagnostic_base
else:
    # Dead branch (condition not met)
    final_diagnostic = -9999

# Print result as required
print(f"Target result: {final_diagnostic}")