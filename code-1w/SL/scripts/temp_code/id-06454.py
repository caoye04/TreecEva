def calculate_stress_distribution(factors, config):
    base_magnitude = sum(factors) * config['scaling']
    adjustment = 0
    
    # Simulate material damping (irrelevant to final result)
    damping_ratio = 0.15
    natural_frequency = 42.0
    transient_response = damping_ratio * natural_frequency  # Dead computation

    temp_result = list(map(lambda x: x ** 2 if x > 0 else 0, factors))
    energy_buffer = sum(temp_result) / (len(temp_result) + 1e-8)

    # Core logic begins
    threshold = config['threshold']
    filtered_loads = [f for f in factors if abs(f) > threshold]
    
    # Secondary transformation (some distraction)
    normalized = []
    max_val = max(filtered_loads) if filtered_loads else 1
    for val in filtered_loads:
        norm = (val / max_val) * config['amplification']
        normalized.append(abs(norm))

    # State tracking with irrelevant counters
    step_count = 0
    convergence_reached = False
    while not convergence_reached and step_count < 5:
        step_count += 1
        if sum(normalized) < 100 or step_count == 10:
            convergence_reached = True

    # Key calculation path
    decay_factor = 0.9 ** len(normalized)
    aggregate = sum(normalized) * decay_factor

    # Red herring: unused structural check
    integrity_check = True
    for i in range(len(normalized)):
        if normalized[i] > 50 and i % 2 == 0:
            integrity_check = False
            break

    # Final derivation
    final_stress = aggregate * base_magnitude / (config['resistance'] + 1)
    return int(final_stress)

# Simulation setup
stress_factors = [3.2, -1.8, 4.5, 0.7, -2.3, 6.1]
configuration = {
    'scaling': 2.1,
    'threshold': 2.0,
    'amplification': 1.8,
    'resistance': 3
}

# Irrelevant preprocessing
preliminary_scan = [x * 1.1 for x in stress_factors]
scan_magnitude = sum(preliminary_scan)

final_load = calculate_stress_distribution(stress_factors, configuration)
print(f"Target result: {final_load}")