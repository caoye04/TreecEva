def analyze_system_metrics(raw_data, thresholds):
    # Preprocessing phase with red herrings
    normalized = [x * 0.95 for x in raw_data if x > 0]
    temp_buffer = [abs(x - 10) for x in normalized if x < 5]
    adjustment_factor = sum(temp_buffer) / len(normalized) if normalized else 0

    # Core logic disguised among side computations
    signal_peaks = []
    for i, val in enumerate(normalized):
        if i > 0 and val > normalized[i-1]:
            if val > thresholds[0]:
                signal_peaks.append(val * 1.2)
        elif i < len(normalized) - 1 and val == normalized[i+1]:
            signal_peaks.append(val * 0.85)  # Dead path: equality rare in real data

    # Irrelevant statistical tracking
    avg_peak = sum(signal_peaks) / len(signal_peaks) if signal_peaks else 0
    peak_variance = sum((p - avg_peak) ** 2 for p in signal_peaks) / len(signal_peaks) if signal_peaks else 0

    # Key computation chain (5-8 steps with interdependencies)
    base_energy = sum(normalized)
    filtered_peaks = [p for p in signal_peaks if p > avg_peak]  # Only above-average matter
    enhancement_mod = len(filtered_peaks) * 0.75
    dynamic_offset = int(base_energy / (len(raw_data) + 1))

    # State-dependent accumulation
    accumulator = 0
    for i in range(3):  # Fixed small loop depth
        if i % 2 == 0:
            accumulator += dynamic_offset // (i + 1)
        else:
            accumulator -= len(temp_buffer) // max(i, 1)

    # Final derived values
    impact_factor = len([x for x in thresholds if x < base_energy])
    stability_bonus = int(enhancement_mod + adjustment_factor)
    gross_total = base_energy + accumulator + stability_bonus
    final_tally = gross_total - sum(p for p in signal_peaks if p < 8.0)

    # Critical execution point
    equilibrium_score = final_tally // (impact_factor + 1)

    # Output requirement
    print(f"Result: {equilibrium_score}")

    # Unused debug traces to increase interference
    debug_snapshot = {
        'raw_count': len(raw_data),
        'norm_count': len(normalized),
        'peak_count': len(signal_peaks),
        'adjustment': adjustment_factor,
        'variance': peak_variance
    }

    return equilibrium_score

# Input setup
input_data = [12, -3, 8, 4, 6, 15, 2, 9]
config_thresholds = [7, 14, 20]

# Execute
result = analyze_system_metrics(input_data, config_thresholds)