def main():
    # Simulate quantum state energy levels with noise filtering
    raw_readings = [1.2, 3.4, 2.5, 0.8, 4.9, 3.3, 2.1, 1.7, 5.5]
    calibration_offset = 0.3
    filtered_readings = [x for x in raw_readings if x > 1.5]

    # Apply non-linear transformation to simulate quantum correction
    transformed_energies = list(map(lambda e: e ** 2 / (e + 1), filtered_readings))

    # Simulated decoherence weights (some are irrelevant)
    decoherence_weights = [0.9, 0.7, 0.85, 0.6, 0.75]
    weight_sum = sum(decoherence_weights)  # Used only for distraction
    avg_weight = weight_sum / len(decoherence_weights)

    # Normalize energies using sliding scale
    normalized_energies = []
    base_factor = 2.0
    for i, e in enumerate(transformed_energies):
        adjusted = e * (base_factor - 0.1 * i) if i % 2 == 0 else e * (base_factor - 0.05 * i)
        normalized_energies.append(adjusted)

    # Define dynamic threshold function (not used in final logic)
    def threshold_filter(x):
        return x > 2.5 and x < 8.0

    # Misleading secondary calculation (dead code path)
    secondary_scores = []
    for val in normalized_energies:
        if val > 3.0:
            secondary_scores.append(val * 0.5)
        else:
            continue  # Red herring branch

    # Core logic: identify stable states above dynamic threshold
    energy_states = [e for e in normalized_energies if e > 2.0]

    # Threshold as a closure (functional pattern)
    def make_threshold_ref(level):
        ref = level * 0.8
        return lambda x: x > ref

    threshold_func = make_threshold_ref(3.5)

    # Critical computation: calculate equilibrium score
    def calculate_equilibrium(states, threshold_fn):
        valid_states = [s for s in states if threshold_fn(s)]
        if not valid_states:
            return 0.0
        mean_state = sum(valid_states) / len(valid_states)
        # Apply quadratic stabilization factor
        stabilization = len(valid_states) ** 0.5
        return round(mean_state * stabilization, 4)

    equilibrium_score = calculate_equilibrium(energy_states, threshold_func)

    # Irrelevant logging computation
    log_entries = [f"State_{i}: {v:.2f}" for i, v in enumerate(normalized_energies)]
    entry_count = len(log_entries)

    # Final output
    print(f"Result: {equilibrium_score}")

if __name__ == "__main__":
    main()