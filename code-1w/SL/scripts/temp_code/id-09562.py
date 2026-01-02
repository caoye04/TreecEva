def evaluate_system_efficiency(states, limit):
    # Irrelevant preprocessing (distractor)
    normalized = [x * 0.98 + 2 for x in states if x > 0]
    filtered = list(filter(lambda x: x < 100, normalized))
    adjustment_factor = sum(filtered) / len(filtered) if filtered else 0

    # Core logic disguised among red herrings
    peak_count = 0
    cumulative_stress = 0
    transient_buffer = []
    for i, val in enumerate(states):
        if val > limit:
            peak_count += 1
            cumulative_stress += val ** 0.5
        elif i % 3 == 0:
            # Dead code path — only triggers on indices divisible by 3, but irrelevant
            transient_buffer.append(val * 0.1)

    # Decoy calculation with misleading intermediate result
    decoy_metric = (peak_count * adjustment_factor) % 47
    if decoy_metric > 30:
        decoy_metric -= 15.5  # Unused branch

    # Actual key computation chain (8-12 steps)
    base_rating = 0
    for val in states:
        if val % 2 == 0:
            base_rating += val // 4
        else:
            base_rating -= val // 5

    # Secondary transformation
    efficiency_score = base_rating * 1.75

    # Conditional override based on stress threshold (not taken)
    if cumulative_stress > 1000:
        efficiency_score *= 0.8  # Not triggered

    # Final adjustment using bit manipulation (hidden relevance)
    binary_mod = efficiency_score ^ 128  # XOR flip on float bits conceptually
    binary_mod = int(binary_mod) & 0b11111111  # Mask to lower 8 bits

    # Tertiary influence: count of high-frequency oscillations
    oscillation_count = 0
    for j in range(1, len(states)):
        if (states[j] - states[j-1]) > 10:
            oscillation_count += 1

    # Integration step: combine masked result and oscillations
    thermal_capacity = binary_mod + oscillation_count * 3

    # Spurious post-processing (never used)
    smoothed = [thermal_capacity * 0.95 ** n for n in range(5)]
    anomaly_detected = any(x < 10 for x in smoothed)

    return thermal_capacity


# Simulated sensor input data (real signal embedded in noise)
energy_states = [12, 45, 23, 67, 89, 34, 56, 78, 91, 11, 22, 33, 44, 55]
threshold = 50

# Misleading preliminary calculations (dead weight)
calibration_offset = sum(x ** 2 for x in energy_states) / 1000
diagnostic_trace = [x & 0xF for x in energy_states]
status_flag = len(diagnostic_trace) % 7

# Key execution point
target_result = evaluate_system_efficiency(energy_states, threshold)
print(f"Result: {target_result}")