def calculate_equilibrium(states):
    adjustment_factor = 0.85
    temp_sum = sum(s ** 0.5 for s in states if s > 0)
    norm_const = len(states) + 1e-5
    return int(temp_sum / norm_const * adjustment_factor)

# Simulate quantum energy state transitions
data_stream = [16, 25, 9, 0, 36, 49, 4]
duplicate_filter = set()
filtered_states = []
for val in data_stream:
    if val not in duplicate_filter:
        filtered_states.append(val)
        duplicate_filter.add(val)

# Irrelevant transformation: reverse and scale (not used in final calculation)
reversed_scaled = [x * 0.1 for x in reversed(data_stream)]
scaling_reference = sum(reversed_scaled) / len(reversed_scaled)

# State categorization (semi-relevant: only non-zero values matter)
categorized = {"high": [], "low": [], "zero": []}
for state in filtered_states:
    if state == 0:
        categorized["zero"].append(state)
    elif state > 25:
        categorized["high"].append(state)
    else:
        categorized["low"].append(state)

# Primary computation path
energy_states = [s for s in filtered_states if s != 0]  # Remove zero states
normalization_offset = len(categorized["zero"]) * 0.1  # Minor offset (unused)

# Key computational step
index_map = {i: idx for i, idx in enumerate(energy_states)}
pairwise_ratios = [energy_states[i] / (energy_states[i-1] + 1e-5) for i in range(1, len(energy_states))]
smoothness_score = sum(abs(pairwise_ratios[i] - pairwise_ratios[i-1]) for i in range(1, len(pairwise_ratios)))

# Final equilibrium calculation
equilibrium_score = calculate_equilibrium(energy_states)

# Distractor: complex unpacking and unused tracking
(*initial, mid, *rest), _ = zip(energy_states, [equilibrium_score] * len(energy_states)), scaling_reference
tracking_log = []
for i, val in enumerate(energy_states):
    if i % 2 == 0:
        tracking_log.append(f"Step {i}: {val}")

# Output result
print(f"Result: {equilibrium_score}")