def calculate_grid_load():
    voltage_levels = [230, 400, 480]
    current_flows = [15, 25, 30]
    efficiency_ratings = [0.92, 0.95, 0.98]  # Irrelevant distractor list

    # Calculate active power per phase using P = V * I
    active_powers = []
    for i in range(len(voltage_levels)):
        phase_power = voltage_levels[i] * current_flows[i]
        active_powers.append(phase_power)

    # Apply load balancing factor across three-phase system
    phase_factor = 1.73  # Approximate sqrt(3) for three-phase AC

    total_phase_power = sum(active_powers) * phase_factor

    # Additional irrelevant computation (distractor at intervention level 5)
    avg_efficiency = sum(efficiency_ratings) / len(efficiency_ratings)
    normalized_load = total_phase_power / (max(voltage_levels) * max(current_flows))

    print(f"Result: {total_phase_power}")

calculate_grid_load()