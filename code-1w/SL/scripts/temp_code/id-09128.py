from collections import defaultdict, Counter
import math

# Simulated system telemetry processing with diagnostic evaluation
def analyze_phase_coherence(timestamps, threshold=0.05):
    if len(timestamps) < 2:
        return False
    coherence = all(abs(timestamps[i+1] - timestamps[i]) < threshold for i in range(len(timestamps)-1))
    debug_snapshot = [abs(t - timestamps[i-1]) for i, t in enumerate(timestamps) if i > 0]
    normalization_factor = sum(debug_snapshot) / len(debug_snapshot) if debug_snapshot else 1.0
    return coherence and normalization_factor < 0.1

def evaluate_signal_integrity(signal_chain):
    baseline = signal_chain.get('baseline', [])
    samples = signal_chain.get('samples', [])
    if not samples:
        return 0
    sample_avg = sum(samples) / len(samples)
    deviation = [abs(s - sample_avg) for s in samples]
    max_dev = max(deviation) if deviation else 0
    return int(sample_avg * (1 - min(max_dev, 0.3)))

def compute_calibration_weight(config_layer):
    weight = 0
    for k, v in config_layer.items():
        if 'calib' in k:
            weight += v ** 0.5 if v > 0 else 0
    return int(weight * 100)

def generate_timing_fingerprint(exec_seq):
    fingerprint = defaultdict(int)
    for item in exec_seq:
        fingerprint['len_' + str(len(item))] += 1
        fingerprint['has_digit'] += any(c.isdigit() for c in item)
    fp_values = list(fingerprint.values())
    return sum(fp_values[i] * (i+1) for i in range(len(fp_values))) % 17

def detect_anomaly_pattern(metrics_log):
    anomalies = 0
    for val in metrics_log:
        if isinstance(val, dict) and 'score' in val:
            if val['score'] < 0.1 or val['score'] > 0.9:
                anomalies += 1
    return anomalies > 2

def recursive_diagnostic_probe(depth, cache=None):
    if cache is None:
        cache = {}
    if depth <= 0:
        return 1
    if depth in cache:
        return cache[depth]
    result = recursive_diagnostic_probe(depth-1, cache) + recursive_diagnostic_probe(depth-2, cache)
    cache[depth] = result
    return result

def validate_consistency_trace(trace_data):
    if not trace_data:
        return False
    sorted_triggers = sorted([x for x in trace_data if isinstance(x, int) and x > 0])
    if len(sorted_triggers) < 2:
        return False
    diffs = [sorted_triggers[i+1] - sorted_triggers[i] for i in range(len(sorted_triggers)-1)]
    return all(d == diffs[0] for d in diffs)

def aggregate_metrics(log_entries, flags):
    # Core logic path
    timing_log = [entry['timing'] for entry in log_entries if 'timing' in entry]
    signal_block = {'samples': [e.get('amplitude', 0) for e in log_entries], 'baseline': [0.5, 0.6]}
    config_map = {f'calib_{i}': t**0.5 for i, t in enumerate(timing_log)}
    exec_sequence = [f'op_{int(t*100)}' for t in timing_log]

    # Irrelevant computations and red herrings
    decoy_sum = sum(1 for t in timing_log if t > 1)  # unused
    shadow_buffer = [t * 0.99 for t in timing_log if t < 0.5]  # dead path
    metadata_envelope = {'version': '2.1', 'mode': 'diagnostic'}  # irrelevant
    dummy_counter = Counter(['A', 'B', 'A'])  # meaningless use

    # Distractor: complex but unused transformation
    transformed_signals = [
        {'raw': s, 'adjusted': s * 1.05, 'status': 'valid'} 
        for s in signal_block['samples'] if s > 0.1
    ]

    # Multiple intermediate values — only some are used
    phase_status = analyze_phase_coherence(timing_log)
    integrity_score = evaluate_signal_integrity(signal_block)
    calib_rating = compute_calibration_weight(config_map)
    fingerprint_hash = generate_timing_fingerprint(exec_sequence)
    anomaly_flag = detect_anomaly_pattern(log_entries)
    recursion_diag = recursive_diagnostic_probe(6)
    trace_valid = validate_consistency_trace([10, 20, 30, 40])

    # Red herring variables
    temp_normalization = sum(timing_log) / len(timing_log) if timing_log else 0  # unused
    alignment_index = math.sin(fingerprint_hash) * 100  # misleading
    debug_weight = calib_rating ^ 15  # bit op distraction

    # Actual dependency chain
    base_metric = integrity_score * 2
    adjusted_metric = base_metric + (calib_rating // 10)
    if phase_status and not anomaly_flag:
        adjusted_metric += 5
    if flags.get('override_safety', False):
        adjusted_metric *= 2
    security_check = flags.get('secure_mode', True) and not flags.get('debug_bypass', False)
    timing_influence = int(sum(timing_log[:3]) * 10) if len(timing_log) >= 3 else 0

    # Final computation — depends on specific prior results
    final_diagnostic = adjusted_metric + timing_influence
    if security_check:
        final_diagnostic -= 3

    # This print must be present and match format
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execution setup
timing_data = [0.12, 0.15, 0.18, 0.22, 0.25]
system_diagnostics = {
    'timing': 0.12,
    'amplitude': 0.85,
    'mode': 'active'
}
log_input = [
    {'timing': 0.12, 'amplitude': 0.85, 'score': 0.88},
    {'timing': 0.15, 'amplitude': 0.72, 'score': 0.75},
    {'timing': 0.18, 'amplitude': 0.91, 'score': 0.92},
    {'timing': 0.22, 'amplitude': 0.67},
    {'timing': 0.25, 'amplitude': 0.88, 'score': 0.15}
]
system_flags = {
    'override_safety': False,
    'secure_mode': True,
    'debug_bypass': False,
    'legacy_support': True
}

# Critical execution point
final_diagnostic = aggregate_metrics(log_input, system_flags)