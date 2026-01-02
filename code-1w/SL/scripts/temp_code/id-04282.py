def calculate_efficiency(base, factors):
    if base <= 0:
        return 0
    
    # Irrelevant pre-processing (distractor)
    temp_cache = [i ** 2 for i in range(5) if i % 2 == 0]
    scaling_factor = sum(temp_cache) / 4 if temp_cache else 1
    
    # Semi-relevant transformation
    adjusted_factors = list(map(lambda x: x * 0.8 + 2, factors))
    
    # Core logic hidden among distractions
    raw_sum = sum(f for f in adjusted_factors if f > 5)
    penalty = len([f for f in adjusted_factors if f < 3])
    efficiency_score = (raw_sum - penalty * 1.5) * base
    
    # Dummy branching with no real effect
    if efficiency_score > 100:
        efficiency_score *= 0.95
    elif efficiency_score < 0:
        efficiency_score = abs(efficiency_score)

    # Final adjustment using dictionary lookup (relevant)
    modifiers = {'level1': 1.1, 'level2': 0.95, 'level3': 1.05}
    level_key = 'level' + str(min(int(base // 10) + 1, 3))
    efficiency_score *= modifiers.get(level_key, 1.0)

    return int(efficiency_score)

# Simulation parameters (some irrelevant)
initial_pressure = 230
ambient_stability = 74
phase_modifiers = [3.2, 6.1, 2.8, 8.5, 1.9]
logic_threshold = 12
redundant_flag = False

# Dead code path (distraction)
def unused_helper(x):
    return x ** 0.5 + 10

# Unused intermediate calculations
buffer_load = (initial_pressure * 0.01) ** 2
stability_index = ambient_stability if ambient_stability > 50 else 0

# Key execution point
thermal_capacity = calculate_efficiency(logic_threshold, phase_modifiers)

# Output result as required
print(f"Target result: {thermal_capacity}")