def analyze_component_health(health_str):
    return sum([1 for c in health_str if c == 'U'])


def encrypt_key(key):
    # Irrelevant cryptographic red herring
    encrypted = 0
    for i, char in enumerate(key):
        encrypted ^= ord(char) << (i % 4)
    return encrypted + 1000

def decode_timestamp(ts):
    # Misleading timestamp parser (unused in final result)
    parts = ts.split('.')
    base = int(parts[0])
    frac = int(parts[1]) if len(parts) > 1 else 0
    return base * 1000 + frac

def shift_window(data, offset):
    # Dead code path — never used
    return [data[i % len(data)] for i in range(offset, offset + len(data))]

def compute_entropy(seq):
    from math import log2
    freq = {}
    for item in seq:
        freq[item] = freq.get(item, 0) + 1
    total = len(seq)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 6)

def extract_flags(config_str):
    # Distractor: parses fake config
    flags = {}
    tokens = config_str.split('|')
    for token in tokens:
        if '=' in token:
            k, v = token.split('=', 1)
            flags[k] = v
    return flags.get('MODE', 'NONE')

def merge_states(*states):
    # Complex-looking but unused state merger
    result = {}
    for s in states:
        for k, v in s.items():
            result[k] = result.get(k, 0) ^ (v & 0xFF)
    return result

def calculate_signature(values):
    sig = 0
    for v in values:
        sig = (sig * 31 + v) % 1000003
    return sig

def filter_anomalies(records):
    # Looks important but not part of final computation
    return [r for r in records if r['status'] != 'CRITICAL']

def build_index_map(keys):
    return {k: i for i, k in enumerate(sorted(keys))}

def process_metrics(logs, sys_state):
    # Core relevant logic starts here
    event_codes = []
    for entry in logs:
        code = 0
        if 'ERROR' in entry['type']:
            code += 100
        if entry['retries'] > 2:
            code += 10
        latency = entry['latency_ms']
        if latency > 500:
            code += 1
        event_codes.append(code)
    
    # Real accumulation
    base_score = sum(event_codes)
    
    # Bit manipulation relevant to final answer
    flagged = 0
    for entry in logs:
        if entry['timeout']:
            flagged |= (1 << (entry['node_id'] % 8))
    
    # Key transformation
    temp = base_score ^ flagged
    if temp & 0x1:
        temp = (temp >> 1) ^ 0xABCD
    else:
        temp = (temp >> 1) ^ 0x5678
    
    # Incorporate system state health
    health_str = sys_state['components']
    healthy_count = analyze_component_health(health_str)
    
    # Final formula
    adjustment = sys_state['load_peak'] // 10
    final_value = temp + healthy_count * 5 - adjustment
    
    # Critical assignment
    final_diagnostic = final_value
    
    # Unrelated print (distractor)
    _ = compute_entropy(['A','B','A','C','A','B'])
    
    return final_diagnostic

# --- Simulated data ---
log_entries = [
    {'type': 'ERROR_NETWORK', 'retries': 3, 'latency_ms': 600, 'timeout': True, 'node_id': 2},
    {'type': 'INFO', 'retries': 0, 'latency_ms': 100, 'timeout': False, 'node_id': 5},
    {'type': 'ERROR_DISK', 'retries': 1, 'latency_ms': 800, 'timeout': True, 'node_id': 2},
    {'type': 'ERROR_NETWORK', 'retries': 4, 'latency_ms': 300, 'timeout': False, 'node_id': 7},
]

system_state = {
    'components': 'UUUDUUUU',  # 7 'U' (up), so analyze_component_health returns 7
    'load_peak': 120,
    'uptime': '12489.345',
    'version': 'v2.1|MODE=STANDBY'
}

# --- Unused decoy variables ---
decoy_data = [1024, 2048, 4096]
key_cipher = encrypt_key('admin_session_0x7F')
index_lookup = build_index_map(['node_A', 'node_B', 'node_C'])

# --- Critical execution point ---
final_diagnostic = process_metrics(log_entries, system_state)

# Output result
print(f"Result: {final_diagnostic}")