def analyze_workload(inputs):
    total_chars = sum(len(s) for s in inputs)
    unique_chars = len(set(''.join(inputs)))
    avg_length = total_chars / len(inputs) if inputs else 0
    return total_chars, unique_chars, avg_length

inputs = ['task', 'flow', 'execute', 'pipeline', 'dispatch']

# Irrelevant transformation chain
shadow_data = [s[::-1].upper() for s in inputs]
temp_scores = [len(s) * (i + 1) for i, s in enumerate(shadow_data)]
weighted_sum = sum(temp_scores) // len(temp_scores) if temp_scores else 0

# Distractor variables
redundant_flag = False
dummy_counter = 0
for item in shadow_data:
    if 'X' in item:
        redundant_flag = True
    dummy_counter += 1

# Core logic disguised among distractions
base = len(inputs) * 100
modifier = sum(1 for s in inputs if len(s) > 4)
efficiency_factor = (modifier * 1.5) + (len(inputs) - modifier)

# Simulate system stress profile
stress_profile = []
for i in range(len(inputs)):
    cycle_value = (base // (i + 1)) if i > 0 else base
    if cycle_value % 2 == 0:
        stress_profile.append(cycle_value * 0.9)
    else:
        stress_profile.append(cycle_value * 1.1)

# Noise: unused aggregation
peak_stress = max(stress_profile) if stress_profile else 0
avg_stress = sum(stress_profile) / len(stress_profile) if stress_profile else 0

# Real computation buried here
intermediate = base + int(efficiency_factor * 10)

# Helper function with red herring parameters
def adjust_capacity(init, factor, stress_series):
    result = init
    factor_int = int(factor)
    for _ in range(factor_int):
        result += 5
        # Simulated decay correction
        if result > 300:
            result -= 2
    return result

# Key assignment
final_capacity = adjust_capacity(base, efficiency_factor, stress_profile)

# Print required output
print(f"Result: {final_capacity}")