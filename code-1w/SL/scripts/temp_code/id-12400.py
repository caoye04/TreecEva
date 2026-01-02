def calculate_plant_efficiency(temperatures, pressures, flow_rates):
    total_energy = 0
    waste_heat = 0
    net_work_output = 0
    heat_input = 0
    efficiency_candidates = []
    temp_pressure_pairs = list(zip(temperatures, pressures))
    
    for i, (temp, pressure) in enumerate(temp_pressure_pairs):
        adjusted_temp = temp * (1 + 0.015 * pressure)
        energy_contribution = adjusted_temp * flow_rates[i]
        total_energy += energy_contribution
        
        if temp > 300 and pressure > 10:
            work_potential = energy_contribution * 0.62
            net_work_output += work_potential
            heat_loss = energy_contribution * 0.23
            waste_heat += heat_loss
        elif temp > 200:
            work_potential = energy_contribution * 0.41
            net_work_output += work_potential
            # Misleading partial reset (distractor)
            waste_heat -= waste_heat * 0.05
        else:
            continue

    # Irrelevant secondary loop - distractor
    stability_index = 0
    for idx, rate in enumerate(flow_rates):
        stability_index += (rate ** 0.5) * (idx + 1)
    normalized_stability = stability_index / len(flow_rates) if flow_rates else 0

    # Another red herring: unused variable calculation
    theoretical_max = max(temperatures) * max(pressures) * sum(flow_rates) * 0.001

    # Core logic embedded within noise
    for t in temperatures:
        if t > 250:
            heat_input += t * 0.85

    # Key statement
    thermal_efficiency = net_work_output / heat_input if heat_input else 0
    
    # Unused derived metrics to increase cognitive load
    performance_ratio = thermal_efficiency / (normalized_stability + 1e-5)
    efficiency_with_penalty = thermal_efficiency * (1 - waste_heat / (total_energy + 1e-9))

    # Final result output
    print(f"Result: {thermal_efficiency}")

# Inputs
temps = [450, 320, 180, 380]
pressures_list = [12, 14, 8, 11]
flow_vals = [2.5, 3.0, 1.8, 2.7]

# Execute
calculate_plant_efficiency(temps, pressures_list, flow_vals)