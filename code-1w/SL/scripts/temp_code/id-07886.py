def analyze_performance(metrics):
    baseline = sum(metrics) / len(metrics) if metrics else 0
    adjusted = [m * 1.1 for m in metrics if m > baseline]
    return sum(adjusted) if adjusted else baseline

metrics_data = [85, 90, 78, 92, 88, 76, 95]
performance_score = analyze_performance(metrics_data)

units = [
    {'type': 'A', 'count': 4, 'base_cap': 150},
    {'type': 'B', 'count': 3, 'base_cap': 200},
    {'type': 'C', 'count': 5, 'base_cap': 120}
]

efficiency_map = {
    'A': 0.88 + (performance_score - 85) * 0.002,
    'B': 0.82 + (performance_score - 85) * 0.0015,
    'C': 0.90 + (performance_score - 85) * 0.001
}

redundancy_factor = 1.15
maintenance_overhead = 0.95
placeholder_value = 999  # unused distractor
unused_list = [x ** 2 for x in range(10)]  # dead code path

scaling_mode = 'dynamic' if performance_score > 87 else 'static'

boost_multiplier = 1.05 if scaling_mode == 'dynamic' else 1.0

interim_results = []
for unit in units:
    base_total = unit['count'] * unit['base_cap']
    efficiency = efficiency_map[unit['type']]
    adjusted_capacity = base_total * efficiency
    
    if unit['type'] == 'B':
        adjusted_capacity *= boost_multiplier
    
    temp_log = f"Unit {unit['type']}: {adjusted_capacity:.2f}"
    interim_results.append(adjusted_capacity)

system_peak = sum(interim_results) * redundancy_factor
energy_loss = system_peak * 0.03
net_output = system_peak - energy_loss

operational_safety = net_output * maintenance_overhead

# Simulate load balancing adjustment
if len(units) > 2 and scaling_mode == 'dynamic':
    balance_shift = net_output * 0.015
    operational_safety += balance_shift

# Final computation point
final_capacity = calculate_system_capacity(units, efficiency_map)

# Dummy function to encapsulate core logic
def calculate_system_capacity(unit_list, eff_map):
    total = 0
    for u in unit_list:
        cap = u['count'] * u['base_cap'] * eff_map[u['type']]
        if u['type'] == 'B':
            cap *= 1.05  # dynamic boost applied only to B
        total += cap
    total *= 1.15  # redundancy
    total *= 0.97  # energy loss
    total *= 0.95  # maintenance
    if len(unit_list) > 2:
        total += total * 0.015  # balancing bonus
    return int(total)

Result: final_capacity