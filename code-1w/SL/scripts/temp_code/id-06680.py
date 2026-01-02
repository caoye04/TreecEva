from itertools import combinations

# Simulate thermodynamic state analysis with mixed computational logic
def analyze_system_stability(temperatures, pressure_levels):
    stability_flags = []n    cumulative_metric = 0
    adjustment_factor = 1.25

    for i, temp in enumerate(temperatures):
        # Irrelevant computation - red herring
        temp_adj = temp * adjustment_factor + 273.15
        exceeded_threshold = False

        # Nested condition with partial relevance
        if temp > 300:
            for p in pressure_levels:
                if p > 101.3:
                    stability_flags.append(True)
                    cumulative_metric += (p / temp) * 0.1
                    exceeded_threshold = True
                    break
            if not exceeded_threshold:
                stability_flags.append(False)
        else:
            stability_flags.append(temp % 2 == 0)

    # Distractor: complex but unused structure
    state_vectors = list(combinations([1, 2, 3, 4], 2))
    vector_sum = sum(a * b for a, b in state_vectors)

    return len(stability_flags), cumulative_metric


def calculate_thermal_properties(state_config):
    base_value = state_config.get('metric', 0)
    phase_shift = state_config.get('stability', False)
    thermal_capacity = 0

    # Core relevant logic
    if phase_shift:
        thermal_capacity = base_value ** 2
    else:
        thermal_capacity = base_value * 1.5

    # Irrelevant transformations
    normalized = thermal_capacity / 100.0
    formatted_result = f"{normalized:.3f}"
    entropy_proxy = 0
    for i in range(5):
        entropy_proxy += i ** 2

    return thermal_capacity

# Main execution flow
initial_temps = [298, 305, 310, 290]
pressures = [98.7, 102.1, 110.5, 95.0]

# Execute analysis with side-effect computations
analysis_result = analyze_system_stability(initial_temps, pressures)
metric_score = analysis_result[1] * 10
is_stable = analysis_result[0] > 3

# Construct equilibrium state - key input to target function
equilibrium_state = {
    'metric': metric_score,
    'stability': is_stable,
    'timestamp': 1678886400,
    'nodes': [1, 1, 2, 3, 5, 8],
    'version': '2.1a'
}

# Critical statement - where answer is determined
temperature_offset = 0
for t in initial_temps:
    temperature_offset += (t // 10) % 3

temperature_offset *= 2

target_variable_init = 55.0
unused_intermediate = target_variable_init ** 0.5

termal_capacity = calculate_thermal_properties(equilibrium_state)

print(f"Result: {thermal_capacity}")