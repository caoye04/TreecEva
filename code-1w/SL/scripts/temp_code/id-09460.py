from itertools import combinations

# System diagnostics for thermal regulation units
unit_ids = ['TURBINE-A', 'TURBINE-B', 'TURBINE-C']
base_rating = 85
operational_threshold = 70
stress_factors = [1.1, 0.9, 1.3, 0.8]
redundancy_checks = list(combinations([1, 0, 1, 1], 3))

# Simulate environmental stress impact
adjusted_stress = [round(sf ** 1.5, 2) for sf in stress_factors if sf > 0.85]
ambient_offset = sum(adjusted_stress) / len(adjusted_stress) if adjusted_stress else 0

# Phantom diagnostic routine (irrelevant to final result)
def analyze_redundancy(checks):
    valid_count = 0
    for c in checks:
        if sum(c) >= 2:
            valid_count += 1
    return valid_count

redundancy_score = analyze_redundancy(redundancy_checks)
system_health = 'STABLE' if redundancy_score > 2 else 'WARNING'

# Core efficiency calculation with state tracking
startup_sequence = [True, False, True]
efficiency_log = []
for step in startup_sequence:
    if step:
        base_rating += 5
    efficiency_log.append(base_rating)

# Key computation point
initial_efficiency = efficiency_log[0]
efficiency_factor = efficiency_log[-1] / 100.0

# Critical assignment with distractor context
thermal_capacity = base_rating * efficiency_factor ** 2

# Post-processing noise
capacity_margin = thermal_capacity * 0.15
diagnostic_trace = {"peak": thermal_capacity + capacity_margin, "floor": thermal_capacity - capacity_margin}
final_report = f"Capacity: {diagnostic_trace['peak']:.2f} (with margin)"

# Output target result
print(f"Result: {thermal_capacity}")