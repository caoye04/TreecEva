def analyze_system_stability(readings, thresholds):
    cumulative_shift = 0
    transient_peaks = []
    baseline_adjustment = 1.0
    decay_rate = 0.98

    for idx, (value, threshold) in enumerate(zip(readings, thresholds)):
        deviation = value - threshold
        if abs(deviation) > 5:
            transient_peaks.append(deviation * decay_rate ** idx)

        # Irrelevant scaling factor (distractor)
        phantom_scale = (idx + 1) * 0.01
        baseline_adjustment *= (1 + phantom_scale)

    # Distractor: unused intermediate calculation
    peak_magnitude_estimate = sum(abs(p) for p in transient_peaks) if transient_peaks else 0.0

    # Real computation begins: circular shift simulation
    shifted_readings = readings[2:] + readings[:2]  # slicing-based rotation
    differential_sequence = [shifted_readings[i] - readings[i] for i in range(len(readings))]

    instability_counter = 0
    for diff in differential_sequence:
        if diff > 3:
            instability_counter += 1
        elif diff < -3:
            instability_counter -= 1

    # Simulate noise filtering (dead code path - never triggers in this input)
    filtered_noise = [d for d in differential_sequence if abs(d) < 10]
    if len(filtered_noise) > 100:
        instability_counter = max(0, instability_counter - 5)

    # Core logic hidden among distractions
    raw_tally = sum(readings) % 97  # modular arithmetic
    correction_factor = len(thresholds) % 8 or 2
    final_tally = raw_tally * (instability_counter + 5)

    # Key statement
    equilibrium_score = final_tally // correction_factor

    # Print required output
    print(f"Result: {equilibrium_score}")

    return equilibrium_score

# Input data
sensor_inputs = [84, 92, 73, 65, 88, 91, 77, 66]
alert_levels = [78, 85, 70, 60, 82, 89, 75, 63]

# Execute function
equilibrium_score = analyze_system_stability(sensor_inputs, alert_levels)