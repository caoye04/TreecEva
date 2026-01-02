from collections import defaultdict, Counter

# Simulated sensor data aggregation system
def collect_sensor_data(nodes):
    data_store = defaultdict(list)
    for node_id, readings in nodes.items():
        for val in readings:
            if val % 3 == 0:
                data_store['critical'].append(val * 1.1)
            elif val % 5 == 0:
                data_store['warning'].append(val * 0.9)
            else:
                data_store['normal'].append(val)
    return data_store

def generate_fingerprint(values):
    fingerprint = 0
    for i, v in enumerate(values):
        fingerprint ^= (v & (i + 1)) << 1
    return fingerprint

def analyze_trend(data_seq):
    trend_score = 0
    for i in range(1, len(data_seq)):
        if data_seq[i] > data_seq[i-1]:
            trend_score += 1
        elif data_seq[i] < data_seq[i-1]:
            trend_score -= 1
    return abs(trend_score)

def compute_entropy(counts):
    total = sum(counts)
    entropy = 0.0
    for c in counts:
        if c > 0:
            p = c / total
            entropy -= p * __import__('math').log2(p)
    return round(entropy, 6)

def derive_key(signal, mask=0x0F):
    # Irrelevant cryptographic red herring
    key = 0
    for s in signal:
        key = (key * 31 + s) & mask
    return key ^ 0xAA

def decoy_analysis(arr):
    # Dead function: never contributes to final result
    hist = Counter(arr)
    peaks = [k for k, v in hist.items() if v > 1]
    return sorted(peaks, reverse=True)

def validate_checksum(chunk):
    # Unused validation routine (distractor)
    chk = 0
    for b in chunk:
        chk = (chk + b) ^ 0xFF
    return chk == 0x12

# Main processing pipeline
def process_metrics(signature, logs):
    
    # Step 1: Filter and transform raw logs
    filtered = [x for x in logs if x > 0 and x % 2 == 1]
    
    # Step 2: Count frequency categories (red herring computation)
    freq_map = Counter(filtered)
    common_vals = freq_map.most_common(3)
    
    # Step 3: Generate structural fingerprint
    shape = [len(str(x)) for x in filtered]
    health_shape = generate_fingerprint(shape)
    
    # Step 4: Analyze temporal trend in filtered data
    trend_metric = analyze_trend(filtered)
    
    # Step 5: Compute distribution entropy
    counts = list(freq_map.values())
    entropy_value = compute_entropy(counts)
    
    # Step 6: Build diagnostic vector
    diagnostics = []
    for i, val in enumerate(filtered):
        if i % 2 == 0:
            diagnostics.append(val ^ health_shape)
        else:
            diagnostics.append(val + trend_metric)
    
    # Step 7: Aggregate secondary metrics (partially relevant)
    temp_summary = {
        'base': sum(diagnostics) // len(diagnostics) if diagnostics else 0,
        'peak': max(diagnostics, default=0),
        'stable': trend_metric < 3
    }
    
    # Step 8: Cross-reference with signature using set operations
    sig_set = set(bin(x)[2:] for x in signature)
    rev_sig = set(s[::-1] for s in sig_set)
    overlap = sig_set & rev_sig  # Symmetric binary patterns
    mirror_count = len(overlap)
    
    # Step 9: Derive adjustment factor
    adjustment = 1
    for s in signature:
        adjustment += (s ^ mirror_count) & 0x03
    
    # Step 10: Combine into final diagnostic score
    raw_score = temp_summary['base'] * (entropy_value + 1) + adjustment
    final_diagnostic = int(raw_score - temp_summary['peak'] // 2)
    
    # --- KEY STATEMENT ---
    final_diagnostic = process_metrics(health_signature, readings)
    
    # Irrelevant print calls (distractors)
    _ = derive_key(readings[:5])
    __ = decoy_analysis(readings)
    
    return final_diagnostic

# Simulated input data
readings = [15, 22, 9, 18, 7, 41, 33, 12, 5, 29, 11]
health_signature = [10, 12, 15, 17, 20]

# Execute main logic
result = process_metrics(health_signature, readings)
print(f"Target result: {result}")