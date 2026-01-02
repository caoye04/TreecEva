import math

# Irrelevant helper function (decoy)
def dummy_transform(data):
    return [x ** 0.5 for x in data if x > 5]

# Unused transformation matrix (red herring)
transform_matrix = [
    [1, 0, -1],
    [2, 1,  0],
    [0, -1, 1]
]

# Misleading intermediate calculation (dead path)
baseline_offset = sum([i * (i - 1) for i in range(7)]) // 3

# Real data: flow states from sensor array
def generate_flow_states():
    raw_signals = [12, 8, 15, 3, 9, 6]
    processed = []
    for idx, val in enumerate(raw_signals):
        if idx % 2 == 0:
            processed.append(val + 2)
        else:
            processed.append(val - 1)
    return processed  # Result: [14, 7, 17, 2, 11, 5]

# Secondary irrelevant computation (distractor)
redundant_aggregate = 0
for i in range(1, 10):
    redundant_aggregate += i * (i + 2) if i % 3 == 0 else 0

# Bit manipulation decoy (unused but plausible)
def obscure_bits(x):
    return ((x << 3) ^ 0b1010) & 0xFF

# Core logic: entropy-like metric on transformed states
def calculate_entropy(states):
    # Apply non-linear scaling using slicing and zip
    shifted = states[1:] + [states[0]]
    paired_diffs = [abs(a - b) for a, b in zip(states, shifted)]
    
    # Introduce lambda for weighted normalization (key step)
    normalize = lambda x, m: round(x / m, 6) if m != 0 else 0
    magnitude = sum(paired_diffs)
    weights = [normalize(diff, magnitude) for diff in paired_diffs]
    
    # Compute weighted sum with index coefficients (actual answer source)
    coefficient_map = {i: (i + 1) * 0.5 for i in range(len(weights))}
    flux_values = []
    for i, w in enumerate(weights):
        if i % 2 == 0:
            flux_values.append(w * coefficient_map[i] * 100)
        else:
            flux_values.append(w * coefficient_map[i] * 50)
    
    # Final aggregation through selective accumulation
    final_component = 0
    for j, fv in enumerate(flux_values):
        if j in [1, 3, 5]:
            final_component += fv * 1.1  # odd indices boosted
        else:
            final_component += fv * 0.9  # even indices reduced
    
    return int(round(final_component))

# Spurious post-processing (never called)
def finalize_output(arr):
    return [math.ceil(x * 1.05) for x in arr]

# Critical execution path begins here
flow_states = generate_flow_states()  # [14, 7, 17, 2, 11, 5]
corrupted_copy = flow_states[:]
corrupted_copy.reverse()

# Actual key statement
final_flux = calculate_entropy(flow_states)

# Print result as required
print(f"Result: {final_flux}")