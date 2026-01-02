def analyze_wave_interference():
    # Simulate multi-signal phase analysis with noise filtering
    frequencies = [12.5, 6.8, 9.1, 14.3, 7.2]
    amplitudes = [3.0, 5.5, 2.1, 4.4, 6.0]
    phases = [0.0, 1.57, 3.14, 0.785, 2.356]  # in radians

    # Irrelevant baseline metrics (distractor)
    baseline_power = sum(f * a for f, a in zip(frequencies, amplitudes))
    avg_frequency = sum(frequencies) / len(frequencies)

    # Signal quality weights (semi-relevant but not used directly)
    quality_weights = []
    for idx, amp in enumerate(amplitudes):
        weight = amp / (frequencies[idx] + 1)
        quality_weights.append(round(weight, 2))

    # Filter signals below average frequency (actual logic branch)
    filtered_indices = []
    for i, f in enumerate(frequencies):
        if f < avg_frequency:
            filtered_indices.append(i)

    # Compute weighted phase contributions only for filtered signals
    weighted_phase_sum = 0.0
    total_weight = 0.0
    count_contributing = 0

    for i in filtered_indices:
        amplitude = amplitudes[i]
        phase = phases[i]
        contribution = amplitude * abs(phase)
        weighted_phase_sum += contribution
        total_weight += amplitude
        count_contributing += 1

    # Dead code path - never executed due to data, adds distraction
    outlier_flag = False
    if any(a > 10 for a in amplitudes):
        outlier_flag = True
        normalization = max(amplitudes) ** 2

    # Final summation using accumulated values
    if total_weight > 0:
        final_sum = weighted_phase_sum / total_weight
    else:
        final_sum = 0.0

    # Correction based on contributing signal count
    correction_map = {0: 0.0, 1: 0.5, 2: 0.8, 3: 1.1, 4: 1.3, 5: 1.5}
    correction_factor = correction_map.get(count_contributing, 1.0)

    # Key computational statement
    net_phase_shift = final_sum * correction_factor

    # Additional unused derived metrics (distraction)
    phase_variance = sum((p - final_sum) ** 2 for p in phases if phases.index(p) in filtered_indices)
    coherence_index = phase_variance / (final_sum + 1e-5)

    print(f"Result: {net_phase_shift}")

analyze_wave_interference()