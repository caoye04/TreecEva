import math

# Irrelevant helper function (decoy)
def normalize_vector(v):
    magnitude = sum(x ** 2 for x in v) ** 0.5
    return [x / magnitude for x in v] if magnitude else v

# Unused transformation table (distractor data)
transform_map = {
    'A': [1, 3, 6, 10],
    'B': [2, 5, 9, 13],
    'C': [4, 8, 12, 16]
}

# Simulated sensor readings (partially relevant, partially red herring)
sensor_data = [18, 24, 36, 42, 54, 60]
offset_correction = sum([x for x in sensor_data if x % 12 == 0])  # Distractor: used nowhere

# Flow state parameters
flow_state = {
    'velocity': 17.3,
    'viscosity': 0.85,
    'turbulence': [0.12, 0.18, 0.21, 0.15],
    'layers': list(range(3, 12, 2))
}

# Pressure node configuration (critical input)
pressure_nodes = [
    {'id': 'P1', 'p': 101.3, 'active': True},
    {'id': 'P2', 'p': 98.7, 'active': False},
    {'id': 'P3', 'p': 103.1, 'active': True},
    {'id': 'P4', 'p': 99.4, 'active': True}
]

# Auxiliary computation with misleading intermediate result (dead path)
baseline_flux = 0
for node in pressure_nodes:
    if node['p'] > 100 and node['active']:
        baseline_flux += node['p'] * 0.01
baseline_flux = round(baseline_flux, 2)  # Computed but unused

# Complex conditional expression (short-circuit logic)
is_stable = len(flow_state['turbulence']) > 3 and flow_state['velocity'] > 15 or flow_state['viscosity'] < 0.7

# Bit manipulation for checksum (irrelevant to final answer)
data_checksum = 0
for val in sensor_data[:4]:
    data_checksum ^= int(val * 1.3) & 0xFF

# Core calculation function with nested logic
def calculate_diffusion(flow, nodes):
    # Extract active pressures using list comprehension and slicing
    active_pressures = [n['p'] for n in nodes if n['active']][::-1]  # Reverse slice

    # Compute layer-weighted diffusion coefficient
    layers = flow['layers']
    turb_avg = sum(flow['turbulence']) / len(flow['turbulence'])
    diff_coeff = flow['velocity'] * (1 + turb_avg) / flow['viscosity']

    # Apply non-linear transformation across pressure differentials
    grad_sum = 0.0
    for i in range(len(active_pressures) - 1):
        delta_p = abs(active_pressures[i] - active_pressures[i + 1])
        # Conditional exponent based on stability and parity
        exponent = 2 if is_stable and (i % 2 == 0) else 1.5
        grad_sum += delta_p ** exponent

    # Combine with weighted harmonic mean of layers (slice middle three)
    mid_layers = layers[1:4]
    harmonic_factor = len(mid_layers) / sum(1/x for x in mid_layers)

    # Final diffusion gradient
    result = grad_sum * diff_coeff * harmonic_factor

    # Red herring: modify result based on checksum parity (but not actually used)
    temp_offset = data_checksum % 4
    if temp_offset > 2:
        result -= temp_offset * 0.1

    return result

# Trigger point: what is thermal_gradient after this?
calculate_diffusion(flow_state, pressure_nodes)  # First call - no assignment
thermal_gradient = calculate_diffusion(flow_state, pressure_nodes)

# Print required output
print(f"Target result: {thermal_gradient}")