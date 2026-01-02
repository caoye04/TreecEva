def analyze_signal_predictions(base_frequency, harmonics, threshold=0.7):
    raw_spectrum = {i for i in range(1, base_frequency + 1) if base_frequency % i == 0}
    harmonic_set = set()
    for h in harmonics:
        for i in range(h, base_frequency + h, h):
            if i <= base_frequency:
                harmonic_set.add(i)
    
    signal_coverage = raw_spectrum | harmonic_set
    prediction_model = [base_frequency // 3, base_frequency // 2, (2 * base_frequency) // 3]
    predicted_coverage = {x for x in prediction_model if x > threshold * (base_frequency / 4)}
    
    coverage_overlap = signal_coverage & predicted_coverage
    
    # Irrelevant metric (minor distraction)
    efficiency_score = len(harmonic_set) / (base_frequency * 0.1) if base_frequency else 0
    
    return coverage_overlap

result_set = analyze_signal_predictions(36, [6, 9, 12])
coverage_overlap = result_set
print(f"Target result: {len(coverage_overlap)}")