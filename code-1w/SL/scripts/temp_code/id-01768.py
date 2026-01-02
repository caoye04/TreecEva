def analyze_signal(samples, threshold=0.75):
    # Irrelevant preprocessing block (distractor)
    normalized = [s / max(samples) for s in samples]
    filtered = [f for f in normalized if f > 0.1]
    stats = {'mean': sum(filtered) / len(filtered), 'count': len(filtered)}

    # Core transformation chain (relevant)
    fft_magnitude = lambda x: abs(x.real ** 2 + x.imag ** 2) ** 0.5
    frequency_bins = []
    for i in range(len(samples)):
        angle = 2 * 3.14159 * i / len(samples)
        complex_sample = complex(samples[i] * 0.5, samples[(i+1)%len(samples)] * 0.5)
        frequency_bins.append(fft_magnitude(complex_sample))

    # Signal envelope detection (partially relevant)
    envelope = []
    for i in range(len(frequency_bins)):
        prev = frequency_bins[i-1] if i > 0 else 0
        curr = frequency_bins[i]
        next_val = frequency_bins[(i+1)%len(frequency_bins)]
        if curr > prev and curr > next_val and curr > threshold * max(frequency_bins):
            envelope.append(i)

    # Red herring: unused feature extraction
    zero_crossings = 0
    for i in range(1, len(normalized)):
        if normalized[i-1] * normalized[i] < 0:
            zero_crossings += 1

    # Decoy function that looks important but isn't called
    def compute_entropy(data):
        from math import log
        prob = [data.count(x)/len(data) for x in set(data)]
        return -sum(p * log(p) for p in prob if p > 0)

    # Actual relevant logic begins here
    sample_pairs = [(samples[i], samples[(i+3)%len(samples)]) for i in range(0, len(samples), 3)]
    transformed = [a ^ b for a, b in [(int(x), int(y)) for x, y in sample_pairs]]  # Bit manipulation

    checksum = 0
    for val in transformed:
        while val:
            checksum += val & 1
            val >>= 1

    # Conditional expression with string distraction
    status_flag = 'valid' if checksum % 2 == 0 else 'corrupted'
    debug_trace = [f"{i}:{hex(v)}" for i, v in enumerate(transformed) if i % 2 == 0]

    # Key data structure - tuple unpacking and list reversal
    metadata = (len(envelope), checksum, len(samples))
    primary_index, parity_key, scale_factor = metadata
    reversed_debug = debug_trace[::-1][:primary_index]

    # String manipulation distractor
    token_chain = ''.join(reversed_debug).replace('0x', '').upper()
    validation_score = sum(ord(c) - ord('A') for c in token_chain if c.isalpha())

    # Actual metric computation (hidden in middle)
    base_metric = sum(frequency_bins[i] for i in envelope) / (scale_factor or 1)
    adjustment = 0.1 * parity_key
    final_adjusted = base_metric - adjustment

    # Diagnostic aggregation functions
    def aggregate_metrics(metrics_list, extra_diagnostics):
        combined = sum(metrics_list) * 0.9
        penalty = extra_diagnostics.get('overhead', 0) * 0.05
        return int((combined - penalty) * 1000)

    processing_chain = [final_adjusted, adjustment, base_metric]
    diagnostics = {
        'overhead': len(token_chain),
        'flags': [status_flag],
        'trace': reversed_debug
    }

    # Critical execution point
    final_diagnostic = aggregate_metrics(processing_chain, diagnostics)
    print(f"Result: {final_diagnostic}")