def analyze_signal(samples, threshold=0.75):
    # Irrelevant preprocessing block (distractor)
    normalized = [s / max(samples) for s in samples]
    filtered = [f for f in normalized if f > 0.1]
    entropy = 0
    for f in filtered:
        if f > 0:
            entropy -= f * __import__('math').log(f)

    # Core logic disguised among red herrings
    peaks = []
    for i in range(1, len(normalized) - 1):
        if normalized[i] > normalized[i-1] and normalized[i] > normalized[i+1]:
            peaks.append(i)

    # Decoy transformation chain
    transformed_peaks = list(map(lambda x: (x ** 2 + 3) % len(samples), peaks))
    peak_values = [samples[p] for p in peaks]

    # Distractor: unused complex structure
    history_log = [{'index': idx, 'value': samples[idx], 'flag': False} for idx in range(0, len(samples), 5)]
    for entry in history_log:
        entry['checksum'] = sum([int(c) for c in str(entry['index']) + str(entry['value'])])

    # Real processing begins — buried in noise
    def extract_features(data):
        avg = sum(data) / len(data)
        variance = sum((x - avg) ** 2 for x in data) / len(data)
        return {'mean': avg, 'variance': variance, 'cv': variance / avg if avg != 0 else 0}

    feature_set = extract_features(peak_values)

    # Misleading secondary analysis path (dead end)
    shadow_analysis = []
    for i, val in enumerate(samples):
        if val > threshold * max(samples):
            shadow_analysis.append({'pos': i, 'weight': val ** 0.5})

    # Another decoy function that's never called
    def compute_fractal_dimension(seq):
        acc = 0
        for j in range(len(seq) - 1):
            acc += abs(seq[j+1] - seq[j])
        return acc / len(seq) if seq else 0

    # Tuple unpacking distraction
    a, b = len(peaks), len(shadow_analysis)
    b, a = a, b  # Swap for no reason

    # Real but obscured logic: process only every second peak
    active_indices = [peaks[i] for i in range(0, len(peaks), 2) if i < len(peaks)]
    core_readings = [samples[i] for i in active_indices]

    # Bit manipulation red herring
    magic_key = 0
    for r in core_readings:
        magic_key ^= int(r) & 0xF
        magic_key = (magic_key << 1) | (magic_key >> 3)
        magic_key &= 0xF

    # Real metric computation (well hidden)
    base_score = sum(core_readings) / len(core_readings) if core_readings else 0
    adjustment = len(active_indices) * 0.25
    raw_diagnostic = base_score + adjustment

    # String-based distractor — uses string methods
    status_flags = ['alert', 'nominal', 'trace', 'spike']
    flag_strings = [s.upper().replace('A', '@') for s in status_flags]
    checksum_str = ''.join(flag_strings)
    str_entropy = sum([checksum_str.count(c) for c in set(checksum_str)])

    # Enumerate and zip used in irrelevant context
    indices = list(range(len(status_flags)))
    paired = list(zip(indices, status_flags))
    labeled = [f"{i}:{s}" for i, s in enumerate(paired)]

    # Actual aggregation function (critical)
    def aggregate_metrics(chain, report):
        # This is where real answer is formed
        total = 0
        for step in chain:
            if 'diagnosis' in step:
                total += step['diagnosis']
            elif 'impact' in step:
                total += step['impact'] * 0.1
        return total + (report.get('consistency', 0) * 0.01)

    # Processing chain with one relevant entry
    step_1 = {'action': 'filter', 'data_len': len(filtered)}
    step_2 = {'action': 'detect', 'peaks_found': len(peaks), 'diagnosis': raw_diagnostic}
    step_3 = {'action': 'validate', 'impact': 5, 'status': 'passed'}
    processing_chain = [step_1, step_2, step_3]

    diagnostics = {
        'consistency': str_entropy,
        'anomalies': len(shadow_analysis),
        'version': 'v2.3'
    }

    final_diagnostic = aggregate_metrics(processing_chain, diagnostics)
    print(f"Result: {final_diagnostic}")