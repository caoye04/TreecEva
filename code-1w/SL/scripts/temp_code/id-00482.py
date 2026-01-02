def simulate_reactor_stability(temperature_log, pressure_readings):
    stability_index = 0
    fluctuation_count = 0
    for i in range(len(temperature_log)):
        if temperature_log[i] > 750:
            stability_index += 1
        if i > 0 and abs(temperature_log[i] - temperature_log[i-1]) > 50:
            fluctuation_count += 1
    return stability_index

# Sensor data from reactor core over 6 time intervals
temperature_profile = [680, 720, 760, 800, 740, 690]
pressure_data = [45, 47, 51, 53, 49, 46]

# Irrelevant transformation (distractor)
normalized_temps = [round((t - 680) / 120 * 100) for t in temperature_profile]

# Secondary analysis: fuel rod efficiency (semi-relevant but not used in final answer)
fuel_efficiency_set = {abs(t - 750) for t in temperature_profile}
efficiency_score = sum(fuel_efficiency_set) // len(fuel_efficiency_set)

# Core calculation chain
baseline_shift = sum([p // 5 for p in pressure_data])  # Minor preprocessing
adjusted_temps = [t - baseline_shift for t in temperature_profile]

# Reactor phase classification based on adjusted temperature
reactor_phases = []
for temp in adjusted_temps:
    if temp < 700:
        reactor_phases.append('cool')
    elif temp < 780:
        reactor_phases.append('stable')
    else:
        reactor_phases.append('overheating')

# Helper function to compute thermal output
def calculate_thermal_output(phases):
    phase_weights = {'cool': 1, 'stable': 2, 'overheating': 3}
    total_weight = 0
    for phase in phases:
        total_weight += phase_weights[phase]
    
    # Extra logic with dead end (distractor)
    if 'overheating' in phases:
        contingency_buffer = 100
        for c in range(3):
            contingency_buffer -= c * 10  # Distractor computation
    
    # Real contribution: base capacity modulated by weight
    base_capacity = 1500
    degradation_factor = len([p for p in phases if p == 'overheating']) * 0.1
    net_capacity = base_capacity * (1 - degradation_factor)
    return int(net_capacity // total_weight)

# Final computation
thermal_capacity = 0
stability_result = simulate_reactor_stability(temperature_profile, pressure_data)
if stability_result >= 3:
    thermal_capacity = calculate_thermal_output(reactor_phases)

# Output result
Result: {thermal_capacity}