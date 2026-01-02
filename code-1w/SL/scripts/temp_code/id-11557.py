def calculate_system_load():
    base_nodes = 8
    expansion_factor = 1.75
    decay_rate = 0.92
    threshold = 42.0
    safety_margin = 2.5

    node_capacity = [base_nodes * (expansion_factor ** i) for i in range(6)]
    temp_buffer = [round(x * decay_rate, 2) for x in node_capacity]

    current_load = 0.0
    peak_capacity = 0.0
    stress_test_phases = 5
    diagnostic_log = []

    for phase in range(stress_test_phases):
        load_increment = (phase + 1) * 3.8
        current_load += load_increment

        if current_load > threshold:
            # Simulate emergency shutdown protocol
            recovery_buffer = sum(temp_buffer[:3]) / len(temp_buffer[:3])
            fallback_mode = True
            break

        # Update peak only during normal operation
        projected_peak = current_load * 1.15
        if projected_peak > peak_capacity:
            peak_capacity = projected_peak

        # Log non-critical diagnostics
        diagnostic_entry = f'Phase{phase}:Load{round(current_load,1)}'
        diagnostic_log.append(diagnostic_entry)

        # Irrelevant adjustment to simulate dynamic tuning
        base_nodes += 0.5  # Does not affect logic
        dummy_check = base_nodes % 2 == 0

    # Post-loop red herring computation
    final_stability_index = (current_load * peak_capacity) / (threshold + 1e-9)
    auxiliary_score = len(diagnostic_log) * 1.5

    print(f"Result: {peak_capacity}")

calculate_system_load()