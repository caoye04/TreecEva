def analyze_sequence(data_points):
    cumulative = 0
    temp_cache = []
    for val in data_points:
        if val % 3 == 0 and val % 5 != 0:
            cumulative += val ** 2
        elif val % 7 == 0:
            cumulative -= val // 2
    return cumulative

# Irrelevant helper (dead path)
def unused_validator(x):
    return x > 0 and bin(x).count('1') % 2 == 0

# Unused transformation chain
def transform_signal(signal):
    shifted = [s << 1 for s in signal if s > 10]
    return [s ^ 7 for s in shifted]

# Real processing functions
def filter_critical(entries):
    return {e['id'] for e in entries if e['severity'] > 75}

def compute_entropy(values):
    from math import log2
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p) if p > 0 else 0
    return round(entropy, 6)

def merge_diagnostics(flags, anomalies):
    flag_set = set(flags)
    anomaly_dict = {a['code']: a['weight'] for a in anomalies}
    score = 0
    for f in flag_set:
        if f in ['ERR', 'CRIT']:
            score += 15
        elif f == 'WARN':
            score += 5
    for code, weight in anomaly_dict.items():
        if code.startswith('X'):
            score += weight // 3
    return score

def evaluate_stability(logs, flags):
    # Extract relevant IDs
    critical_ids = filter_critical(logs)
    
    # Decoy computation on strings
    decoy_text = "".join([chr(97 + (len(str(log['id'])) % 26)) for log in logs])
    decoy_hash = sum(ord(decoy_text[i]) * (i + 1) for i in range(len(decoy_text)))
    
    # Real number extraction
    numeric_traces = [log['trace_id'] for log in logs if 'trace_id' in log]
    base_entropy = compute_entropy(numeric_traces)
    
    # Flag-based scoring
    flag_score = merge_diagnostics(flags, [{'code': 'X1', 'weight': 30}, {'code': 'Y2', 'weight': 10}])
    
    # Dummy list mutation
    phantom_buffer = [0] * 5
    for i in range(len(phantom_buffer)):
        phantom_buffer[i] = (i * 17) % 11
        if phantom_buffer[i] == 7:
            break  # Dead-end logic
    
    # Core calculation
    raw_sum = sum(critical_ids)
    adjustment = len(numeric_traces) * base_entropy
    
    # Final formula
    result = int((raw_sum + flag_score) - adjustment + base_entropy)
    
    # Key assignment point
    final_diagnostic = result
    return final_diagnostic

# Simulated input data
log_entries = [
    {'id': 105, 'severity': 82, 'trace_id': 2001},
    {'id': 210, 'severity': 67, 'trace_id': 2002},
    {'id': 315, 'severity': 91, 'trace_id': 2001},
    {'id': 420, 'severity': 45, 'trace_id': 2003},
    {'id': 525, 'severity': 88, 'trace_id': 2002}
]

system_flags = ['INFO', 'WARN', 'CRIT', 'ERR']

# Misleading pre-processing
preliminary = analyze_sequence([x for x in range(10, 40, 3)])
decoy_signal = transform_signal([12, 15, 18, 25, 35])

# Critical execution point
final_diagnostic = evaluate_stability(log_entries, system_flags)

print(f"Target result: {final_diagnostic}")