def analyze_signal(samples, threshold_multiplier=1.7):
    # Irrelevant preprocessing block (distractor)
    normalized = [s / max(samples) for s in samples]
    filtered = [s for s in normalized if s > 0.1]
    snapshot = normalized[::2]  # Slicing - relevant later

    # Real computation begins: trend detection
    deltas = [samples[i+1] - samples[i] for i in range(len(samples)-1)]
    growth_peaks = [d for d in deltas if d > 0]
    decay_valleys = [abs(d) for d in deltas if d < 0]

    avg_growth = sum(growth_peaks) / len(growth_peaks) if growth_peaks else 0.0
    avg_decay = sum(decay_valleys) / len(decay_valleys) if decay_valleys else 0.0

    # Misleading metric (dead path)
    volatility_index = sum((d ** 2) for d in deltas) ** 0.5
    stability_score = 1 / (1 + volatility_index)  # Looks important, unused

    # Core logic: compute trend vectors using enumerate and zip
    trend_vectors = []
    for i, delta in enumerate(deltas):
        if i % 3 == 0:
            trend_vectors.append(delta * (i + 1))

    phase_weights = [1.1, 0.9, 1.2, 0.8]  # Oscillation pattern
    extended_deltas = deltas + [deltas[-1]] * (len(phase_weights) - len(deltas) % len(phase_weights))
    grouped = zip(*[extended_deltas[i::len(phase_weights)] for i in range(len(phase_weights))])

    weighted_phases = []
    for idx, group in enumerate(grouped):
        weighted_sum = sum(g * w for g, w in zip(group, phase_weights))
        weighted_phases.append(weighted_sum)

    # Baseline shift due to calibration drift (real effect)
    calibration_factor = 0.94
    adjusted_trend = [t * calibration_factor for t in weighted_phases]

    # Decoy function call (no side effects)
    def compute_entropy(arr):
        from math import log
        total = sum(arr)
        if total == 0: return 0.0
        probs = [a / total for a in arr if a != 0]
        return -sum(p * log(p) for p in probs)

    entropy_diagnostic = compute_entropy(adjusted_trend)  # Computed but not used

    # Actual signal aggregation
    trend_data = adjusted_trend[1::2]  # Take odd-indexed trends
    baseline_offset = sum(deltas[:5]) * 0.1

    def aggregate_metrics(trends, offset):
        magnitude = sum(abs(t) for t in trends)
        coherence = len([t for t in trends if t > 0]) / len(trends) if trends else 0
        penalty = 0.95 if coherence < 0.6 else 1.05
        return int((magnitude * penalty) + offset)

    final_diagnostic = aggregate_metrics(trend_data, baseline_offset)

    # Dead code branches (red herrings)
    if len(samples) > 100:
        dummy_cache = {i: val for i, val in enumerate(samples) if val % 2 == 0}
    else:
        temp_buffer = [0] * 10  # Unused allocation

    # Spurious control flow
    mode_flag = 'A'
    if mode_flag == 'Z':
        scaling_register = 2.0
    elif mode_flag == 'X':
        scaling_register = 1.5
    else:
        scaling_register = 1.0  # Default, not used later

    # Output the required result
    Result: final_diagnostic