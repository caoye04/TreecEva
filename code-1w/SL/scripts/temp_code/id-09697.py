from collections import defaultdict, Counter
import itertools

# Simulate low-level system telemetry processing with diagnostic flags
def analyze_timing_sequence(raw_intervals):
    interval_stats = defaultdict(float)
    anomalies = []
    baseline = 0.5
    for i, interval in enumerate(raw_intervals):
        if i % 7 == 0:
            # Red herring: rarely executed normalization
            baseline = (baseline + interval) / 2
        deviation = abs(interval - baseline)
        interval_stats['total_deviation'] += deviation
        if deviation > 0.8:
            anomalies.append(i)
    interval_stats['anomaly_count'] = len(anomalies)
    return dict(interval_stats)

# Legacy function – unused but looks relevant
def compute_legacy_score(events):
    score = 0
    for e in events:
        if e['type'] == 'IRQ':
            score -= 1
        elif e['type'] == 'ACK':
            score += 2
    return score * 0.9

# Core data transformation pipeline
def extract_signal_envelope(timestamps):
    envelope = []
    for i in range(1, len(timestamps)):
        delta = timestamps[i] - timestamps[i-1]
        if delta < 0.1:
            continue  # suppress noise
        envelope.append(delta ** 0.5)
    return envelope

# Flag-based routing and filtering
def filter_by_system_state(signal_data, flags):
    result_stream = []
    state_mask = flags.get('mode', 1) & 3
    threshold = 0.65
    if flags.get('turbo'):
        threshold *= 0.5
    for val in signal_data:
        # Simulated hardware-dependent filtering
        if state_mask == 0:
            if val > threshold * 2:
                result_stream.append(val * 1.1)
        elif state_mask == 1:
            if val > threshold:
                result_stream.append(val)
        elif state_mask == 2:
            capped_val = min(val, threshold * 1.5)
            result_stream.append(capped_val)
        else:
            result_stream.append(val * 0.9)
    return result_stream

# Aggregation with combinatorics side-channel
def generate_combinations(data):
    # Distractor: generates combinations but only size is used
    count = 0
    for r in range(2, 4):
        for _ in itertools.combinations(data, r):
            count += 1
            if count > 10000:  # early break to avoid explosion
                break
    return count

# Main diagnostic aggregator
def aggregate_metrics(log_entries, sys_flags):
    timing_data = [entry['delta_t'] for entry in log_entries if entry['valid']]
    
    # Step 1: Extract physical signal characteristics
    envelope = extract_signal_envelope([e['ts'] for e in log_entries])
    processed_signal = filter_by_system_state(envelope, sys_flags)
    
    # Step 2: Analyze timing anomaly profile
    analysis_report = analyze_timing_sequence(timing_data)
    
    # Step 3: Compute combinatorial complexity metric (distractor-heavy)
    combo_metric = generate_combinations(processed_signal[:10]) if len(processed_signal) > 5 else 0
    
    # Step 4: Weighted fusion of metrics (only some inputs matter)
    base_score = sum(processed_signal) * 100
    penalty = analysis_report.get('anomaly_count', 0) * 500
    bonus = combo_metric // 1000  # Minimal impact, looks important
    
    # Critical calculation: final diagnostic value
    final_score = base_score - penalty + bonus
    
    # Dead code branch - never reached due to logic above
    if len(processed_signal) < 0:  # Always false
        fallback = Counter(processed_signal)
        final_score = fallback[0] * 1000
    
    # Irrelevant counters for cache simulation
    cache_stats = defaultdict(int)
    for val in timing_data:
        bucket = int(val * 10)
        cache_stats[bucket] += 1
    
    return int(final_score)

# Simulated telemetry input
timing_log = [
    {'ts': 0.0, 'delta_t': 0.12, 'valid': True},
    {'ts': 0.15, 'delta_t': 0.15, 'valid': True},
    {'ts': 0.35, 'delta_t': 0.20, 'valid': True},
    {'ts': 0.60, 'delta_t': 0.25, 'valid': True},
    {'ts': 0.90, 'delta_t': 0.30, 'valid': True},
    {'ts': 1.25, 'delta_t': 0.35, 'valid': True},
    {'ts': 1.65, 'delta_t': 0.40, 'valid': True},
    {'ts': 2.10, 'delta_t': 0.45, 'valid': True},
    {'ts': 2.60, 'delta_t': 0.50, 'valid': True},
    {'ts': 3.15, 'delta_t': 0.55, 'valid': True}
]

# System configuration with misleading flags
system_flags = {
    'mode': 7,          # Only lower 2 bits matter
    'turbo': False,
    'debug': True,      # Unused
    'safe_mode': True   # Unused
}

# Execute core computation
final_diagnostic = aggregate_metrics(timing_log, system_flags)
print(f"Result: {final_diagnostic}")