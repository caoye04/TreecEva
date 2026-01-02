def analyze_signal(samples, threshold=0.75):
    # Irrelevant preprocessing (distractor)
    normalized = [s / max(samples) for s in samples]
    filtered = [n for n in normalized if n > 0.1]
    entropy = 0.0
    for f in filtered:
        if f > 0:
            entropy -= f * __import__('math').log(f)

    # Relevant feature extraction
    peaks = [i for i, s in enumerate(samples) if s > threshold and i > 0 and samples[i-1] < s]
    peak_magnitudes = [samples[p] for p in peaks]
    avg_peak = sum(peak_magnitudes) / len(peak_magnitudes) if peak_magnitudes else 0

    # Distraction: unused transformation chain
    transformed = [__import__('math').sin(s * 0.1) for s in samples][::2]
    derived_matrix = [[t * 1.5 for _ in range(3)] for t in transformed]  # Dead structure

    # Real computation path begins here
    window_size = 4
    rolling_averages = [
        sum(samples[i:i+window_size]) / window_size
        for i in range(len(samples) - window_size + 1)
    ]

    # Destructuring assignment (tuple unpacking)
    first_avg, *middle_avgs, last_avg = rolling_averages

    # Bit manipulation for diagnostic signature (key step)
    sig_bits = 0
    for val in peak_magnitudes[:3]:
        shifted = int(val * 10) << 2
        sig_bits ^= shifted  # XOR accumulation

    # Dictionary-based state tracking (relevant)
    diagnostics = {
        'peak_count': len(peaks),
        'avg_magnitude': avg_peak,
        'signature': sig_bits,
        'stability': abs(first_avg - last_avg)
    }

    # Slicing and string-based encoding (distractor with partial relevance)
    status_str = "anomalous" if diagnostics['stability'] > 2.0 else "stable"
    code_name = status_str.upper()[::-1][:3]  # Reverse and slice
    diagnostics['code'] = code_name

    # UNUSED recursive function (dead code path)
    def traverse_diags(data):
        if isinstance(data, list):
            return sum(traverse_diags(d) for d in data)
        return hash(str(data))

    # Actual processing chain construction (critical)
    baseline = sum(samples) / len(samples)
    deviations = [abs(baseline - s) for s in samples]
    high_dev = [d for d in deviations if d > baseline * 0.5]
    dev_ratio = len(high_dev) / len(deviations)

    # Control flow with logical operations
    is_complex = len(peaks) > 2 and dev_ratio > 0.3 and diagnostics['stability'] < 5.0
    priority_flag = (diagnostics['peak_count'] & 3 == 1) or (len(middle_avgs) % 2 == 0)

    processing_chain = {
        'base': baseline,
        'quality': min(1.0, dev_ratio * 2),
        'complexity': int(is_complex),
        'priority': int(priority_flag)
    }

    # Final aggregation function (answer point)
    def aggregate_metrics(chain, diag):
        # Mix of arithmetic and dictionary lookups
        score = chain['base'] * 10
        score += diag['peak_count'] * 5
        score -= diag['signature'] // 10
        score *= (1 + chain['quality'])
        if chain['complexity']:
            adjustment = diag['avg_magnitude'] if diag['avg_magnitude'] > 1.0 else 0.5
            score += adjustment * chain['priority'] * 2
        return round(score, 4)

    final_diagnostic = aggregate_metrics(processing_chain, diagnostics)

    # Print required result
    print(f"Result: {final_diagnostic}")