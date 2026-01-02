def analyze_signal(samples, config):
    # Irrelevant transformation (distractor)
    normalized = [round(x * config['gain'] / 1.7, 2) for x in samples]
    offset_correction = sum(normalized[:3]) - config['baseline']

    # Real processing begins: frequency band isolation
    low_band = [x for x in samples if 10 <= x <= 90]
    mid_band = [x for x in samples if 90 < x <= 180]
    high_band = [x for x in samples if x > 180]

    # Misleading diagnostic path (dead code)
    if len(low_band) > len(high_band):
        stability_index = 0.85
    else:
        stability_index = 0.42  # Never used later

    # Actual relevant computation: entropy approximation
    total_power = sum(x**2 for x in samples)
    band_powers = [
        sum(x**2 for x in low_band),
        sum(x**2 for x in mid_band),
        sum(x**2 for x in high_band)
    ]

    entropy_components = []
    for power in band_powers:
        if power > 0 and total_power > 0:
            p = power / total_power
            entropy_components.append(-p * __import__('math').log(p))
        else:
            entropy_components.append(0)

    # Red herring: unused signal quality metric
    quality_score = len([x for x in normalized if x > 50]) / len(normalized) if normalized else 0

    # Destructuring assignment with partial relevance
    (primary_entropy, secondary_entropy, _) = sorted(entropy_components, reverse=True)

    # Decoy function call with side effect that does nothing
    def apply_filter(data_slice): return data_slice[::2]
    filtered_view = apply_filter(mid_band)  # Unused

    # Core logic masked by noise: threshold-based classification
    thresholds = {'low': 85, 'high': 160}
    classified = []
    for x in samples:
        if x < thresholds['low']:
            classified.append('L')
        elif x <= thresholds['high']:
            classified.append('M')
        else:
            classified.append('H')

    # Slicing and set operations to identify unique transition points
    transitions = [classified[i:i+2] for i in range(len(classified)-1)]
    transition_pairs = [tuple(pair) for pair in transitions]
    unique_transitions = set(transition_pairs)

    # Critical intermediate result (misleading but not final)
    transition_count = len(unique_transitions)

    # Linear search for first major fluctuation
    fluctuation_point = -1
    for i in range(1, len(samples)):
        if abs(samples[i] - samples[i-1]) > 75:
            fluctuation_point = i
            break

    # Another irrelevant bit manipulation trail
    bit_encoded = 0
    for x in samples[:4]:
        bit_encoded ^= int(x) & 0xFF
    checksum = bit_encoded << 2  # Dead end

    # Real data flow resumes: build profile based on entropy and distribution
    temp_profile = {
        'entropy': round(sum(entropy_components), 4),
        'fluctuation': fluctuation_point,
        'class_dist': {
            'L': classified.count('L'),
            'M': classified.count('M'),
            'H': classified.count('H')
        }
    }

    # Threshold map with decoy keys
    threshold_map = {
        'critical': 180,
        'warning': 100,
        'clear': 50,
        'unused_flag': True,
        'mode_bias': 0.0
    }

    # Final aggregation function buried in distractions
    def aggregate_measures(profile, limits):
        base_score = profile['entropy'] * 1000
        if profile['fluctuation'] > 0:
            base_score -= 150
        if profile['class_dist']['H'] >= 3:
            base_score += 220
        if profile['class_dist']['L'] == 0:
            base_score += 95
        return int(round(base_score))

    final_diagnostic = aggregate_measures(temp_profile, threshold_map)
    Result: final_diagnostic