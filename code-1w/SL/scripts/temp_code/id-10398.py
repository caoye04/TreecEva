def analyze_signal(samples):
    # Irrelevant preprocessing (distractor)
    normalized = [x / max(abs(max(samples)), abs(min(samples))) for x in samples]
    filtered = [x for x in normalized if abs(x) > 0.1]
    energy = sum(x * x for x in filtered)

    # Relevant recursive transformation
    def bit_reversed_fft(data):
        if len(data) <= 1:
            return data
        even = bit_reversed_fft(data[0::2])
        odd = bit_reversed_fft(data[1::2])
        return [even[i] + odd[i] for i in range(len(even))] + \
               [even[i] - odd[i] for i in range(len(odd))]

    transformed = bit_reversed_fft(samples)

    # Decoy function (never used)
    def spectral_entropy(signal):
        magnitude = [abs(x) for x in signal]
        total = sum(magnitude)
        if total == 0: return 0
        probabilities = [m / total for m in magnitude]
        from math import log
        return -sum(p * log(p) for p in probabilities if p > 0)

    # Distractor: fake clustering attempt
    clusters = {}
    for i, val in enumerate(transformed):
        key = int(val) // 5
        clusters.setdefault(key, []).append(val)

    # Real processing begins here
    magnitude_spectrum = [abs(x) for x in transformed]
    avg_magnitude = sum(magnitude_spectrum) / len(magnitude_spectrum)

    # Simulated hardware thresholds via lambda (required feature)
    threshold_fn = lambda x: x > avg_magnitude * 0.75

    # Dummy statistical checks (irrelevant)
    variance = sum((x - avg_magnitude) ** 2 for x in magnitude_spectrum) / len(magnitude_spectrum)
    kurtosis = sum((x - avg_magnitude) ** 4 for x in magnitude_spectrum) / (len(magnitude_spectrum) * (variance ** 2)) if variance != 0 else 0

    # Data structure manipulation red herring
    stats_map = {
        'mean': avg_magnitude,
        'variance': variance,
        'kurtosis': kurtosis,
        'peak': max(magnitude_spectrum),
        'energy': energy  # reused from earlier
    }

    critical_bands = [x for x in magnitude_spectrum if threshold_fn(x)]

    # Complex conditional logic with nesting (4 levels)
    if len(critical_bands) > 5:
        if stats_map['kurtosis'] > 2:
            for idx in range(len(critical_bands)):
                if critical_bands[idx] > stats_map['peak'] * 0.8:
                    critical_bands[idx] *= 1.15  # boost strong signals
        else:
            critical_bands = critical_bands[:len(critical_bands)//2]
    else:
        fallback = [x * 0.5 for x in magnitude_spectrum]
        critical_bands.extend(fallback)

    # Core algorithm hidden in decoys
    def process_metrics(data, condition):
        valid = list(filter(condition, data))
        if not valid:
            return sum(data) / len(data)
        # Actual answer computation buried here
        weighted_sum = sum(i * val for i, val in enumerate(valid))
        scaling_factor = len(data) / (len(valid) or 1)
        temp_result = weighted_sum * scaling_factor
        # Final transformation using lambda (second use)
        adjust = lambda x: x * 0.9 if x > 100 else x * 1.1
        return int(adjust(temp_result)) if temp_result > 50 else int(temp_result * 1.05)

    # Unused recursive reducer (dead code path)
    def reduce_signal(seq, func):
        if len(seq) == 1:
            return seq[0]
        return func(seq[0], reduce_signal(seq[1:], func))

    # Key execution point
    final_diagnostic = process_metrics(transformed_data=magnitude_spectrum, threshold_fn=threshold_fn)
    print(f"Result: {final_diagnostic}")

# Ground truth input (deterministic)
signal_samples = [3, -7, 12, -4, 8, 15, -1, 6, 11, -9, 14, 2, -5, 10, 13, -6]
analyze_signal(signal_samples)
