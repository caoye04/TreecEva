def evaluate_performance(entries, threshold):
    total_events = len(entries)
    critical_count = 0
    warning_count = 0
    info_count = 0
    normalized_weights = []

    # Preprocess: classify and weight events
    for entry in entries:
        level = entry['level'].upper()
        duration = entry['duration_sec']
        if level == 'CRITICAL':
            critical_count += 1
            weight = duration * 3.0
        elif level == 'WARNING':
            warning_count += 1
            weight = duration * 1.5
        elif level == 'INFO':
            info_count += 1
            weight = duration * 0.5
        else:
            weight = duration * 0.1  # Unknown levels get minimal weight
        normalized_weights.append(weight)

    # Compute aggregate metrics (some are red herrings)
    avg_duration = sum(e['duration_sec'] for e in entries) / total_events if total_events > 0 else 0
    total_weight = sum(normalized_weights)
    weighted_average = total_weight / total_events if total_events > 0 else 0

    # Distractor computation: entropy-like measure (not used)
    probabilities = [w / total_weight for w in normalized_weights if total_weight > 0]
    import math
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0) if probabilities else 0.0

    # Case conversion distraction using string methods
    status_flags = ['alert', 'notify', 'resolve']
    upper_flags = [flag.upper() for flag in status_flags]
    flipped_flags = [flag[::-1] for flag in upper_flags]  # Reverse strings, unused

    # Key logic: performance score based on critical ratio and threshold
    critical_ratio = critical_count / total_events if total_events > 0 else 0
    compliance_factor = 1.0 if critical_ratio <= threshold else 0.6

    # Bonus for low warnings, penalty for high info noise
    warning_ratio = warning_count / total_events
    info_ratio = info_count / total_events
    stability_bonus = 1.0
    if warning_ratio < 0.2:
        stability_bonus += 0.1
    if info_ratio > 0.5:
        stability_bonus -= 0.1  # Noise reduces clarity

    # Final score calculation
    base_score = 100 * compliance_factor * stability_bonus
    adjustment = (weighted_average - avg_duration) * 0.25  # Minor tweak
    final_score = base_score + adjustment

    # Dead code path (never reached due to logic above)
    if entropy > 3.0:
        final_score *= 1.05  # Hypothetical high-complexity bonus

    return int(round(final_score))

# Simulated log data
log_data = [
    {'level': 'critical', 'duration_sec': 120},
    {'level': 'warning', 'duration_sec': 45},
    {'level': 'info', 'duration_sec': 10},
    {'level': 'info', 'duration_sec': 8},
    {'level': 'warning', 'duration_sec': 60},
    {'level': 'info', 'duration_sec': 15},
    {'level': 'info', 'duration_sec': 20},
    {'level': 'info', 'duration_sec': 25},
    {'level': 'critical', 'duration_sec': 90},
    {'level': 'info', 'duration_sec': 5}
]

base_threshold = 0.25

# Execution point of interest
final_score = evaluate_performance(log_data, base_threshold)
print(f"Result: {final_score}")