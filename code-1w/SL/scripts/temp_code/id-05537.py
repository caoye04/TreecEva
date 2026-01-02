def calculate_critical_energy(flow, eff):
    base_energy = 3.7 * flow
    adjusted_eff = eff if eff > 0.8 else 0.8
    penalty = 15 if flow < 100 else 0
    return int(base_energy * adjusted_eff - penalty)

mass_flow = 89
efficiency_ratio = 0.83
initial_warning = "Flow rate low"
diagnostic_code = 200  # Normal status
energy_threshold = calculate_critical_energy(mass_flow, efficiency_ratio)
print(f"Result: {energy_threshold}")