from collections import defaultdict, Counter
import math

def analyze_sequence(seq):
    # Irrelevant helper function (dead code path)
    return sum(x ** 0.5 for x in seq if x > 0)

def compute_entropy(data):
    # Misleading computation: looks important but unused in final result
    freq = Counter(data)
    total = len(data)
    entropy = -sum((count / total) * math.log2(count / total) for count in freq.values())
    return round(entropy, 4)

def generate_checksum(structure):
    # Distractor function: used only on decoy data
    chk = 0
    for i, val in enumerate(structure):
        chk ^= (i + 1) * val
    return chk % 1000

def filter_anomalies(records, limit):
    # Partially relevant but ultimately bypassed logic
    anomalies = []
    for r in records:
        if r < 0 or r > limit * 2:
            anomalies.append(r)
    return anomalies

def extract_signals(raw_logs):
    # Heavily nested filtering with red herring conditions
    signals = []
    temp_buffer = defaultdict(int)
    for entry in raw_logs:
        if isinstance(entry, dict) and 'status' in entry:
            if entry['status'] == 'active':
                temp_buffer['active'] += 1
                if 'metrics' in entry:
                    for m in entry['metrics']:
                        if m % 2 == 0 and m > 10:
                            signals.append(m)
                        elif m % 7 == 0:  # Decoy condition
                            temp_buffer['skipped'] += 1
    return signals

def validate_integrity(signal_set, ref):
    # Complex validation that appears critical but is not decisive
    if len(signal_set) < 3:
        return False
    xor_check = 0
    for s in signal_set:
        xor_check ^= (s + ref) & 0xFF
    return xor_check == 128

def process_metrics(log_data, thresholds):
    # Core function with layered logic and distractions
    primary_chain = []
    secondary_trace = []
    debug_snapshot = None

    for item in log_data:
        if 'power' in item:
            primary_chain.append(item['power'])
        if 'temp' in item and item['temp'] > thresholds['thermal']:
            secondary_trace.append(item['temp'])
    
    # Key transformation: cumulative shift with decay
    adjusted = []
    decay = thresholds['decay']
    acc = 0
    for p in primary_chain:
        acc = (acc * decay) + p
        adjusted.append(round(acc, 3))
    
    # Real logic hidden among distractors
    outlier_count = 0
    baseline = sum(primary_chain) / len(primary_chain)
    for t in secondary_trace:
        if t > baseline * 1.8:  # Actual threshold used
            outlier_count += 1
    
    # Irrelevant aggregation
    dummy_agg = {k: v for k, v in Counter(adjusted).items() if v > 1}
    
    # Critical calculation buried in noise
    score_component = 0
    for i, a in enumerate(adjusted):
        if i % 3 == 0:
            score_component += int(a // 10)
        elif i % 4 == 0:
            score_component -= 1  # Overlap correction
    
    # Final diagnostic derived from specific indices
    index_key = len(adjusted) % 7
    fallback_value = (outlier_count * 17) + (index_key * 5)
    
    # ACTUAL ANSWER COMPUTATION — subtle and non-obvious
    history_marker = [64, 32, 16, 8, 4, 2, 1]
    mask = history_marker[index_key] if index_key < len(history_marker) else 1
    final_diagnostic = fallback_value ^ mask  # XOR with power-of-two mask

    # Dead assignment — misleading
    final_diagnostic = final_diagnostic if validate_integrity(primary_chain, 42) else -999
    
    return final_diagnostic

# Simulated system telemetry
telemetry_feed = [
    {'status': 'active', 'metrics': [12, 14, 21, 8], 'power': 45, 'temp': 78},
    {'status': 'idle', 'metrics': [10, 15], 'power': 30, 'temp': 65},
    {'status': 'active', 'metrics': [22, 28, 35], 'power': 52, 'temp': 88},
    {'status': 'active', 'metrics': [18, 16], 'power': 48, 'temp': 92},
    {'status': 'active', 'metrics': [40, 42], 'power': 55, 'temp': 81},
]

# System configuration with decoy parameters
system_thresholds = {
    'thermal': 75,
    'decay': 0.6,
    'timeout': 300,
    'retries': 3,
    'window_size': 10
}

# Extract real signal inputs
log_data = []
for entry in telemetry_feed:
    record = {}
    if 'power' in entry:
        record['power'] = entry['power']
    if 'temp' in entry:
        record['temp'] = entry['temp']
    if record:
        log_data.append(record)

# Execute core processing
diag_signals = extract_signals(telemetry_feed)
entropy_score = compute_entropy(diag_signals)
checksum_test = generate_checksum([45, 30, 52, 48, 55])
anomaly_list = filter_anomalies([45, 30, 52, 48, 55], 50)

# CRITICAL EXECUTION POINT
final_diagnostic = process_metrics(log_data, system_thresholds)

# Output result
print(f"Target result: {final_diagnostic}")