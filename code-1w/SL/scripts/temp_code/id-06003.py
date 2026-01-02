def calculate_final_score(records, importance_weights):
    base_values = []
    temp_sum = 0
    
    for idx, (key, value) in enumerate(records.items()):
        if idx % 2 == 0:
            transformed = value ** 2
        else:
            transformed = value * 3 + 1
        base_values.append(transformed)
    
    # Irrelevant accumulator (distractor)
    dummy_accumulator = 0
    for i in range(len(base_values)):
        dummy_accumulator += i * base_values[i]  # Not used later

    # Real computation starts here
    weighted_components = list(map(lambda x, w: x * w, base_values, importance_weights))
    
    adjustment_factor = 1.0
    if len(weighted_components) > 3:
        adjustment_factor = 0.9
    
    intermediate_total = sum(weighted_components)
    
    # Secondary adjustment using zip and enumerate (semi-relevant)
    offsets = [0.5, -0.2, 0.3, -0.1]
    for i, (comp, offset) in enumerate(zip(weighted_components, offsets)):
        if i < len(offsets):
            intermediate_total -= comp * offset  # Minor correction

    final_normalized = intermediate_total * adjustment_factor
    
    # Additional red herring: complex but unused expression
    shadow_value = sum([base_values[j] ** 0.5 for j in range(0, len(base_values), 2)])
    shadow_value *= 0.75
    
    return int(final_normalized)

# Main execution
config_flags = {'debug': False, 'trace': True}
data_map = {'input_a': 4, 'input_b': 5, 'input_c': 3, 'input_d': 6}
weights = [0.8, 1.2, 0.5, 1.0]

# Unused helper (dead code path - distractor)
def analyze_pattern(seq):
    return [x & (x + 1) for x in seq if x > 0]

# Key computation
final_score = calculate_final_score(data_map, weights)
print(f"Result: {final_score}")