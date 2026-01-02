def calculate_inertia(forces):
    inertia = 0
    for i, f in enumerate(forces):
        if i % 2 == 0:
            inertia += f * (i + 1)
        else:
            inertia -= f // (i + 1)
    return inertia

# Simulate mechanical system response
def simulate_response(base_inputs):
    scaled = [x * 1.5 for x in base_inputs]
    offset = sum(scaled) / len(scaled)
    adjusted = [x + offset for x in scaled]
    return [int(x) for x in adjusted]

# Irrelevant helper: computes average magnitude (not used in final path)
def avg_magnitude(lst):
    return sum(abs(x) for x in lst) / len(lst)

# System calibration data
initial_forces = [12, -8, 15, 3, -6]

# Step 1: Apply simulation model to get adjusted forces
distortion_factor = 0.7
noisy_input = [f * distortion_factor for f in initial_forces]
adjusted_forces = simulate_response(noisy_input)

# Misleading intermediate computation (dead-end analysis)
peak_force = max(abs(f) for f in adjusted_forces)
force_range = max(adjusted_forces) - min(adjusted_forces)

# Normalize forces (semi-relevant transformation)
norm_const = sum(abs(f) for f in adjusted_forces) + 1e-5
normalized_forces = [int(f / norm_const * 100) for f in adjusted_forces]

# Key state tracking variables (only some are used later)
state_log = []
for idx, val in enumerate(adjusted_forces):
    state_log.append((idx, val, val ** 2))

# Red herring: frequency analysis of force patterns
freq_map = {}
for f in adjusted_forces:
    freq_map[f] = freq_map.get(f, 0) + 1

# Dummy loop with zip: correlates indices and normalized values (unused)
correlation_score = 0
for idx, norm_val in zip(range(len(adjusted_forces)), normalized_forces):
    if norm_val > 5:
        correlation_score += idx * norm_val

# Critical computation chain begins
baseline_shift = sum(adjusted_forces[:3]) // 3
filtered_forces = []
for f in adjusted_forces:
    if abs(f - baseline_shift) > 5:
        filtered_forces.append(f)
    else:
        filtered_forces.append(0)

# Final preparation before inertia calculation
trimmed_forces = [f for f in filtered_forces if f != 0]
while len(trimmed_forces) < len(adjusted_forces):
    trimmed_forces.append(0)

total_inertia = calculate_inertia(trimmed_forces)
print(f"Result: {total_inertia}")