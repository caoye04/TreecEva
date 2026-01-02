def analyze_signal(samples, threshold=0.75):
    # Irrelevant preprocessing block (dead path)
    if len(samples) == 0:
        return {'status': 'empty', 'data': []}

    # Distractor: complex but unused transformation
    normalized = [abs(x) / max([abs(z) for z in samples]) if max([abs(z) for z in samples]) != 0 else 0 for x in samples]
    filtered = list(filter(lambda x: x > threshold, normalized))

    # Unused recursive function (decoy)
    def decay_sequence(n, rate=0.9):
        return [1] if n == 1 else decay_sequence(n-1, rate) + [decay_sequence(n-1, rate)[-1] * rate]

    # Real processing begins: extract peaks
    peaks = [i for i in range(1, len(samples)-1) if samples[i-1] < samples[i] > samples[i+1]]
    peak_values = [samples[i] for i in peaks]

    # Compute rolling average over window of 3 (with padding)
    padded = [0] + samples + [0]
    rolling_avg = [(padded[i] + padded[i+1] + padded[i+2]) / 3 for i in range(len(padded)-2)]

    # Extract rising edges
    rising_edges = [i for i in range(1, len(rolling_avg)) if rolling_avg[i] > rolling_avg[i-1]]

    # Compute energy as sum of squares
    energy = sum(x**2 for x in samples)

    # Distractor: set operations with no downstream use
    unique_magnitudes = set(round(abs(x), 2) for x in samples)
    high_mags = {x for x in unique_magnitudes if x > 1.0}
    low_mags = {x for x in unique_magnitudes if x <= 0.5}
    symmetric_diff = high_mags ^ low_mags  # unused

    # Simulate diagnostic flags using conditional expressions
    flag_a = 'OK' if len(peaks) > 3 else 'CHECK'
    flag_b = 'OK' if energy > 10 else 'ALERT'
    flag_c = 'OK' if len(rising_edges) > len(peaks) * 2 else 'STABLE'

    # Diagnostic score computed via lambda and conditional logic
    score_fn = lambda f: 2 if f == 'OK' else (1 if f == 'STABLE' else 0)
    raw_score = sum(score_fn(f) for f in [flag_a, flag_b, flag_c])

    # This dictionary is not used — red herring
    dummy_report = {
        'integrity': all(x > -10 for x in samples),
        'coherence': len(peaks) >= 2,
        'trend': 'rising' if sum(rolling_avg[-5:]) > sum(rolling_avg[:5]) else 'falling',
        'score': raw_score * 10
    }

    # Actual signal metric: weighted combination
    stability_metric = len(peaks) * 0.8 + len(rising_edges) * 0.3 - abs(len(samples) - 50) * 0.05
    return {'metric': stability_metric, 'flags': [flag_a, flag_b, flag_c], 'energy': energy}


def aggregate_metrics(chain, diag_map):
    base = diag_map['metric']
    penalty = 0
    for step in chain:
        if step.get('type') == 'filter' and step.get('active'):
            penalty += 0.1
        elif step.get('type') == 'amplify' and step.get('gain', 1) > 1.5:
            penalty -= 0.2  # improvement
    return int((base - penalty) * 100)  # deterministic integer output

# Main execution sequence
sensor_readings = [
    -0.2, 1.1, 0.5, -1.3, 2.2, 1.8, -0.1, 0.9, 1.6, 2.5,
    0.3, -0.5, 0.7, 1.4, 2.1, 1.9, 0.4, -0.3, 0.6, 1.0,
    1.2, 0.8, -0.4, 0.2, 1.7, 2.3, 1.5, 0.1, -0.6, 0.9
]

# Unused alternate data path (distractor)
alt_stream = [x * 1.5 for x in sensor_readings if x > 0.5]

# Processing configuration with multiple irrelevant fields
processing_chain = [
    {'type': 'filter', 'cutoff': 0.5, 'active': True},
    {'type': 'shift', 'amount': 1, 'active': False},  # no effect
    {'type': 'amplify', 'gain': 1.8, 'active': True},
    {'type': 'quantize', 'bits': 8, 'active': True}  # unused type
]

# Generate intermediate diagnostics (some values are misleading)
diagnostics = analyze_signal(sensor_readings, threshold=0.65)

# Critical assignment point
final_diagnostic = aggregate_metrics(processing_chain, diagnostics)

print(f"Target result: {final_diagnostic}")