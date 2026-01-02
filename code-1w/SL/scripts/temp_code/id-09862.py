import itertools

# Simulate sensor array diagnostics with noise filtering and pattern analysis
def main():
    raw_readings = [127, 255, 89, 190, 64, 230, 100, 150]
    calibration_map = {i: val % 16 for i, val in enumerate(raw_readings)}
    normalized = [r / 255.0 for r in raw_readings]

    # Irrelevant transformation: color space simulation (distraction)
    rgb_profile = [(n * 255, n * 120, n * 60) for n in normalized]
    hex_codes = [f'{int(r):02X}{int(g):02X}{int(b):02X}' for r, g, b in rgb_profile]

    # Decoy function: unused but plausible
    def compute_color_temperature(r, g, b):
        return (r * 0.299 + g * 0.587 + b * 0.114) * 100

    # Noise threshold calculation (partially relevant)
    base_noise = sum(normalized) / len(normalized)
    thresholds = { 'low': base_noise * 0.3, 'high': base_noise * 0.7 }

    # Signal extraction using bit manipulation (red herring)
    signal_peaks = []
    for val in raw_readings:
        if (val & 128) and (val ^ 255) < 100:
            signal_peaks.append(val >> 2)

    # Real processing begins: filter and transform
    filtered = [x for x in normalized if thresholds['low'] < x < thresholds['high']]
    amplified = [round(f * 2.1, 4) for f in filtered]

    # Create data windows (using itertools)
    window_pairs = list(itertools.pairwise(amplified))
    
    # Dummy statistical analysis (distractor)
    avg_pair_product = sum(p[0] * p[1] for p in window_pairs) / len(window_pairs) if window_pairs else 0
    entropy_proxy = -sum(f * __import__('math').log(f) for f in amplified if f > 0)

    # Transform data into phase states (core path)
    phase_states = []
    for a in amplified:
        if a < 0.5:
            phase_states.append(1)
        elif a < 0.7:
            phase_states.append(2)
        else:
            phase_states.append(3)

    # Configuration dict with decoy keys
    config = {
        'version': '3.1.4',
        'mode': 'diagnostic',
        'threshold': 1.8,
        'weights': [0.1, 0.3, 0.6],
        'debug': True,
        'decay_factor': 0.91  # unused
    }

    # Transform phase sequence into grouped patterns
    grouped = []
    current = []
    for state in phase_states:
        if current and current[-1] != state:
            grouped.append(current)
            current = [state]
        else:
            current.append(state)
    if current:
        grouped.append(current)

    # Compute pattern scores
    pattern_scores = []
    for group in grouped:
        duration = len(group)
        intensity = group[0] * 0.5
        score = duration * intensity
        pattern_scores.append(round(score, 3))

    # Misleading aggregation (looks important, isn't used)
    total_energy = sum(pattern_scores) * config['weights'][2]
    peak_analysis = max(pattern_scores) if pattern_scores else 0

    # Critical transformation: apply exponential decay weighting
    transformed_data = []
    for i, score in enumerate(reversed(pattern_scores)):
        weight = 1.3 ** i  # growing weight forward in time
        transformed_data.append(score * weight)

    # Main analysis function
    def analyze_pattern(data, cfg):
        if not data:
            return -1
        
        # Apply threshold filter
        threshold = cfg['threshold']
        valid = [x for x in data if x > threshold]
        
        # Multiple branching logic with nesting
        if len(valid) == 0:
            result = sum(data) / len(data)
        elif len(valid) == 1:
            bonus = 0
            if valid[0] > threshold * 1.5:
                bonus = 5
            elif valid[0] > threshold * 1.2:
                bonus = 3
            result = valid[0] + bonus
        else:
            sorted_valid = sorted(valid, reverse=True)
            top_two = sorted_valid[:2]
            if top_two[0] > 2 * top_two[1]:
                result = top_two[0] * 0.8
            else:
                result = (top_two[0] + top_two[1]) * 0.6
        
        # Final adjustment (this is where answer comes from)
        adjustment = 0
        for d in data:
            if d > threshold:
                adjustment += 0.1
        return round(result + adjustment, 4)

    # Execute critical statement
    final_diagnostic = analyze_pattern(transformed_data, config)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")

    # Dead code path (never reached)
    def postprocess(result):
        import math
        return math.floor(result * 10) / 10

    return final_diagnostic

if __name__ == "__main__":
    main()