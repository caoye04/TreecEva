def analyze_signal_integrity(raw_samples, threshold=0.75):
    # Irrelevant preprocessing: string-based header validation (distractor)
    header = "SIG_PROC_V2"
    version_tag = header.lower().replace('_', '').strip()
    is_valid = len(version_tag) == 9 and 'v' in version_tag
    temp_result = [x * 1.05 for x in raw_samples if x > 0.1]  # Distractor list

    # Signal binning with misleading intermediate stats
    binned = {i: 0 for i in range(5)}
    for val in raw_samples:
        bucket = min(int(val * 4), 4)
        binned[bucket] += 1

    # Decoy statistical analysis
    mean_val = sum(raw_samples) / len(raw_samples) if raw_samples else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in raw_samples) / len(raw_samples) if raw_samples else 0
    entropy_approx = -sum(x * __import__('math').log(x + 1e-8) for x in binned.values())  # Misleading complexity

    # Core logic disguised among noise: identify anomalous bursts
    burst_flags = []
    for i in range(1, len(raw_samples)):
        if raw_samples[i] > threshold and raw_samples[i-1] < threshold * 0.5:
            burst_flags.append(i)

    # Secondary decoy: simulate frequency sweep analysis (unused)
    sweep_pattern = [raw_samples[i] - raw_samples[i % (len(raw_samples)//2)] for i in range(len(raw_samples)//4)]
    normalized_sweep = [abs(x) / (max(sweep_pattern) + 1e-6) for x in sweep_pattern]  # Dead computation path

    # Real signal processing chain (obscured)
    transition_points = []
    for idx in burst_flags:
        if idx + 2 < len(raw_samples):
            avg_next = (raw_samples[idx+1] + raw_samples[idx+2]) / 2
            if avg_next > threshold * 0.9:
                transition_points.append(idx)

    # Tertiary distraction: unused recursive helper (red herring)
    def recursive_energy(seq, depth=0):
        if depth >= 3 or len(seq) < 2:
            return 0
        return seq[0] + 0.5 * recursive_energy(seq[1:], depth + 1)

    # Actual transformation pipeline (buried in middle)
    filtered_indices = [i for i in transition_points if i % 3 == 0]
    weighted_sum = sum(raw_samples[i] * (i % 7 + 1) for i in filtered_indices)

    # Simulated diagnostic calibration (partly relevant)
    base_metric = len(filtered_indices) * 100
    adjustment_factor = __import__('math').sin(len(burst_flags) * 0.5)
    calibrated = base_metric + (weighted_sum * 50) + (adjustment_factor * 10)

    # Final red herrings: tuple unpacking with dummy values
    diagnostics_log = (calibrated, len(temp_result), entropy_approx, sum(sweep_pattern))
    primary_diag, size_marker, _, _ = diagnostics_log  # Unpack but ignore some

    # Critical assignment (target execution point)
    final_diagnostic = int(primary_diag + 0.5)  # Round to nearest integer

    # Unused complex data structure (interference)
    history_tracker = {
        'trace': [{'step': i, 'val': raw_samples[i]} for i in range(0, len(raw_samples), max(1, len(raw_samples)//5))],
        'flags': set(burst_flags),
        'metrics': {'raw': mean_val, 'var': variance_proxy}
    }

    # Output required result
    print(f"Result: {final_diagnostic}")
    return final_diagnostic


def aggregate_metrics(chain, offset=0):
    # Dummy wrapper to increase abstraction depth (distractor)
    return int(chain + offset * 1.2)

# Data setup (real input)
input_samples = [
    0.2, 0.3, 0.6, 0.8, 0.9, 0.1, 0.4, 0.85, 0.92, 0.7,
    0.2, 0.65, 0.88, 0.91, 0.87, 0.3, 0.5, 0.77, 0.89, 0.93
]

processing_chain = analyze_signal_integrity(input_samples)
baseline_offset = len([x for x in input_samples if x > 0.8])  # Count high-amplitude samples

final_diagnostic = aggregate_metrics(processing_chain, baseline_offset)