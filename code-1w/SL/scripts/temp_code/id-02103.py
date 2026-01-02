from itertools import cycle, islice

def analyze_signal_integrity(raw_samples, threshold=0.75):
    # Irrelevant preprocessing: amplitude normalization (not used in final path)
    normalized = [min(max(x, -1.0), 1.0) for x in raw_samples]
    filtered = [x for x in normalized if abs(x) > 0.1]
    
    # Distractor: frequency estimation with unused result
    phase_accumulator = 0.0
    estimated_freqs = []
    for s in filtered:
        phase_accumulator += s * 0.5
        estimated_freqs.append(phase_accumulator % 1.0)
    
    # Relevant logic: count coherent oscillations above threshold
    coherence_count = 0
    for i in range(1, len(filtered)):
        if filtered[i] * filtered[i-1] > 0 and abs(filtered[i]) > threshold:
            coherence_count += 1
    
    return coherence_count

def generate_synthetic_pattern(seed_offset):
    # Generates a decoy data pattern that looks important but is unused
    base = [(i * seed_offset) % 7 for i in range(15)]
    return [x ** 2 if x % 2 == 0 else x + 1 for x in base]

def extract_metadata_features(context_str):
    # Real but partially irrelevant feature extraction
    upper_count = sum(1 for c in context_str if c.isupper())
    digit_pairs = [context_str[i:i+2] for i in range(len(context_str)-1) if context_str[i].isdigit()]
    ascii_sum = sum(ord(c) for c in context_str if c in 'AEIOU')
    
    # This result is only partially used (only ascii_sum matters later)
    return {'uc': upper_count, 'dp': len(digit_pairs), 'as': ascii_sum}

def aggregate_metrics(chain, logs):
    # Core accumulation logic
    total_weight = 0
    for item in chain:
        if isinstance(item, dict) and 'weight' in item:
            total_weight += item['weight'] * 0.85
    
    # Critical computation branch
    adjustment_factor = logs.get('peak_coherence', 0) * 0.3
    if logs.get('diagnostics_active', False):
        adjustment_factor += logs.get('baseline_drift', 0) * 0.1

    # Red herring: complex string transformation with no impact
    status_tags = ['ERR', 'OK', 'WARN']
    tag_cycle = cycle(status_tags)
    synthetic_trace = ''.join(islice(tag_cycle, len(logs.get('history', []))))

    # Decoy dictionary mutation
    temp_report = {'status': 'nominal', 'flags': [], 'version': '2.1'}
    temp_report['checksum'] = sum(ord(c) for c in temp_report['status']) % 100

    # Actual key computation
    base_metric = total_weight + adjustment_factor
    if base_metric > 10:
        base_metric = base_metric / 1.5
    return round(base_metric, 4)

def main():
    # Input signal data (simulated sensor readings)
    sensor_readings = [0.81, -0.23, 0.91, 0.77, 0.85, -0.65, 0.93, 0.12, -0.05, 0.88]

    # Unused synthetic pattern (distractor)
    phantom_pattern = generate_synthetic_pattern(seed_offset=13)

    # Extract metadata from configuration context
    ctx_string = "CALIB_2024_ALPHA_V2\nUSER:ADMIN\nREGION=NA"
    features = extract_metadata_features(ctx_string)
    
    # Signal analysis (produces relevant metric)
    peak_coherence = analyze_signal_integrity(sensor_readings, threshold=0.75)
    
    # Build processing chain with mixed relevance
    processing_chain = [
        {'type': 'filter', 'weight': 12.0, 'active': True},
        {'type': 'amplify', 'weight': 8.5, 'active': False},
        {'type': 'shift', 'weight': 5.0, 'active': True},
        'dummy_entry',  # Invalid type, skipped in processing
        {'type': 'scale', 'weight': 10.0, 'active': True}
    ]
    
    # Diagnostic log with mixed relevant/irrelevant fields
    diagnostics = {
        'peak_coherence': peak_coherence,
        'baseline_drift': 4.2,
        'sample_rate': 128,
        'version': '3.0a',
        'history': ['OK', 'OK', 'ERR'],
        'diagnostics_active': True,
        'timestamp': '2024-05-21T10:30:00Z',
        'uc_features': features['uc'],
        'as_checksum': features['as']
    }
    
    # Dead code path: conditional that never triggers (red herring)
    if len(phantom_pattern) > 50:
        fallback_value = sum(phantom_pattern) / len(phantom_pattern)
        diagnostics['peak_coherence'] = int(fallback_value)
    
    # Key execution point
    final_diagnostic = aggregate_metrics(processing_chain, diagnostics)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")

if __name__ == '__main__':
    main()