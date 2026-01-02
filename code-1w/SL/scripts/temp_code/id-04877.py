def analyze_signal_integrity(raw_samples, threshold=0.75):
    # Simulate multi-stage signal processing with extensive distractions
    normalized = [x / max(raw_samples) for x in raw_samples]
    filtered = [x for x in normalized if x > 0.1]
    segments = [filtered[i:i+4] for i in range(0, len(filtered), 4)]
    
    # Distractor: irrelevant transformation chain
    temp_shadow = [sum(segment) ** 0.5 for segment in segments if len(segment) == 4]
    temp_shadow = [t - 0.1 for t in temp_shadow if t > 0.5]
    shadow_copy = temp_shadow.copy()  # Dead reference
    adjustment_factor = 1.0

    # Real logic begins: identify high-integrity segments
    integrity_flags = []
    for s in segments:
        if len(s) == 0:
            continue
        peak = max(s)
        avg = sum(s) / len(s)
        stability = sum(1 for x in s if abs(x - avg) < 0.2 * avg)
        if peak > threshold and stability >= 3:
            integrity_flags.append(True)
        else:
            integrity_flags.append(False)

    # Distractor: unused recursive function
    def explore_combinations(n, r):
        if r == 0 or n == r:
            return 1
        return explore_combinations(n-1, r-1) + explore_combinations(n-1, r)

    # Distractor: complex but unused data structure
    metadata_map = {
        'version': '2.1',
        'calibration': [0.11, 0.22, 0.33],
        'history': [(1, 'init'), (2, 'scan'), (3, 'abort')],
        'checksum': sum([len(str(x)) for x in raw_samples[:3]])
    }

    # Distractor: misleading statistical calculation
    outlier_count = 0
    mean_norm = sum(normalized) / len(normalized)
    for val in normalized:
        if abs(val - mean_norm) > 2 * mean_norm:
            outlier_count += 1

    # Actual critical path: track active segments using slicing
    active_segments = []
    for i, flag in enumerate(integrity_flags):
        if flag:
            if i+1 < len(segments):  # Look ahead conditionally
                merged = segments[i] + segments[i+1][:2]  # Use slice to take first two of next
                active_segments.append(merged)

    # Distractor: bit manipulation with no impact
    mask = 0b101010
    encoded = 0
    for v in raw_samples[:5]:
        encoded ^= int(v) & mask
    encoded = (encoded << 2) | (encoded >> 6)

    # Distractor: string obfuscation
    status_log = "Signal:OK|Node:5|Err:0"
    log_parts = status_log.split('|')
    node_id = int(log_parts[1].split(':')[1])
    if 'ERR' in status_log.upper():
        adjustment_factor *= 0.9

    # Critical intermediate result
    baseline_score = sum(len(seg) for seg in active_segments) * 1.5

    # Distractor: redundant list copying
    backup_segments = [list(seg) for seg in active_segments]
    del backup_segments  # Unused

    # Compute aggregate metrics with slicing history
    aggregate_metrics = [baseline_score]
    for seg in active_segments:
        segment_metric = (
            min(seg) * 100 + 
            len(seg) + 
            (max(seg) > 0.8) * 5
        )
        aggregate_metrics.append(segment_metric)
    
    # Key statement: final_diagnostic depends on last metric and active count
    final_diagnostic = aggregate_metrics[-1] + len(active_segments)

    # Irrelevant final adjustments (never executed due to prior definition)
    if False:
        correction = sum(metadata_map['calibration'])
        final_diagnostic = round(final_diagnostic * correction, 3)

    print(f"Result: {final_diagnostic}")

# Hidden seed ensures deterministic execution
import random
random.seed(42)

# Input data derived from fixed pattern
base_data = [120, 180, 200, 90, 210, 195, 88, 205, 170, 160, 220]
sample_input = [x * 0.01 + i*0.001 for i, x in enumerate(base_data)]

analyze_signal_integrity(sample_input)