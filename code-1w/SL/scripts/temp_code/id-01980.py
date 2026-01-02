def analyze_signal(samples, threshold=0.7):
    filtered = [s for s in samples if abs(s) > threshold]
    magnitude_sum = sum(abs(x) for x in filtered)
    peak_count = len(filtered)
    
    # Irrelevant signal stats (distractor)
    avg_noise = sum(abs(x) for x in samples) / len(samples) if samples else 0
    noise_floor = avg_noise * 0.3
    suppression_factor = 1.0
    if noise_floor > 0.5:
        suppression_factor = 0.8
    
    return {'magnitude': magnitude_sum, 'peaks': peak_count}


def compute_entropy(data):
    from math import log2
    freq = {}
    total = len(data)
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    entropy = -sum((count / total) * log2(count / total) for count in freq.values())
    return entropy

# Simulate sensor data streams (mixed relevance)
sensor_a = [0.1, -0.4, 0.85, -1.2, 0.3, 0.91, -0.77, 0.02]
sensor_b = [0.65, 0.71, -0.2, 0.5, 1.05, -0.98, 0.44]
sensor_c = [x * 0.9 for x in sensor_a]  # Correlated but irrelevant

# Primary analysis path
analysis_report = []
for idx, sig in enumerate([sensor_a, sensor_b]):
    result = analyze_signal(sig, threshold=0.75)
    result['id'] = f'S{idx+1}'
    analysis_report.append(result)

# Distractor: unused entropy calculations
entropy_a = compute_entropy([round(x, 1) for x in sensor_a])
entropy_b = compute_entropy([round(x, 1) for x in sensor_b])
entropy_c = compute_entropy([round(x, 1) for x in sensor_c])

# Diagnostic flags (some relevant, some red herrings)
diagnostic_flags = {
    'SATURATION_DETECTED': False,
    'NOISE_SPIKE': True,  # Misleading flag
    'VALID_PEAKS_PRESENT': True,
    'CROSS_TALK_WARNING': False
}

# Data fusion chain with decoy operations
processing_chain = []
for report in analysis_report:
    score = report['magnitude'] * (report['peaks'] + 1)
    normalized_score = min(score / 5.0, 2.0)
    processing_chain.append(normalized_score)
    
    # Dead code path (never used)
    if report['magnitude'] > 10:
        adjusted = score * 0.95
        processing_chain.append(adjusted)

# Unused alternate processing (distractor)
alt_chain = [x ** 0.5 for x in processing_chain if x > 0.5]
sorted_chain = sorted(alt_chain, reverse=True)
trimmed = sorted_chain[1:3]

# Real aggregation logic buried among distractions
def aggregate_metrics(chain, flags):
    base = sum(chain)
    adjustment = 0.0
    
    # Conditional adjustments (only one applies)
    if flags['SATURATION_DETECTED']:
        adjustment -= 0.5
    elif flags['VALID_PEAKS_PRESENT']:
        adjustment += 1.8  # This triggers
    
    if len(chain) > 3:
        adjustment += 0.3
    else:
        adjustment -= 0.1  # Executes due to chain length = 2
    
    # Final computation
    raw_total = base + adjustment
    
    # Extra obfuscation via set and dict ops (partially relevant)
    history_log = {f'entry_{i}': val for i, val in enumerate(chain)}
    keys_set = set(history_log.keys())
    aux_set = {f'entry_{j}' for j in range(len(chain) + 5)}
    overlap = keys_set & aux_set  # Always full match, but distracts
    
    # Slicing distraction
    chain_slice = chain[:len(chain)]
    slice_sum = sum(chain_slice)
    
    # The real answer only depends on raw_total
    final_value = round(raw_total * 100) / 100
    return final_value

# Spurious function calls (no side effects)
dummy_report = analyze_signal([], threshold=0.1)
dummy_entropy = compute_entropy([0, 1, 1, 0])

# Critical execution point
diagnostics = diagnostic_flags
diagnostics['TIMESTAMP_SYNCED'] = True  # Additional red herring
final_diagnostic = aggregate_metrics(processing_chain, diagnostics)

print(f"Result: {final_diagnostic}")