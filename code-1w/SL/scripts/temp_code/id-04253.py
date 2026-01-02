import math

# Simulated system telemetry data with mixed signal types
def fetch_signal_strength(frequency, phase):
    return abs(math.sin(frequency * phase) * 100)

# Legacy function - unused but looks relevant
def compute_legacy_score(data):
    total = 0
    for x in data:
        if x > 50:
            total += x // 3
    return total

# Noise filter that's never invoked
def apply_noise_gate(samples, threshold=0.1):
    return [s for s in samples if s > threshold]

# Main diagnostic processor
def analyze_event_sequence(events):
    event_codes = {i: events[i] * (i + 1) for i in range(len(events))}
    adjusted = []
    for k, v in event_codes.items():
        if k % 2 == 0:
            adjusted.append(v + 7)
        else:
            adjusted.append(v - 3)
    return adjusted

# Signal clustering by magnitude band
def categorize_signals(values):
    bands = {'low': 0, 'medium': 0, 'high': 0}
    for v in values:
        if v < 30:
            bands['low'] += 1
        elif v < 70:
            bands['medium'] += 1
        else:
            bands['high'] += 1
    return bands

# Core metric aggregator - actually used
def aggregate_metrics(entries, flags):
    # Distractor: irrelevant counters
    temp_buffer = [0] * len(entries)
    for i in range(len(entries)):
        temp_buffer[i] = entries[i] + (i % 5)

    # Real computation begins
    analysis_chain = analyze_event_sequence(entries)
    signal_data = [fetch_signal_strength(x, 0.25) for x in analysis_chain]
    
    # Mask based on system flags using bitwise logic
    mask_value = flags['critical'] << 2 | flags['active']
    masked_results = []
    for s in signal_data:
        if mask_value & 2:
            masked_results.append(s * 0.9)
        else:
            masked_results.append(s * 1.1)

    # Actual answer derivation path
    filtered = [f for f in masked_results if f > 40]
    sorted_filtered = sorted(filtered, reverse=True)
    
    # Key slicing operation to isolate top performers
    top_segment = sorted_filtered[1:4]  # Middle three after sorting descending

    # Final computation
    base_score = sum(top_segment) / len(top_segment)
    penalty = len(entries) * 0.25
    final_score = base_score - penalty

    # Decoy variable that looks important
    diagnostic_trace = {
        'raw_count': len(entries),
        'adjusted_peaks': len([x for x in entries if x > 20]),
        'legacy_metric': compute_legacy_score(entries)
    }

    # The real target variable
    final_diagnostic = int(round(final_score))

    # Dead code branch - never executed due to flag condition
    if flags['debug'] and False:
        correction = math.log(sum(entries) + 1)
        final_diagnostic += int(correction)

    return final_diagnostic

# Simulated input data
log_entries = [12, 15, 22, 8, 31, 19]
system_flags = {
    'critical': 1,
    'active': 1,
    'debug': 0,
    'timeout': 500
}

# Execution point of interest
final_diagnostic = aggregate_metrics(log_entries, system_flags)

# Output result as required
print(f"Result: {final_diagnostic}")