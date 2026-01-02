from itertools import accumulate

# Simulate multi-phase sensor data calibration with noise filtering and trend analysis
def analyze_sensor_phases(raw_readings):
    calibrated = [x * 0.95 + 1.2 for x in raw_readings]
    filtered = [val for val in calibrated if val > 5.0]  # Remove low-noise outliers

    # Compute rolling differences (deltas)
    deltas = [filtered[i+1] - filtered[i] for i in range(len(filtered)-1)]
    
    # Misleading computation: unused energy metric
    energy_sum = sum([d**2 for d in deltas])
    avg_magnitude = energy_sum / len(deltas) if deltas else 0

    # Trend detection using sign changes (zero crossings)
    zero_crossings = 0
    for i in range(1, len(deltas)):
        if deltas[i-1] < 0 <= deltas[i] or deltas[i-1] >= 0 > deltas[i]:
            zero_crossings += 1

    # Introduce distractor state tracking (not directly used)
    state_log = []
    current_state = 'STABLE'
    for d in deltas:
        if d > 1.5:
            current_state = 'HIGH'
        elif d < -1.5:
            current_state = 'LOW'
        state_log.append(current_state)

    # Real processing path: cumulative trend strength
    trend_strength = list(accumulate(abs(d) for d in deltas))
    if not trend_strength:
        return 0

    # Simulate cyclic behavior across 3 operational cycles
    cycle_contributions = []
    for cycle_index in range(1, 4):
        # Each cycle applies a decayed weight to later trends
        weighted_cycle_value = sum(trend_strength[i] * (0.8 ** i) for i in range(len(trend_strength)) if i % 3 == cycle_index % 3)
        cycle_contributions.append(weighted_cycle_value)

    # Distractor: harmonic mean calculation (unused)
    harmonic_mean = 0
    if cycle_contributions:
        reciprocals = [1/c for c in cycle_contributions if c != 0]
        if reciprocals:
            harmonic_mean = len(reciprocals) / sum(reciprocals)

    # Key execution point: compute equilibrium score
    final_tally = int(sum(cycle_contributions) * 1.1)
    cycle_index = 3  # Last cycle index from loop
    equilibrium_score = final_tally // (cycle_index + 1)
    
    # Additional red herring: entropy-like measure
    probabilities = [abs(d)/sum(abs(d) for d in deltas) for d in deltas if sum(abs(d) for d in deltas) > 0]
    entropy = -sum(p * __import__('math').log(p) for p in probabilities if p > 0)

    return equilibrium_score

# Generate synthetic sensor readings
base_pattern = [8, 6, 7, 5, 3, 0, 9, 1]
synthetic_data = [val + (i % 4) * 0.3 for i, val in enumerate(base_pattern * 3)]

result = analyze_sensor_phases(synthetic_data)
print(f"Target result: {result}")