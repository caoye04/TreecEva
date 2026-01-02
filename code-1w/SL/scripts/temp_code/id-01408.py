def analyze_signal_integrity(raw_data, noise_floor):
    baseband_signals = {x ^ 2 for x in raw_data if x > noise_floor}
    reference_peaks = {x + 1 for x in baseband_signals}
    purified_signals = {x for x in reference_peaks if x % 3 == 0}
    critical_thresholds = {x * 2 for x in range(5, 15)}
    transient_mask = {x | 1 for x in purified_signals}  # Irrelevant derived set
    backup_check = sum(purified_signals) % 7  # Minor distraction
    filtration_score = len(purified_signals & critical_thresholds)
    return filtration_score

result = analyze_signal_integrity([12, 15, 8, 9, 14, 18], 10)
print(f"Result: {result}")