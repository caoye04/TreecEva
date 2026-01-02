def calculate_equilibrium(states, factor):
    adjustment = 0
    temp_buffer = []
    cumulative_shift = 0

    for idx, (val, meta) in enumerate(zip(states, [x ** 0.5 for x in range(len(states))])):
        if idx % 2 == 0:
            adjusted_val = val * (factor + idx)
            temp_buffer.append(adjusted_val)
            if len(temp_buffer) > 2:
                adjustment += temp_buffer[-2] / (idx + 1)
        else:
            shifted = val - (meta * factor)
            cumulative_shift += shifted

    # Misleading computation: looks relevant but not used in final result
    outlier_count = sum(1 for x in states if x > 50)
    normalization_hint = ''.join([str(int(x) % 10) for x in states if x.is_integer()]).strip('')

    # Core logic disguised among distractions
    base_total = sum(temp_buffer)
    shift_correction = abs(cumulative_shift) if cumulative_shift != 0 else 1
    score = (base_total + adjustment) / shift_correction

    return int(score)

# Initialization block
energy_states = [4.0, 8.0, 15.0, 16.0, 23.0, 42.0]
dampening_factor = 1.5

# Red herring variables and operations
placeholder_data = {k: v for k, v in enumerate(['alpha', 'beta', 'gamma'])}
redundant_calc = max(energy_states) ** 2 - min(energy_states) ** 1.5
intermediate_snapshot = list(filter(lambda x: x > 10, energy_states))

# Key execution point
equilibrium_score = calculate_equilibrium(energy_states, dampening_factor)

# Final output
print(f"Result: {equilibrium_score}")