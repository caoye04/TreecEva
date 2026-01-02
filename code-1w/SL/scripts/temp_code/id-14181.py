def calculate_stellar_decay(power_level, modifiers):
    decay_rate = 0.92
    adjusted_levels = []
    
    # Irrelevant pre-processing (distractor)
    temp_buffer = [x * 0.1 for x in modifiers if x > 3]
    buffer_sum = sum(temp_buffer)

    for i, mod in enumerate(modifiers):
        if i % 2 == 0:
            transformed = power_level * (mod ** 0.5) * decay_rate
        else:
            transformed = power_level / (mod + 1) + decay_rate * 10
        adjusted_levels.append(transformed)
    
    # Semi-relevant filtering using zip and enumerate
    filtered = []
    for idx, (orig, adj) in enumerate(zip(modifiers, adjusted_levels)):
        if orig >= 4 or adj > 50:
            filtered.append(adj * 0.85)
    
    # Misleading aggregation path (dead end)
    phantom_total = 0
    for val in adjusted_levels:
        if val < 0:
            phantom_total += val
    
    # Actual computation path
    exponent_shift = sum(1 for x in modifiers if x in [2, 4, 6])
    base_accum = 0
    for val in filtered:
        base_accum += val / (exponent_shift or 1)
    
    helper_fn = lambda x: x * 0.9
    final_adjust = helper_fn(base_accum)
    
    # Key assignment
    final_flux = int(final_adjust - 15)  # Final deterministic result
    return final_flux

# Setup inputs
base_power = 75
exponents = [2, 5, 4, 7, 6]

# Dead code: unused function
def unused_diagnostic():
    return [i**2 for i in range(5)]

# Unused variables (distraction)
baseline_calibration = 3.14159
redundant_flag = True
aux_data = {'status': 'idle', 'mode': 'passive'}

# Execution point
final_flux = calculate_stellar_decay(base_power, exponents)
print(f"Result: {final_flux}")