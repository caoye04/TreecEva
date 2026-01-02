import itertools

def analyze_sequence(data):
    # Irrelevant transformation (dead-end function)
    return [x ** 2 for x in data if x % 3 == 0]

def decode_signal(pattern):
    # Distractor: looks important but unused in critical path
    base = 0
    for i, p in enumerate(pattern):
        base += p << (i % 4)
    return base % 100

def filter_noisy_readings(readings):
    # Real but slightly misleading preprocessing
    cleaned = [r for r in readings if r > -50 and r < 150]
    avg = sum(cleaned) / len(cleaned) if cleaned else 0
    return [r for r in cleaned if abs(r - avg) < 30]

def compute_entropy(values):
    from math import log
    if not values:
        return 0.0
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = 0.0
    for count in freq.values():
        prob = count / total
        entropy -= prob * log(prob) if prob > 0 else 0
    return round(entropy, 6)

def aggregate_diagnostics(sequences):
    # Complex-looking aggregation with red herring logic
    flattened = list(itertools.chain.from_iterable(sequences))
    stats = {
        'max_val': max(flattened),
        'min_val': min(flattened),
        'range': max(flattened) - min(flattened),
        'count_above_50': len([x for x in flattened if x > 50])
    }
    # This intermediate result looks important but isn't used in final answer
    dummy_score = (stats['max_val'] + stats['min_val']) // 2
    return stats

def validate_checksum(tag):
    # String method distractor
    if isinstance(tag, str):
        return sum(ord(c) for c in tag if c.isalpha()) % 11
    return 0

def process_metrics(log_entries, system_threshold):
    # Core logic buried among distractions
    
    # Step 1: Extract numeric payloads from logs
    raw_signals = []
    for entry in log_entries:
        payload = entry.get('payload', [])
        if isinstance(payload, list):
            raw_signals.extend(payload)
    
    # Step 2: Filter out noise
    filtered_data = filter_noisy_readings(raw_signals)
    
    # Step 3: Apply threshold masking
    masked = [x for x in filtered_data if x >= system_threshold]
    
    # Step 4: Count occurrences of each value
    count_map = {}
    for val in masked:
        count_map[val] = count_map.get(val, 0) + 1
    
    # Step 5: Find most frequent value
    primary_mode = max(count_map.items(), key=lambda pair: pair[1])[0] if count_map else 0
    
    # Step 6: Compute secondary metric - entropy of all unique values above threshold
    unique_high_vals = [v for v in set(masked) if v > primary_mode]
    entropy_score = compute_entropy(unique_high_vals)
    
    # Step 7: Apply bit manipulation for final encoding
    encoded = (primary_mode ^ 242) & 511  # Bitwise mix
    
    # Step 8: Final diagnostic computed from encoded mode and entropy
    final_value = encoded + int(entropy_score * 1000)
    
    # Irrelevant final checks (distractors)
    health_flag = 'OK' if final_value < 900 else 'WARNING'
    audit_trail = [validate_checksum(tag) for tag in ['SYS_OK', 'DIAG_1', 'CHK_PASS']]
    
    # Critical assignment
    final_diagnostic = final_value  # <-- Key statement
    
    return final_diagnostic

# Simulated sensor log data (real input)
log_entries = [
    {'timestamp': 1001, 'type': 'sensor', 'payload': [45, 67, 89, 67, 23, 101], 'tag': 'SNSR_A'},
    {'timestamp': 1002, 'type': 'debug',  'payload': [67, 89, 67, 45, -200, 150], 'tag': 'DBG_X'},
    {'timestamp': 1003, 'type': 'sensor', 'payload': [89, 67, 89, 89, 34, 78], 'tag': 'SNSR_B'},
    {'timestamp': 1004, 'type': 'sensor', 'payload': [12, 89, 67, 45, 89, 90], 'tag': 'SNSR_C'}
]

system_threshold = 60

# Dead code paths (unused functions)
decoy_sequence = [3, 6, 9, 12, 15]
analyze_sequence(decoy_sequence)

signal_pattern = [1, 0, 1, 1, 0]
decode_signal(signal_pattern)

# Unused list comprehension with string methods
tags = ['SYS_OK', 'DIAG_1', 'CHK_PASS']
valid_tags = [t.lower() for t in tags if t.endswith('PASS') or t.find('_') > 0]

# Main execution flow
intermediate_stats = aggregate_diagnostics([entry['payload'] for entry in log_entries])

# Key computation
final_diagnostic = process_metrics(log_entries, system_threshold)

# Output result
print(f"Result: {final_diagnostic}")