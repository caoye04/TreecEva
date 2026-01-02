def analyze_system_performance(data_points):
    # Preprocess: extract magnitude and phase
    magnitudes = [abs(x) for x in data_points]
    phases = [1 if x >= 0 else -1 for x in data_points]
    
    # Compute derived metrics with some red herrings
    avg_magnitude = sum(magnitudes) / len(magnitudes)
    max_phase_shift = max(phases) - min(phases)
    
    # Distractor: irrelevant frequency analysis
    frequency_domain = list(map(lambda x: x * 0.5, magnitudes))
    spectral_entropy = sum([x * x for x in frequency_domain])  # unused
    
    # Core logic begins
    threshold = 3.5
    stable_windows = 0
    for i in range(len(magnitudes) - 1):
        if abs(magnitudes[i] - magnitudes[i+1]) < threshold:
            stable_windows += 1

    # Secondary distraction: simulate temperature drift (unused)
    temp_drift = 0
    for mag in magnitudes:
        temp_drift += mag * 0.01
        if temp_drift > 10:
            temp_drift = 0  # reset, but irrelevant

    # Convergence metric based on trend consistency
    trend_consistency = 0
    for i in range(1, len(phases)):
        if phases[i] == phases[i-1]:
            trend_consistency += 1

    convergence = trend_consistency / (len(phases) - 1) if len(phases) > 1 else 1
    
    # Stability factor from window analysis
    stability_factor = stable_windows / (len(magnitudes) - 1) if len(magnitudes) > 1 else 1
    
    # Irrelevant normalization attempt
    normalized_stability = round(stability_factor * 100) / 100
    
    # Key function call embedded
    def calculate_rating(conv, stab):
        base_rating = conv * 50
        bonus = stab * 30 if stab > 0.6 else stab * 10
        penalty = 10 if max_phase_shift == 2 else 0
        return base_rating + bonus - penalty
    
    final_score = calculate_rating(convergence, stability_factor)
    
    # Dead code path - never executed but looks important
    if False:
        fallback_score = sum(magnitudes) / 10
        final_score = fallback_score

    print(f"Result: {final_score}")

# Execute with fixed input
data_input = [2.1, -1.9, 2.0, 2.2, -2.05, -1.95, 2.15]
analyze_system_performance(data_input)